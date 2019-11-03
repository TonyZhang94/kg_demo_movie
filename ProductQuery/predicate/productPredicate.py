# -*- coding: utf-8 -*-

from ProductQuery.predicate.predicate import W


# TODO
pos_brand = "nbr"
pos_model = "nmo"
pos_function = "nfu"

entity_brand = (W(pos=pos_brand))
entity_model = (W(pos=pos_model))
entity_function = (W(pos=pos_function))

p_function = (W("功能") | W("作用"))
p_hasAbility = (W("可以") | W("能够"))
