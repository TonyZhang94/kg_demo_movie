# -*- coding: utf-8 -*-

from refo import Star, Any

from ProductQuery.rules.rule import Rule
from ProductQuery.predicate import *
from ProductQuery.questions import *

# TODO
# rules = [
#     Rule(condition_num=2, condition=person_entity + Star(Any(), greedy=False) + movie + Star(Any(), greedy=False), action=MovieQuestionSet.has_movie_question),
#     Rule(condition_num=2, condition=(movie_entity + Star(Any(), greedy=False) + actor + Star(Any(), greedy=False)) | (actor + Star(Any(), greedy=False) + movie_entity + Star(Any(), greedy=False)), action=MovieQuestionSet.has_actor_question),
#     Rule(condition_num=3, condition=person_entity + Star(Any(), greedy=False) + person_entity + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=MovieQuestionSet.has_cooperation_question),
#     Rule(condition_num=4, condition=person_entity + Star(Any(), greedy=False) + compare + number_entity + Star(Any(), greedy=False) + movie + Star(Any(), greedy=False), action=MovieQuestionSet.has_compare_question),
#     Rule(condition_num=3, condition=person_entity + Star(Any(), greedy=False) + category + Star(Any(), greedy=False) + movie, action=MovieQuestionSet.has_movie_type_question),
#     Rule(condition_num=3, condition=person_entity + Star(Any(), greedy=False) + genre + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=MovieQuestionSet.has_specific_type_movie_question),
#     Rule(condition_num=3, condition=person_entity + Star(Any(), greedy=False) + several + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=MovieQuestionSet.has_quantity_question),
#     Rule(condition_num=3, condition=person_entity + Star(Any(), greedy=False) + genre + actor + Star(Any(), greedy=False), action=MovieQuestionSet.is_specific_genre_actor_question),
#     Rule(condition_num=3, condition=(person_entity + Star(Any(), greedy=False) + (when | where) + person_basic + Star(Any(), greedy=False)) | (person_entity + Star(Any(), greedy=False) + person_basic + Star(Any(), greedy=False)), action=MovieQuestionSet.has_basic_person_info_question),
#     Rule(condition_num=2, condition=movie_entity + Star(Any(), greedy=False) + movie_basic + Star(Any(), greedy=False), action=MovieQuestionSet.has_basic_movie_info_question)
# ]

DotStarNG = Star(Any(), greedy=False)
DotStar = Star(Any(), greedy=True)
regex_product = ((entity_brand + DotStarNG + entity_model) | (entity_model + DotStarNG + entity_brand))

rules = list()
# 拥有某项属性的某类产品
# e.g. 我想查看可以喷雾的电子美容仪有哪些
rules.append(Rule(condition_num=3, condition=p_hasAbility + DotStarNG + entity_attribute + DotStarNG + entity_cidname, action=ProductQuestionSet.has_attribute_question))
# e.g. 电子美容仪中可以喷雾的有哪些型号
rules.append(Rule(condition_num=3, condition=entity_cidname + DotStarNG + p_hasAbility + DotStarNG + entity_attribute, action=ProductQuestionSet.has_attribute_question))

# 某项属性高的某品牌-型号
rules.append(Rule(condition_num=2, condition=entity_attribute + DotStarNG + p_better, action=ProductQuestionSet.has_high_performance_question))

# 某品牌-型号某项属性的得分
rules.append(Rule(condition_num=4, condition=regex_product + DotStarNG + entity_attribute + DotStarNG + p_score, action=ProductQuestionSet.product_has_performance_score_question))

# 某属性的最高得分
rules.append(Rule(condition_num=2, condition=entity_attribute + DotStarNG + p_highest, action=ProductQuestionSet.product_highest_performance_question))

# 指定brand，model的产品某项属性的排名
rules.append(Rule(condition_num=4, condition=regex_product + DotStarNG + entity_attribute + DotStarNG + p_rank, action=ProductQuestionSet.product_has_performance_rank_question))

# 某项属性有多少个
rules.append(Rule(condition_num=2, condition=entity_attribute + DotStarNG + p_total, action=ProductQuestionSet.product_has_performance_total_question))

# 指定brand，model的产品某项属性好不好高不高
rules.append(Rule(condition_num=4, condition=regex_product + DotStarNG + entity_attribute + DotStarNG + p_question, action=ProductQuestionSet.product_has_performance_detail_question))

# 具体取值(推导颜色：功能)
rules.append(Rule(condition_num=1, condition=entity_attribute, action=ProductQuestionSet.has_standard_property_question))

# 获取有某项功能的品类
# e.g. 有哪些类别的宝贝具有去鱼尾纹的功能
rules.append(Rule(condition_num=2, condition=p_cidname + DotStarNG + entity_attribute, action=ProductQuestionSet.catalog_has_performance_question))
# e.g. 去鱼尾纹的品类有哪些
rules.append(Rule(condition_num=2, condition=entity_attribute + DotStarNG + p_cidname, action=ProductQuestionSet.catalog_has_performance_question))
# e.g. 可以去鱼尾纹的品类有哪些
rules.append(Rule(condition_num=3, condition=p_hasAbility + DotStarNG + entity_attribute + DotStarNG + p_cidname, action=ProductQuestionSet.catalog_has_performance_question))
