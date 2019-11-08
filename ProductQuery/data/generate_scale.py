# -*- coding: utf-8 -*-

"""
@Project  : kg_demo_movie
@File     : generate_scale.py
@Author   : Call偶围城
@Date     : 2019/11/7
@Time     : 3:04
@Software : PyCharm

@description : 生成数据
brand model
cid, cidname, id, brand, model, datamonth, price,biz30day, total_sold_price,
model_ratings, model_rank,
model_pos, model_neu, model_neg, model_total, model_rate, model_rate_rank

cid, cidname, id, brand, model, funcid, name,
target_ratings, target_rank,
target_pos, target_neu, target_neg, target_total, target_rate, target_rate_rank
cid，cidname，模型，品牌，target，竞争力得分，均价（缺失），销售量（缺失），销售额（缺失），好评率（缺失），好评总数（缺失），好评书数量（缺失）
{comment_id: itemid} {itemid: biz30day, totolsoldprice}
找到product_brain里target在tb_comment_nlp里的数据，groupbytarget，统计

target
cid, cidname, datamonth, relate_model_num, aver_price, biz30day, total_sold_price,
aver_target_ratings, aver_target_rank,
sum_target_pos, sum_target_neu, sum_target_neg, sum_target_total, sum_target_rate, sum_target_rate_rank
"""

import datetime
import warnings

from ProductQuery.data.DBparam import *
from ProductQuery.data.delete_all_data import process_delete_all_data
from ProductQuery.data.sku import process_sku
from ProductQuery.data.add_data import process_add_data


def get_comment_data(pcid, cid, datamonth):
    try:
        df = pd.read_csv(f"all_comment_pcid{pcid}cid{cid}.csv", encoding="utf_8_sig", index_col=0)
    except FileNotFoundError:
        sql = f"SELECT * FROM comment.review_analysis_pcid{pcid}_cid{cid}_model_reviews;"
        engine = get_pgsql_engine(Outer99, "report_dg")
        df = pd.read_sql(sql, con=engine)
        df = df.replace(np.nan, "")
        df.to_csv(f"all_comment_pcid{pcid}cid{cid}.csv", encoding="utf_8_sig")
    return df


def get_model_data(pcid, cid, datamonth):
    try:
        df = pd.read_csv(f"all_model_pcid{pcid}cid{cid}.csv", encoding="utf_8_sig", index_col=0)
    except FileNotFoundError:
        sql = f"SELECT * FROM product_brain.product_brain_pcid{pcid} WHERE cid = '{cid}';"
        engine = get_pgsql_engine(Outer99, "report_dg")
        df = pd.read_sql(sql, con=engine)
        del df["sku"]
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
        del df["model_tag_ratings"]
        del df["model_target_ratings"]
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
        del df["imageurl"]

        df = df.replace(np.nan, "")

        def func(df):
            total_biz, total_sold = 0, 0
            for _, row in df.iterrows():
                total_biz += row["biz30day"]
                total_sold += row["total_sold_price"]
            df["biz30day"] = total_biz
            df["total_sold_price"] = total_sold
            return df

        df = df.groupby(["brand", "model"]).apply(func)
        df = df[df["datamonth"] == "201908"]
        df.to_csv(f"all_model_pcid{pcid}cid{cid}.csv", encoding="utf_8_sig")
    return df


def get_data(pcid, cid, datamonth):
    # primary key: brand, model
    df_model = get_model_data(pcid, cid, datamonth)
    # no primary key
    df_comment = get_comment_data(pcid, cid, datamonth)

    return df_model, df_comment


def statFunc(df, prefix):
    pos, neu, neg = 0, 0, 0
    for _, row in df.iterrows():
        if 1 == int(row["grade"]):
            pos += int(row["frequency"])
        elif -1 == int(row["grade"]):
            neg += int(row["frequency"])
        else:
            neu += int(row["frequency"])
    total = pos + neu + neg
    try:
        rate = pos / total
    except ZeroDivisionError:
        rate = 0
    df[prefix + "pos"] = pos
    df[prefix + "neu"] = neu
    df[prefix + "neg"] = neg
    df[prefix + "total"] = total
    df[prefix + "rate"] = rate
    return df


def sortFunc(df, prefix):
    rank = 1
    for inx, _ in df.iterrows():
        df.at[inx, prefix + "rank"] = rank
        rank += 1
    return df


