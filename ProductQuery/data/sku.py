# -*- coding: utf-8 -*-

import random
import copy

from ProductQuery.data.DBparam import *


# TODO
def split_brand(brand):
    pass


# TODO
def find_item_url(pcid, cid, brand, model):
    pass


def get_model_data(pcid, cid, datamonth):
    try:
        df = pd.read_csv(f"data_pcid{pcid}cid{cid}.csv", encoding="utf_8_sig", index_col=0)
        # print("read local data")
    except FileNotFoundError:
        # print("read db data")
        sql = f"SELECT * FROM product_brain.product_brain_pcid{pcid} WHERE cid = '{cid}' and datamonth = '{datamonth}';"
        engine = get_pgsql_engine(Outer99, "report_dg")
        df = pd.read_sql(sql, con=engine)
        df = df.replace(np.nan, "")
        # drops = df[(df["brand"] == "")].index.tolist()
        # drops.extend(df[(df["model"] == "")].index.tolist())
        # df = df.drop(drops)

        df_model = df[["brand", "model"]].drop_duplicates(["brand", "model"])
        ids = set()
        while True:
            seed = random.randint(1e5, 1e8)
            if seed in ids:
                continue
            ids.add(seed)
            if len(ids) >= len(df_model):
                break
        df_model["id"] = [x for x in ids]
        df = pd.merge(df, df_model, how="inner", on=["brand", "model"])

        # TODO
        # get_url
        # TODO
        # split brand
        df.to_csv(f"data_pcid{pcid}cid{cid}.csv", encoding="utf_8_sig")
    # print("get df", len(df))
    return df


def split_text(text, tags, first=True):
    try:
        text = text.strip()
    except AttributeError:
        text = None
    if text is None or 0 == len(text):
        return None
    elif len(text) <= 2:
        res = set()
        res.add(text)
    elif "['" == text[:2] or "[\"" == text[:2]:
        res = set(eval(text))
        # print("eval", text, res)
    else:
        for split in splits:
            text = text.replace(split, " ")
        text = text.strip()
        res = set([x for x in filter(lambda seg: seg, text.split())])

    if not first:
        useless = set()
        useful = set()
        for item in res:
            if len(item) < 5:
                continue
            useless.add(item)
            tags = sorted(tags, key=lambda x: len(x), reverse=True)
            for tag in tags:
                if tag in item:
                    useful.add(tag)
                    item = item.replace(tag, "")

        if 0 != len(useless):
            res = res.difference(useless)
            res = res.union(useful)
    return res


def parse_json_tag(json_text):
    res = []
    try:
        data = eval(json_text)
    except Exception as e:
        # print(e)
        # print(json_text)
        raise e
    for tag, score in data.items():
        res.append([tag, float(score)])
    return res


def parse_json_target(json_text):
    res = []
    data = eval(json_text)
    for tag, subdata in data.items():
        for target, score in subdata.items():
            res.append([target, float(score)])
    return res


def parse_json_function(json_text):
    res = []
    data = eval(json_text)
    for _, func in data.items():
        funcs = split_text(func, splits, first=True)
        for key in funcs:
            res.append([key, 0.0])
    return res


def insert_model2cid(df_ori, cid, table="model_to_catalog"):
    df = df_ori[["id"]]
    df["cid"] = cid
    try:
        sql = f"DELETE FROM {table};"
        pd.read_sql(sql, con=engine)
    except Exception as e:
        # print(e)
        pass
    # print("Start insert model to catalogid")
    df.to_sql(table, con=engine, if_exists="append", index=False, dtype=None)


