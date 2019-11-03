# -*- coding: utf-8 -*-

from ProductQuery.data.DBparam import *


def save_vocab(tasks):
    engine = get_mysql_engine(localhost, "graph")
    base = "SELECT DISTINCT {column} FROM {table};"
    for task in tasks:
        table, column, file, tag = task
        sql = base.format(column=column, table=table)
        values = pd.read_sql(sql, con=engine)[column].values
        with open(f"../vocab/{file}.txt", mode="w", encoding="utf-8") as fp:
            for value in values:
                fp.write(f"{value} {tag}\n")


if __name__ == '__main__':
    tasks = []
    tasks.append(("model", "brand", "vocab_brand_nbr", "nbr"))
    tasks.append(("model", "model", "vocab_model_nmo", "nmo"))
    tasks.append(("function", "name", "vocab_function_nfu", "nfu"))
    save_vocab(tasks)
