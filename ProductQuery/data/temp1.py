# -*- coding: utf-8 -*-

"""
@Project  : kg_demo_movie
@File     : temp.py
@Author   : Call偶围城
@Date     : 2019/11/6
@Time     : 23:05
@Software : PyCharm

@description : 拷贝2019070912_cut_new中comment_all like '热量%高%'的记录
"""

from ProductQuery.data.DBparam import *


def copy_data(pcid, cid):
    engine = get_pgsql_engine(DB114, "tb_comment_words")
    sql = f"SELECT * FROM raw_comment_pcid{pcid}.raw_tb_comment{cid}_cut_new WHERE comment_all like '%%热量%%高%%';"
    print(sql)
    df = pd.read_sql(sql, con=engine)
    # df.to_csv("temp.csv", encoding=UTF8)
    df.to_sql(f"raw_tb_comment{cid}_cut_new_Gao", schema=f"raw_comment_pcid{pcid}", con=engine, if_exists="append", index=False, dtype=None)


if __name__ == '__main__':
    pcid, cid = "100", "2019070912"
    copy_data(pcid, cid)
