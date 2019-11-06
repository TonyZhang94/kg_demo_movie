# -*- coding:utf-8 -*-

import sqlalchemy as sa
import pandas as pd
import numpy as np


dynamic_ip = "125.120.146.49"


class DB99(object):
    host = "192.168.1.99"
    port = 5433
    user = "zczx_write"
    password = "zczxTech2012"

    DB = dict()
    DB["standard_library"] = "standard_library"
    DB["fact_library"] = "fact_library"
    DB["zhuican_web"] = "zhuican_web"
    DB["raw_mj_category"] = "raw_mj_category"
    DB["report_dg"] = "report_dg"
    DB["raw_tb_comment_notag"] = "raw_tb_comment_notag"
    DB["tb_comment_nlp"] = "tb_comment_nlp"
    DB["lexicon"] = "lexicon"
    DB["tb_comment_words"] = "tb_comment_words"
    DB["chu"] = "chu"


class Outer99(object):
    host = dynamic_ip
    port = 28944  # 5432 28943 5433 28944
    user = "zczx_write"
    password = "zczx112211"

    DB = dict()
    DB["standard_library"] = "standard_library"
    DB["fact_library"] = "fact_library"
    DB["zhuican_web"] = "zhuican_web"
    DB["raw_mj_category"] = "raw_mj_category"
    DB["report_dg"] = "report_dg"
    DB["raw_tb_comment_notag"] = "raw_tb_comment_notag"
    DB["tb_comment_nlp"] = "tb_comment_nlp"
    DB["lexicon"] = "lexicon"
    DB["tb_comment_words"] = "tb_comment_words"
    DB["chu"] = "chu"


class Tencent(object):
    host = "postgres-lkr70ecv.gz.cdb.myqcloud.com"
    port = 62
    user = "zczx_admin"
    password = "zczx112211"

    DB = dict()
    DB["standard_library"] = "standard_library"
    DB["fact_library"] = "fact_library"
    DB["zhuican_web"] = "zhuican_web"
    DB["raw_mj_category"] = "raw_mj_category"
    DB["report_dg"] = "report_dg"
    DB["raw_tb_comment_notag"] = "raw_tb_comment_notag"
    DB["tb_comment_nlp"] = "tb_comment_nlp"
    DB["lexicon"] = "lexicon"
    DB["tb_comment_words"] = "tb_comment_words"
    DB["chu"] = "chu"


class DB114(object):
    host = dynamic_ip
    port = 28946
    user = "zczx_write"
    password = "zczxTech2012"

    DB = dict()
    DB["tb_comment_words"] = "tb_comment_words"


class DBTencentComment(object):
    host = "postgres-jq4zka6d.sql.tencentcdb.com"
    port = 25876
    user = "zczx_admin"
    password = "zczx112211"

    DB = dict()
    DB["raw_taobao_comment"] = "raw_taobao_comment"


class localhost(object):
    host = "localhost"
    port = 3306
    user = "root"
    password = ""

    DB = dict()
    DB["graph"] = "graph"


UTF8 = "utf_8_sig"


def get_pgsql_engine(info, db):
    conn = sa.create_engine("postgresql://{USER}:{PASS}@{HOST}:{PORT}/{DB}".
                            format(USER=info.user,
                                   PASS=info.password,
                                   HOST=info.host,
                                   PORT=info.port,
                                   DB=info.DB[db]))
    return conn


def get_mysql_engine(info, db):
    conn = sa.create_engine("mysql://{USER}@{HOST}:{PORT}/{DB}?charset=utf8".
                            format(USER=info.user,
                                   HOST=info.host,
                                   PORT=info.port,
                                   DB=info.DB[db]))
    return conn