def make_brand_model_scale(pcid, cid, cidname, datamonth):
    df_model, df_comment = get_data(pcid, cid, datamonth)

    df_comment = df_comment.groupby(["brand", "model"]).apply(statFunc, "model_").drop_duplicates(["brand", "model"])
    df_comment = df_comment[["brand", "model", "model_pos", "model_neu", "model_neg", "model_total", "model_rate"]]
    df = pd.merge(df_model, df_comment, how="left", on=["brand", "model"])

    df["biz30day_rank"] = 0
    df = sortFunc(df.sort_values("biz30day", ascending=False), "biz30day_")
    df["total_sold_price_rank"] = 0
    df = sortFunc(df.sort_values("total_sold_price", ascending=False), "total_sold_price_")
    df["model_rate_rank"] = 0
    df = sortFunc(df.sort_values("model_rate", ascending=False), "model_rate_")

    df["cidname"] = cidname
    df = df[["cid", "cidname", "brand", "model", "datamonth", "price", "biz30day", "biz30day_rank", "total_sold_price", "total_sold_price_rank",
             "model_ratings", "model_rank", "model_pos", "model_neu", "model_neg", "model_total", "model_rate", "model_rate_rank"]]
    df.to_csv(f"scale_model_pcid{pcid}cid{cid}.csv", encoding=UTF8)


def make_brand_model_target_scale(pcid, cid, cidname, datamonth):
    df_model, df_comment = get_data(pcid, cid, datamonth)

    engine = get_mysql_engine(localhost, "graph")
    model_to_catalog = pd.read_sql(f"SELECT id FROM model_to_catalog WHERE cid = '{cid}';", con=engine)
    model = pd.read_sql("SELECT brand, model, id FROM model;", con=engine)
    model_to_function = pd.read_sql("SELECT id, funcid, score FROM model_to_function;", con=engine).rename(columns={"score": "target_ratings"})

    function = pd.read_sql("SELECT funcid, name FROM function;", con=engine)

    df = pd.merge(model_to_catalog, model, how="left", on=["id"])
    df = pd.merge(df, model_to_function, how="inner", on=["id"])
    df = pd.merge(df, function, how="left", on=["funcid"])
    df.to_csv("temp.csv", encoding=UTF8)

    df_target = df_comment.groupby(["brand", "model", "target"]).apply(statFunc, "target_").drop_duplicates(["brand", "model", "target"])
    df_target["name"] = df_target["target"]
    del df_target["tag"]
    del df_target["target"]
    df_tag = df_comment.groupby(["brand", "model", "tag"]).apply(statFunc, "target_").drop_duplicates(["brand", "model", "tag"])
    df_tag["name"] = df_tag["tag"]
    del df_tag["tag"]
    del df_tag["target"]
    df_attribute = pd.concat([df_target, df_tag]).drop_duplicates(["brand", "model", "name"])
    df_attribute = df_attribute[["brand", "model", "name", "target_pos", "target_neu", "target_neg", "target_total", "target_rate"]]

    df = pd.merge(df, df_attribute, how="left", on=["brand", "model", "name"])

    df["target_rank"] = 0
    df = df.sort_values("target_ratings", ascending=False).groupby(["name"]).apply(sortFunc, "target_")
    df["target_rate_rank"] = 0
    df = df.sort_values("target_rate", ascending=False).groupby(["name"]).apply(sortFunc, "target_rate_")

    df["cid"], df["cidname"] = cid, cidname
    df = df.rename(columns={"name": "target"})
    df = df[["cid", "cidname", "brand", "model", "funcid", "target",
             "target_ratings", "target_rank", "target_pos", "target_neu", "target_neg", "target_total", "target_rate", "target_rate_rank"]]
    df.to_csv(f"scale_comment_pcid{pcid}cid{cid}.csv", encoding=UTF8)


def merge_model_comment(pcid, cid):
    df_model = pd.read_csv(f"scale_model_pcid{pcid}cid{cid}.csv", encoding=UTF8, index_col=0)
    df_comment = pd.read_csv(f"scale_comment_pcid{pcid}cid{cid}.csv", encoding=UTF8, index_col=0)

    del df_comment["cid"]
    del df_comment["cidname"]

    df = pd.merge(df_model, df_comment, how="left", on=["brand", "model"])
    df.to_csv(f"scale_result_model_pcid{pcid}cid{cid}.csv", encoding=UTF8)


