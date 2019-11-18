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

    funcid = 1275
    params = [funcid, "煲鸡汤"]
    add_function(params)

    funcid = 1276
    params = [funcid, "煲汤"]
    add_function(params)

    funcid = 1277
    params = [funcid, "复古红"]
    add_function(params)

    funcid = 1278
    params = [funcid, "粉红"]
    add_function(params)

    funcid = 1279
    params = [funcid, "至尊红"]
    add_function(params)

    funcid = 1280
    params = [funcid, "萌化粉"]
    add_function(params)

    funcid = 1281
    params = [funcid, "中国红"]
    add_function(params)

    funcid = 1282
    params = [funcid, "红色"]
    add_function(params)

    tasks = list()
    # url: https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.7.45e811b1xbxz25&id=596564902117&skuId=4144875748103&areaId=330100&user_id=2842320334&cat_id=2&is_b=1&rn=482771adb4b72e697e9d660204516e29
    tasks.append(
        ["100", "2018101516", 1274, "去鱼尾纹", 93.87, "Marco pele/玛可蓓莉", "MP1016p", 139, 174, 139 * 174, 95.14, 49,
         "https://img.alicdn.com/imgextra/https://img.alicdn.com/imgextra/i3/2842320334/O1CN01YcHTnQ1EL0p3eaWTM_!!2842320334.jpg_430x430q90.jpg",
         677777])
    # url: https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.6.8efc70146et71u&id=553045647118&skuId=3831989592474&areaId=330100&user_id=1031543550&cat_id=2&is_b=1&rn=c889b41eee8d8a4c057bf237d90cda92
    tasks.append(
        ["5", "121484013", 1274, "去鱼尾纹", 97.61, "ELABEST/雅莱贝斯", "黄金多肽眼部精华", 167, 2672, 167 * 2672, 94.81, 124,
         "https://img.alicdn.com/imgextra/https://img.alicdn.com/imgextra/i2/1031543550/O1CN01oSWVLe1c5wbMNzvyP_!!1031543550.jpg_430x430q90.jpg",
         677778])  # 5443个产品
    # url: https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.11.6228404drOKtKr&id=521261585415&areaId=330100&standard=1&user_id=877603842&cat_id=2&is_b=1&rn=baac031a5d7ad5f2c3b0d6b4069c46ea
    tasks.append(["6", "50016098", 1274, "去鱼尾纹", 87.79, "汤臣倍健", "天然维生素E软胶囊", 115, 2029, 115 * 2029, 89.92, 78,
                  "https://img.alicdn.com/imgextra/https://img.alicdn.com/imgextra/i3/877603842/O1CN01OyQcZ91eFgCHpgGca_!!877603842.jpg_430x430q90.jpg",
                  677779])  # 1074个产品
    # url: https://detail.tmall.com/item.htm?id=567938974847&ali_refid=a3_430673_1006:1121404410:N:CPc3q7JwIsvAP4gQJZdOyQ==:738166b7fd5baa1dca5e7ea2769b1575&ali_trackid=1_738166b7fd5baa1dca5e7ea2769b1575&spm=a2e15.8261149.07626516002.2&skuId=3624144617390
    tasks.append(["4", "50013008", 1275, "煲鸡汤", 87.79, "SUPOR/苏泊尔", "SY-50YC5210EQ", 379, 20000, 379 * 20000, 96.98, 21,
                  "https://img.alicdn.com/bao/uploaded/i2/TB1HDwzdF67gK0jSZPfSuuhhFXa.jpg_600x600.jpg",
                  677780])  # 3822个产品
    # url: https://detail.tmall.com/item.htm?id=571796299182&ali_refid=a3_430673_1006:1152695386:N:KT0+otDGCXB8uU89EnsiMg==:c87a832f17af44a5a2968b65fb752c47&ali_trackid=1_c87a832f17af44a5a2968b65fb752c47&spm=a2e15.8261149.07626516002.1
    tasks.append(
        ["4", "50012097", 1277, "复古红", 94.19, "BRUNO", "BOE021", 1199, 25000, 1199 * 25000, 96.11, 6,
         "https://img.alicdn.com/imgextra/https://img.alicdn.com/imgextra/i1/3979625482/O1CN01qnVCew1qMnnuKRNgB_!!3979625482.jpg_430x430q90.jpg",
         677781])
    # url: https://item.taobao.com/item.htm?id=605507147935&ali_refid=a3_430673_1006:1110456505:N:KT0%2BotDGCXB8uU89EnsiMg%3D%3D:b36efe1cc81430b6e014d2c6bfb428bf&ali_trackid=1_b36efe1cc81430b6e014d2c6bfb428bf&spm=a2e15.8261149.07626516002.6
    tasks.append(
        ["4", "50012097", 1278, "粉红", 71.65, "mokkom", "MK-240A", 299, 24, 299 * 24, 73.36, 197,
         "https://img.alicdn.com/imgextra/i1/1731331726/O1CN01lR4yPz1OcYAgRz6Eu_!!1731331726.jpg_400x400.jpg",
         677782])
    # url: https://detail.tmall.com/item.htm?id=561273561723&ali_refid=a3_430673_1006:1105231527:N:KT0+otDGCXB8uU89EnsiMg==:a7a37753f3d43217f04badf38ec2247d&ali_trackid=1_a7a37753f3d43217f04badf38ec2247d&spm=a2e15.8261149.07626516002.17
    tasks.append(
        ["4", "50012097", 1279, "至尊红", 92.85, "HATTIECS/海蒂诗", "769S", 349, 10000, 349 * 10000, 94.91, 27,
         "https://img.alicdn.com/imgextra/i4/1583725153/TB2.s6IjAfb_uJjSsrbXXb6bVXa_!!1583725153.jpg_430x430q90.jpg",
         677783])
    # url: https://detail.tmall.com/item.htm?id=602096306654&ali_refid=a3_430673_1006:1154900004:N:KT0+otDGCXB8uU89EnsiMg==:8481c4be19a034c1d778e2f6fab84bc8&ali_trackid=1_8481c4be19a034c1d778e2f6fab84bc8&spm=a2e15.8261149.07626516002.10
    tasks.append(
        ["4", "50012097", 1280, "至尊红", 92.85, "Howaryou/好阿优", "HAY-807", 79.00, 20000, 79.00 * 20000, 92.97, 75,
         "https://img.alicdn.com/imgextra/i4/4035922652/O1CN01XKH8a31VSevHPcxOc_!!4035922652.png_430x430q90.jpg",
         677784])
    # url: https://item.taobao.com/item.htm?id=564681440422&ali_refid=a3_430673_1006:1106434920:N:KT0%2BotDGCXB8uU89EnsiMg%3D%3D:a9ecacbd3ed01448691026694b9fbc92&ali_trackid=1_a9ecacbd3ed01448691026694b9fbc92&spm=a2e15.8261149.07626516002.25
    tasks.append(
        ["4", "50012097", 1281, "中国红", 89.55, "MIUI", "JE-B02C", 388.00, 952, 388.00 * 952, 90.20, 112,
         "https://gd4.alicdn.com/imgextra/i1/346352241/O1CN01Mxb0h81SQQ9hVnhQZ_!!346352241.jpg_400x400.jpg",
         677785])
    for task in tasks:
        add(task)


