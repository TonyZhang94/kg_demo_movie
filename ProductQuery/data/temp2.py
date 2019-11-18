# -*- coding: utf-8 -*-

"""
@Project  : kg_demo_movie
@File     : temp2.py
@Author   : Call偶围城
@Date     : 2019/11/13
@Time     : 14:50
@Software : PyCharm

@description : 查看历史处理的pcid4cid50012097有多少target
"""


def run(task):
    pcid, cid = task
    words = set()
    file = f"D:\KG for movie\kg_demo_movie\ProductQuery\data\\temp_pcid{pcid}cid{cid}.txt"
    with open(file, mode="r", encoding="utf-8") as fp:
        for line in fp.readlines():
            word = line.strip()
            words.add(word)
    print(task, "words", len(words))


if __name__ == '__main__':
    tasks = list()
    tasks.append(("100", "2018101516"))
    tasks.append(("4", "50012097"))
    for task in tasks:
        run(task)
