# -*- coding: utf-8 -*-

from ProductQuery.data.DBparam import *


def delete_model_to_function(table="model_to_function"):
    engine = get_mysql_engine(localhost, "graph")
    try:
        sql = f"DELETE FROM {table};"
        pd.read_sql(sql, con=engine)
    except Exception as e:
        pass


def delete_model(table="model"):
    engine = get_mysql_engine(localhost, "graph")
    try:
        sql = f"DELETE FROM {table};"
        pd.read_sql(sql, con=engine)
    except Exception as e:
        pass


def delete_function(table="function"):
    engine = get_mysql_engine(localhost, "graph")
    try:
        sql = f"DELETE FROM {table};"
        pd.read_sql(sql, con=engine)
    except Exception as e:
        pass


if __name__ == '__main__':
    delete_model_to_function()
    delete_model()
    delete_function()