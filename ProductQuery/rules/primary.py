# -*- coding: utf-8 -*-

from refo import Star, Any

from ProductQuery.rules.rule import Rule
from ProductQuery.predicate import *
from ProductQuery.questions import *

# TODO
"""
1. 某演员演了什么电影
2. 某电影有哪些演员出演
3. 演员A和演员B合作出演了哪些电影
4. 某演员参演的评分大于X的电影有哪些
5. 某演员出演过哪些类型的电影
6. 某演员出演的XX类型电影有哪些。
7. 某演员出演了多少部电影。
8. 某演员是什么类型的演员吗。
9. 某演员的生日/出生地/英文名/简介
10. 某电影的简介/上映日期/评分
"""

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

rules = list()
rules.append(Rule(condition_num=2, condition=p_hasAbility + DotStarNG + entity_function + DotStarNG, action=ProductQuestionSet.has_function_question))