def insert_model2func(df, table_model2func="model_to_function", table_func="function"):
    sql = f"SELECT * FROM {table_func};"
    df_func = pd.read_sql(sql, con=engine)
    func2id = dict()
    for _, row in df_func.iterrows():
        func2id[row["name"]] = row["funcid"]

    values = []
    for _, row in df.iterrows():
        # funcs = split_text(row["function"], func2id.keys(), first=False)
        try:
            funcs = parse_json_tag(row["model_tag_ratings"])
        except Exception as e:
            # print(e)
            # print(_)
            # print(row)
            # exit()
            pass
        funcs_ = parse_json_target(row["model_target_ratings"])
        funcs.extend(funcs_)
        # funcs__ = parse_json_function(row["sku"])
        # funcs.extend(funcs__)
        if funcs is None:
            continue
        vis = set()
        for item in funcs:
            func, score = item
            # if "多功能" != func:
            #     func = func.replace("功能", "")
            # while func and "等" == func[-1]:
            #     func = func[:-1]
            # if not func:
            #     continue
            #
            # if "效果" != func:
            #     func = func.replace("效果", "")
            # func = func.replace("模式", "")
            # while func and "等" == func[-1]:
            #     func = func[:-1]
            # if not func:
            #     continue
            #
            # if len(func) > 5:
            #     print("long", func)

            if func in vis or "其他" in func:
                continue
            vis.add(func)

            try:
                values.append([row["id"], func2id[func], score])
            except KeyError:
                try:
                    # print(f"insert func name = {func}  id = {len(func2id)+1}")
                    sql = f"INSERT INTO {table_func}(name) VALUES ('{func}');"
                    pd.read_sql(sql, con=engine)
                except Exception as e:
                    pass
                func2id[func] = len(func2id) + 1
                values.append([row["id"], func2id[func], score])

    df_model2func = pd.DataFrame(values, columns=["id", "funcid", "score"])
    # print("Start insert model_to_function", len(values))
    try:
        sql = f"DELETE FROM {table_model2func};"
        pd.read_sql(sql, con=engine)
    except Exception as e:
        pass
    df_model2func.to_sql(table_model2func, con=engine, if_exists="append", index=False, dtype=None)


def insert_standard_properties(df, table="model"):
    del df["sku"]
    del df["model_tag_ratings"]
    del df["model_target_ratings"]

    df["brand"] = df["brand"].replace("\\", "/")
    df = df.drop_duplicates(["model", "brand"])
    # print("Start insert model standard properties", len(df))

    try:
        sql = "DELETE FROM model_to_catalog;"
        pd.read_sql(sql, con=engine)
    except Exception as e:
        pass
    try:
        sql = f"DELETE FROM {table};"
        pd.read_sql(sql, con=engine)
    except Exception as e:
        pass
    df["price"] = df["price"].astype("float").fillna(0)
    df["total_sold_price"] = df["total_sold_price"].astype("float").fillna(0)
    df["model_ratings"] = df["model_ratings"].astype("float").fillna(0)
    df.to_sql(table, con=engine, if_exists="append", index=False, dtype=None)
    # # sql = f"ALTER TABLE {table} ADD CONSTRAINT PK_id PRIMARY KEY (id);"
    # try:
    #     pd.read_sql(sql, con=engine)
    # except Exception as e:
    #     pass


def insert_fixed_properties(df):
    cid = df["cid"].values[0]
    del df["cid"]
    del df["datamonth"]
    # del df["sku"]
    del df["submarket"]
    del df["tag_score"]
    del df["target_score"]
    del df["rate_ring_biz30day"]
    del df["rate_ring_total_sold_price"]
    del df["season_biz30day_raise"]
    del df["season_total_sold_price_raise"]
    del df["rate_year_biz30day"]
    del df["rate_year_total_sold_price"]
    del df["biz30day_increment"]
    del df["total_sold_price_increment"]
    # del df["model_tag_ratings"]
    del df["aver_model_ratings"]
    del df["aver_model_tag_ratings"]
    del df["aver_model_target_ratings"]
    del df["model_tag_rank"]
    del df["model_target_rank"]
    del df["top_model"]
    del df["top_tag"]
    del df["top_target"]
    del df["model_ratings_confidence"]
    del df["model_tag_ratings_confidence"]

    df = df.drop_duplicates(["brand", "model"])
    insert_standard_properties(copy.deepcopy(df))
    insert_model2cid(copy.deepcopy(df), cid)
    insert_model2func(df)
    # insert_id2style(df)
    # insert_id2searchword(df)


def insert_sales_by_month(pcid, cid, df):
    pass


def delete_data():
    tables = ["model_to_function", "model"]
    for table in tables:
        try:
            sql = f"DELETE FROM {table};"
            pd.read_sql(sql, con=engine)
        except Exception as e:
            pass

engine = get_mysql_engine(localhost, "graph")
splits = [",", ";", ".", "，", "；", "。", "、", " ", "/", "\\"]


def process_sku(pcid, cid, datamonth):
    df = get_model_data(pcid, cid, datamonth)
    delete_data()
    insert_fixed_properties(df)


if __name__ == '__main__':
    # pcid, cid = "4", "50012097"
    # pcid, cid, datamonth = "100", "2018101516", "201812"  # 美容仪
    # pcid, cid, datamonth = "100", "2018112610", "201909"  # "螺丝刀"
    pcid, cid, datamonth = "100", "2019091609", "201908"  # 智能门锁
    # pcid, cid, datamonth = "100", "2019090610", "201812"  # 投影仪
    df = get_model_data(pcid, cid, datamonth)
    delete_data()
    insert_fixed_properties(df)
