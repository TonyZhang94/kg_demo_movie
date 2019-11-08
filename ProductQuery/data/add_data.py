# -*- coding: utf-8 -*-

from ProductQuery.data.DBparam import *


engine = get_mysql_engine(localhost, "graph")


def add_function(task):
    funcid, name = task

    table = "function"
    columns = ["funcid", "name"]
    data = [[funcid, name]]
    df = pd.DataFrame(data, columns=columns)
    df.to_sql(table, con=engine, if_exists="append", index=False, dtype=None)


def add(task):
    pcid, cid, funcid, name, score, brand, model, price, biz30day, total_sold_price, model_ratings, model_rank, imageurl, id = task
    table = "model"
    columns = ["brand", "model", "price", "biz30day", "total_sold_price", "model_ratings", "model_rank", "imageurl", "id"]
    data = [[brand, model, price, biz30day, total_sold_price, model_ratings, model_rank, imageurl, id]]
    df = pd.DataFrame(data, columns=columns)
    df.to_sql(table, con=engine, if_exists="append", index=False, dtype=None)

    table = "model_to_catalog"
    columns = ["id", "cid"]
    data = [[id, cid]]
    df = pd.DataFrame(data, columns=columns)
    df.to_sql(table, con=engine, if_exists="append", index=False, dtype=None)

    table = "model_to_function"
    columns = ["id", "funcid", "score"]
    data = [[id, funcid, score]]
    df = pd.DataFrame(data, columns=columns)
    df.to_sql(table, con=engine, if_exists="append", index=False, dtype=None)


def process_add_data():
    funcid = 1274

    params = [funcid, "去鱼尾纹"]
    add_function(params)

    tasks = list()
    # url: https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.7.45e811b1xbxz25&id=596564902117&skuId=4144875748103&areaId=330100&user_id=2842320334&cat_id=2&is_b=1&rn=482771adb4b72e697e9d660204516e29
    tasks.append(
        ["100", "2018101516", funcid, "去鱼尾纹", 93.87, "Marco pele/玛可蓓莉", "MP1016p", 139, 174, 139 * 174, 95.14, 49,
         "https://img.alicdn.com/imgextra/https://img.alicdn.com/imgextra/i3/2842320334/O1CN01YcHTnQ1EL0p3eaWTM_!!2842320334.jpg_430x430q90.jpg",
         677777])
    # url: https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.6.8efc70146et71u&id=553045647118&skuId=3831989592474&areaId=330100&user_id=1031543550&cat_id=2&is_b=1&rn=c889b41eee8d8a4c057bf237d90cda92
    tasks.append(
        ["5", "121484013", funcid, "去鱼尾纹", 97.61, "ELABEST/雅莱贝斯", "黄金多肽眼部精华", 167, 2672, 167 * 2672, 94.81, 124,
         "https://img.alicdn.com/imgextra/https://img.alicdn.com/imgextra/i2/1031543550/O1CN01oSWVLe1c5wbMNzvyP_!!1031543550.jpg_430x430q90.jpg",
         677778])  # 5443个产品
    # https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.11.6228404drOKtKr&id=521261585415&areaId=330100&standard=1&user_id=877603842&cat_id=2&is_b=1&rn=baac031a5d7ad5f2c3b0d6b4069c46ea
    tasks.append(["6", "50016098", funcid, "去鱼尾纹", 87.79, "汤臣倍健", "天然维生素E软胶囊", 115, 2029, 115 * 2029, 89.92, 78,
                  "https://img.alicdn.com/imgextra/https://img.alicdn.com/imgextra/i3/877603842/O1CN01OyQcZ91eFgCHpgGca_!!877603842.jpg_430x430q90.jpg",
                  677779])  # 1074
    for task in tasks:
        add(task)


if __name__ == '__main__':
    funcid = 1274

    params = [funcid, "去鱼尾纹"]
    add_function(params)

    tasks = list()
    # url: https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.7.45e811b1xbxz25&id=596564902117&skuId=4144875748103&areaId=330100&user_id=2842320334&cat_id=2&is_b=1&rn=482771adb4b72e697e9d660204516e29
    tasks.append(["100", "2018101516", funcid, "去鱼尾纹", 93.87, "Marco pele/玛可蓓莉", "MP1016p", 139, 174, 139*174, 95.14, 49,
                  "https://img.alicdn.com/imgextra/https://img.alicdn.com/imgextra/i3/2842320334/O1CN01YcHTnQ1EL0p3eaWTM_!!2842320334.jpg_430x430q90.jpg", 677777])
    # url: https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.6.8efc70146et71u&id=553045647118&skuId=3831989592474&areaId=330100&user_id=1031543550&cat_id=2&is_b=1&rn=c889b41eee8d8a4c057bf237d90cda92
    tasks.append(["5", "121484013", funcid, "去鱼尾纹", 97.61, "ELABEST/雅莱贝斯", "黄金多肽眼部精华", 167, 2672, 167*2672, 94.81, 124,
                  "https://img.alicdn.com/imgextra/https://img.alicdn.com/imgextra/i2/1031543550/O1CN01oSWVLe1c5wbMNzvyP_!!1031543550.jpg_430x430q90.jpg", 677778])  # 5443个产品
    # https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.11.6228404drOKtKr&id=521261585415&areaId=330100&standard=1&user_id=877603842&cat_id=2&is_b=1&rn=baac031a5d7ad5f2c3b0d6b4069c46ea
    tasks.append(["6", "50016098", funcid, "去鱼尾纹", 87.79, "汤臣倍健", "天然维生素E软胶囊", 115, 2029, 115*2029, 89.92, 78,
                  "https://img.alicdn.com/imgextra/https://img.alicdn.com/imgextra/i3/877603842/O1CN01OyQcZ91eFgCHpgGca_!!877603842.jpg_430x430q90.jpg", 677779])  # 1074
    for task in tasks:
        add(task)