if __name__ == '__main__':
    # funcid = 1274
    # params = [funcid, "去鱼尾纹"]
    # add_function(params)

    # funcid = 1275
    # params = [funcid, "煲鸡汤"]
    # add_function(params)

    # funcid = 1276
    # params = [funcid, "煲汤"]
    # add_function(params)
    #
    # funcid = 1277
    # params = [funcid, "复古红"]
    # add_function(params)
    #
    # funcid = 1278
    # params = [funcid, "粉红"]
    # add_function(params)
    #
    # funcid = 1279
    # params = [funcid, "至尊红"]
    # add_function(params)
    #
    # funcid = 1280
    # params = [funcid, "萌化粉"]
    # add_function(params)
    #
    # funcid = 1281
    # params = [funcid, "中国红"]
    # add_function(params)

    funcid = 1282
    params = [funcid, "红色"]
    add_function(params)

    tasks = list()
    # url: https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.7.45e811b1xbxz25&id=596564902117&skuId=4144875748103&areaId=330100&user_id=2842320334&cat_id=2&is_b=1&rn=482771adb4b72e697e9d660204516e29
    # tasks.append(
    #     ["100", "2018101516", 1274, "去鱼尾纹", 93.87, "Marco pele/玛可蓓莉", "MP1016p", 139, 174, 139 * 174, 95.14, 49,
    #      "https://img.alicdn.com/imgextra/https://img.alicdn.com/imgextra/i3/2842320334/O1CN01YcHTnQ1EL0p3eaWTM_!!2842320334.jpg_430x430q90.jpg",
    #      677777])
    # url: https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.6.8efc70146et71u&id=553045647118&skuId=3831989592474&areaId=330100&user_id=1031543550&cat_id=2&is_b=1&rn=c889b41eee8d8a4c057bf237d90cda92
    # tasks.append(
    #     ["5", "121484013", 1274, "去鱼尾纹", 97.61, "ELABEST/雅莱贝斯", "黄金多肽眼部精华", 167, 2672, 167 * 2672, 94.81, 124,
    #      "https://img.alicdn.com/imgextra/https://img.alicdn.com/imgextra/i2/1031543550/O1CN01oSWVLe1c5wbMNzvyP_!!1031543550.jpg_430x430q90.jpg",
    #      677778])  # 5443个产品
    # https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.11.6228404drOKtKr&id=521261585415&areaId=330100&standard=1&user_id=877603842&cat_id=2&is_b=1&rn=baac031a5d7ad5f2c3b0d6b4069c46ea
    # tasks.append(["6", "50016098", 1274, "去鱼尾纹", 87.79, "汤臣倍健", "天然维生素E软胶囊", 115, 2029, 115 * 2029, 89.92, 78,
    #               "https://img.alicdn.com/imgextra/https://img.alicdn.com/imgextra/i3/877603842/O1CN01OyQcZ91eFgCHpgGca_!!877603842.jpg_430x430q90.jpg",
    #               677779])  # 1074个产品
    # url: https://detail.tmall.com/item.htm?id=567938974847&ali_refid=a3_430673_1006:1121404410:N:CPc3q7JwIsvAP4gQJZdOyQ==:738166b7fd5baa1dca5e7ea2769b1575&ali_trackid=1_738166b7fd5baa1dca5e7ea2769b1575&spm=a2e15.8261149.07626516002.2&skuId=3624144617390
    # tasks.append(
    #     ["4", "50013008", 1275, "煲鸡汤", 87.79, "SUPOR/苏泊尔", "SY-50YC5210EQ", 379, 20000, 379 * 20000, 96.98, 21,
    #      "https://img.alicdn.com/bao/uploaded/i2/TB1HDwzdF67gK0jSZPfSuuhhFXa.jpg_600x600.jpg",
    #      677780])  # 3822个产品
    # url: https://detail.tmall.com/item.htm?id=571796299182&ali_refid=a3_430673_1006:1152695386:N:KT0+otDGCXB8uU89EnsiMg==:c87a832f17af44a5a2968b65fb752c47&ali_trackid=1_c87a832f17af44a5a2968b65fb752c47&spm=a2e15.8261149.07626516002.1
    # tasks.append(
    #     ["4", "50012097", 1277, "复古红", 94.19, "BRUNO", "BOE021", 1199, 25000, 1199 * 25000, 96.11, 6,
    #      "https://img.alicdn.com/imgextra/https://img.alicdn.com/imgextra/i1/3979625482/O1CN01qnVCew1qMnnuKRNgB_!!3979625482.jpg_430x430q90.jpg",
    #      677781])
    # url: https://item.taobao.com/item.htm?id=605507147935&ali_refid=a3_430673_1006:1110456505:N:KT0%2BotDGCXB8uU89EnsiMg%3D%3D:b36efe1cc81430b6e014d2c6bfb428bf&ali_trackid=1_b36efe1cc81430b6e014d2c6bfb428bf&spm=a2e15.8261149.07626516002.6
    # tasks.append(
    #     ["4", "50012097", 1278, "粉红", 71.65, "mokkom", "MK-240A", 299, 24, 299 * 24, 73.36, 197,
    #      "https://img.alicdn.com/imgextra/i1/1731331726/O1CN01lR4yPz1OcYAgRz6Eu_!!1731331726.jpg_400x400.jpg",
    #      677782])
    # url: https://detail.tmall.com/item.htm?id=561273561723&ali_refid=a3_430673_1006:1105231527:N:KT0+otDGCXB8uU89EnsiMg==:a7a37753f3d43217f04badf38ec2247d&ali_trackid=1_a7a37753f3d43217f04badf38ec2247d&spm=a2e15.8261149.07626516002.17
    # tasks.append(
    #     ["4", "50012097", 1279, "至尊红", 92.85, "HATTIECS/海蒂诗", "769S", 349, 10000, 349 * 10000, 94.91, 27,
    #      "https://img.alicdn.com/imgextra/i4/1583725153/TB2.s6IjAfb_uJjSsrbXXb6bVXa_!!1583725153.jpg_430x430q90.jpg",
    #      677783])
    # url: https://detail.tmall.com/item.htm?id=602096306654&ali_refid=a3_430673_1006:1154900004:N:KT0+otDGCXB8uU89EnsiMg==:8481c4be19a034c1d778e2f6fab84bc8&ali_trackid=1_8481c4be19a034c1d778e2f6fab84bc8&spm=a2e15.8261149.07626516002.10
    # tasks.append(
    #     ["4", "50012097", 1280, "萌化粉", 92.85, "Howaryou/好阿优", "HAY-807", 79.00, 20000, 79.00 * 20000, 92.97, 75,
    #      "https://img.alicdn.com/imgextra/i4/4035922652/O1CN01XKH8a31VSevHPcxOc_!!4035922652.png_430x430q90.jpg",
    #      677784])
    # url: https://item.taobao.com/item.htm?id=564681440422&ali_refid=a3_430673_1006:1106434920:N:KT0%2BotDGCXB8uU89EnsiMg%3D%3D:a9ecacbd3ed01448691026694b9fbc92&ali_trackid=1_a9ecacbd3ed01448691026694b9fbc92&spm=a2e15.8261149.07626516002.25
    # tasks.append(
    #     ["4", "50012097", 1281, "中国红", 89.55, "MIUI", "JE-B02C", 388.00, 952, 388.00 * 952, 90.20, 112,
    #      "https://gd4.alicdn.com/imgextra/i1/346352241/O1CN01Mxb0h81SQQ9hVnhQZ_!!346352241.jpg_400x400.jpg",
    #      677785])
    for task in tasks:
        add(task)