def statTargetFunc(df):
    sum_biz30day, sum_total_sold_price = 0, 0
    sum_target_pos, sum_target_neu, sum_target_neg, sum_target_total = 0, 0, 0, 0
    sum_target_ratings = 0
    for _, row in df.iterrows():
        sum_biz30day += row["biz30day"]
        sum_total_sold_price += row["total_sold_price"]
        sum_target_pos += row["target_pos"]
        sum_target_neu += row["target_neu"]
        sum_target_neg += row["target_neg"]
        sum_target_total += row["target_total"]
        sum_target_ratings += row["target_ratings"] * row["biz30day"]

    try:
        sum_avg_price = sum_total_sold_price / sum_biz30day
    except ZeroDivisionError:
        sum_avg_price = 0
    try:
        sum_rate = sum_target_pos / sum_target_total
    except ZeroDivisionError:
        sum_rate = 0
    try:
        sum_target_ratings = sum_target_ratings / sum_biz30day
    except ZeroDivisionError:
        sum_target_ratings = 0

    df["sum_avg_price"] = sum_avg_price
    df["sum_biz30day"] = sum_biz30day
    df["sum_total_sold_price"] = sum_total_sold_price
    df["sum_target_pos"] = sum_target_pos
    df["sum_target_neu"] = sum_target_neu
    df["sum_target_neg"] = sum_target_neg
    df["sum_target_total"] = sum_target_total
    df["sum_rate"] = sum_rate
    df["sum_target_ratings"] = sum_target_ratings

    return df


def make_target_scale(pcid, cid, cidname, datamonth):
    df = pd.read_csv(f"scale_result_model_pcid{pcid}cid{cid}.csv", encoding=UTF8, index_col=0)
    del df["brand"]
    del df["model"]
    del df["price"]
    del df["biz30day_rank"]
    del df["total_sold_price_rank"]
    del df["model_ratings"]
    del df["model_rank"]
    del df["model_pos"]
    del df["model_neu"]
    del df["model_neg"]
    del df["model_total"]
    del df["model_rate"]
    del df["model_rate_rank"]

    df = df.groupby(["target"]).apply(statTargetFunc)
    del df["target_rank"]
    del df["biz30day"]
    del df["total_sold_price"]
    del df["target_pos"]
    del df["target_neu"]
    del df["target_neg"]
    del df["target_total"]
    del df["target_rate"]
    del df["target_rate_rank"]

    df = df.drop_duplicates(["target"])

    df["sum_biz30day_rank"] = 0
    df = sortFunc(df.sort_values("sum_biz30day", ascending=False), "sum_biz30day_")
    df["sum_total_sold_price_rank"] = 0
    df = sortFunc(df.sort_values("sum_total_sold_price", ascending=False), "sum_total_sold_price_")
    df["sum_target_rank"] = 0
    df = sortFunc(df.sort_values("sum_target_ratings", ascending=False), "sum_target_")
    df["sum_rate_rank"] = 0
    df = sortFunc(df.sort_values("sum_rate", ascending=False), "sum_rate_")

    df = df[["cid", "cidname", "datamonth", "funcid", "target", "sum_avg_price",
             "sum_biz30day", "sum_biz30day_rank", "sum_total_sold_price", "sum_total_sold_price_rank",
             "sum_target_ratings", "sum_target_rank",
             "sum_target_pos", "sum_target_neu", "sum_target_neg", "sum_target_total", "sum_rate", "sum_rate_rank"]]
    df.to_csv(f"scale_result_target_pcid{pcid}cid{cid}.csv", encoding=UTF8)


if __name__ == '__main__':
    try:
        warnings.filterwarnings("ignore")
        tasks = list()
        tasks.append(("100", "2018101516", "电子美容仪", "201812"))
        tasks.append(("100", "2018112610", "螺丝刀", "201909"))
        tasks.append(("100", "2018112614", "家用工具组套", "201909"))
        tasks.append(("100", "2019070912", "果冻/布丁", "201906"))
        tasks.append(("100", "2019090610", "投影仪", "201908"))
        # tasks.append(("100", "2019091609", "智能门锁", "201908"))
        tasks.append(("7", "50006219", "电钻", "201909"))
        tasks.append(("7", "50008950", "测距仪", "201909"))
        for task in tasks:
            try:
                start = datetime.datetime.now()
                print(start)
                print("start task:", task)
                pcid, cid, cidname, datamonth = task

                process_delete_all_data()
                try:
                    process_sku(pcid, cid, datamonth)
                except Exception as e:
                    pass
                process_sku(pcid, cid, datamonth)
                process_add_data()

                make_brand_model_scale(pcid, cid, cidname, datamonth)
                make_brand_model_target_scale(pcid, cid, cidname, datamonth)
                merge_model_comment(pcid, cid)
                make_target_scale(pcid, cid, cidname, datamonth)
            except Exception as e:
                raise e
            finally:
                end = datetime.datetime.now()
                print(end)
                print("end task:", task)
                print("cost:", end-start)
                print("=====================================\n")
    except Exception as e:
        pass
    finally:
        warnings.filterwarnings("default")
