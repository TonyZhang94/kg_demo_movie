# -*- coding: utf-8 -*-

from ProductQuery.predicate.predicate import W


# TODO
pos_brand = "nbr"
pos_model = "nmo"
pos_attribute = "nattr"
pos_cidname = "ncid"

entity_brand = (W(pos=pos_brand))
entity_model = (W(pos=pos_model))
entity_attribute = (W(pos=pos_attribute))
entity_cidname = (W(pos=pos_cidname))

p_function = (W("功能") | W("作用"))
p_hasAbility = (W("可以") | W("能够"))
p_score = (W("得分") | W("分数"))
p_rank = (W("排名"))
p_total = (W("总共") | W("总数") | W("数量") | W("一共"))
p_highest = (W("最高得分") | W("最高分数"))
p_cidname = (W("品类") | W("类别"))
