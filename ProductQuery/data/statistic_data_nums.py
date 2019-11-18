# -*- coding: utf-8 -*-

"""
@Project  : kg_demo_movie
@File     : statistic_data_nums.py.py
@Author   : Call偶围城
@Date     : 2019/11/13
@Time     : 13:15
@Software : PyCharm

@description : 统计各行业评价、商品、型号、属性数量
"""

import pandas as pd

from ProductQuery.data.DBparam import *


def get_comment_nums(pcid, cid):
    table = f"raw_comment_pcid{pcid}.raw_tb_comment{cid}"
    sql = f"SELECT COUNT(*) FROM {table};"
    engine = get_pgsql_engine(Outer99, "raw_tb_comment_notag")
    try:
        nums1 = pd.read_sql(sql, con=engine)["count"].values[0]
    except Exception as e:
        nums1 = 0

    if "100" != pcid:
        table = f"pcid{pcid}.raw_tb_comment{cid}"
        sql = f"SELECT COUNT(*) FROM {table};"
        engine = get_pgsql_engine(DBTencentComment, "raw_taobao_comment")
        try:
            nums2 = pd.read_sql(sql, con=engine)["count"].values[0]
        except Exception as e:
            raise e
    else:
        nums2 = 0
    print("评价数量")
    print(f"115服务器：{nums1}   tencent服务器：{nums2}")
    return max([nums1, nums2])


def get_item_nums(pcid, cid):
    table = f"raw_comment_pcid{pcid}.raw_tb_comment{cid}"
    sql = f"SELECT COUNT(*) FROM (SELECT DISTINCT itemid FROM {table}) as itemids;"
    engine = get_pgsql_engine(Outer99, "raw_tb_comment_notag")
    try:
        nums1 = pd.read_sql(sql, con=engine)["count"].values[0]
    except Exception as e:
        nums1 = 0

    if "100" != pcid:
        table = f"pcid{pcid}.raw_tb_comment{cid}"
        sql = f"SELECT COUNT(*) FROM (SELECT DISTINCT itemid FROM {table}) as itemids;"
        engine = get_pgsql_engine(DBTencentComment, "raw_taobao_comment")
        try:
            nums2 = pd.read_sql(sql, con=engine)["count"].values[0]
        except Exception as e:
            raise e
    else:
        nums2 = 0

    table = f"fact_item_pcid{pcid}.cid{cid}"
    sql = f"SELECT COUNT(*) FROM (SELECT DISTINCT itemid FROM {table}) as itemids;"
    engine = get_pgsql_engine(Outer99, "fact_library")
    try:
        nums3 = pd.read_sql(sql, con=engine)["count"].values[0]
    except Exception as e:
        nums3 = 0
    print("item数量")
    print(f"115服务器：{nums1}   tencent服务器：{nums2}   fact_library:{nums3}")
    return max([nums1, nums2, nums3])


def get_model_nums(pcid, cid):
    table = f"fact_model_pcid{pcid}.cid{cid}"
    sql = f"SELECT COUNT(*) FROM (SELECT DISTINCT brand, model FROM {table}) as models;"
    engine = get_pgsql_engine(Outer99, "fact_library")
    try:
        nums1 = pd.read_sql(sql, con=engine)["count"].values[0]
    except Exception as e:
        nums1 = 0
    print("model数量")
    print(f"fact_library：{nums1}")
    return max([nums1])


def get_attribute_nums(pcid, cid):
    table = f"pcid{pcid}.review_analysis_{cid}"
    sql = f"SELECT COUNT(*) FROM (SELECT DISTINCT target FROM {table}) as targets;"
    engine = get_pgsql_engine(DB115, "tb_comment_nlp")
    try:
        nums1 = pd.read_sql(sql, con=engine)["count"].values[0]
    except Exception as e:
        nums1 = 0
    print("model数量")
    print(f"tb_comment_nlp：{nums1}")
    return max([nums1])


def run(task):
    pcid, cid, cidname, _ = task
    comment_nums = get_comment_nums(pcid, cid)
    item_nums = get_item_nums(pcid, cid)
    model_nums = get_model_nums(pcid, cid)
    attribute_nums = get_attribute_nums(pcid, cid)
    return [cid, cidname, comment_nums, item_nums, model_nums, attribute_nums]


if __name__ == '__main__':
    tasks = list()
    tasks.append(("100", "2018101516", "电子美容仪", "201812"))
    tasks.append(("100", "2018112610", "螺丝刀", "201909"))
    tasks.append(("100", "2018112614", "家用工具组套", "201909"))
    tasks.append(("100", "2019070912", "果冻/布丁", "201906"))
    tasks.append(("100", "2019090610", "投影仪", "201908"))
    tasks.append(("100", "2019091609", "智能门锁", "201908"))
    tasks.append(("7", "50006219", "电钻", "201909"))
    tasks.append(("5", "121484013", "眼霜", "201909"))
    tasks.append(("6", "50016098", "维生素E", "201909"))
    tasks.append(("4", "50012097", "料理机", "201909"))
    tasks.append(("4", "50013008", "电饭煲", "201909"))
    tasks.append(("7", "50008950", "测距仪", "201909"))

    results = list()
    for task in tasks:
        print("task start:", task)
        result = run(task)
        print("result:", result)
        results.append(result)
    df = pd.DataFrame(results, columns=[
        "cid", "cidname", "comments", "items", "models", "attributes"])
    df.to_csv("statistic.csv", encoding=UTF8)
