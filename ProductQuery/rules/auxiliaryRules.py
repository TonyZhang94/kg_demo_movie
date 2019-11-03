# -*- coding: utf-8 -*-

from refo import Star, Any, Disjunction

from ProductQuery.rules.rule import KeywordRule
from ProductQuery.predicate import *
from ProductQuery.properties.xsdProperties import xsdPropertySet
from ProductQuery.properties.IRIsProperties import IRIsPropertySet

# # TODO 具体的属性词匹配规则
# genre_keyword_rules = [
#     KeywordRule(condition=person_entity + Star(Any(), greedy=False) + adventure + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=xsdPropertySet.return_adventure_value),
#     KeywordRule(condition=person_entity + Star(Any(), greedy=False) + fantasy + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=xsdPropertySet.return_fantasy_value),
#     KeywordRule(condition=person_entity + Star(Any(), greedy=False) + animation + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=xsdPropertySet.return_animation_value),
#     KeywordRule(condition=person_entity + Star(Any(), greedy=False) + drama + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=xsdPropertySet.return_drama_value),
#     KeywordRule(condition=person_entity + Star(Any(), greedy=False) + thriller + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=xsdPropertySet.return_thriller_value),
#     KeywordRule(condition=person_entity + Star(Any(), greedy=False) + action + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=xsdPropertySet.return_action_value),
#     KeywordRule(condition=person_entity + Star(Any(), greedy=False) + comedy + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=xsdPropertySet.return_comedy_value),
#     KeywordRule(condition=person_entity + Star(Any(), greedy=False) + history + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=xsdPropertySet.return_history_value),
#     KeywordRule(condition=person_entity + Star(Any(), greedy=False) + western + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=xsdPropertySet.return_western_value),
#     KeywordRule(condition=person_entity + Star(Any(), greedy=False) + horror + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=xsdPropertySet.return_horror_value),
#     KeywordRule(condition=person_entity + Star(Any(), greedy=False) + crime + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=xsdPropertySet.return_crime_value),
#     KeywordRule(condition=person_entity + Star(Any(), greedy=False) + documentary + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=xsdPropertySet.return_documentary_value),
#     KeywordRule(condition=person_entity + Star(Any(), greedy=False) + science_fiction + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=xsdPropertySet.return_fiction_value),
#     KeywordRule(condition=person_entity + Star(Any(), greedy=False) + mystery + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=xsdPropertySet.return_mystery_value),
#     KeywordRule(condition=person_entity + Star(Any(), greedy=False) + music + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=xsdPropertySet.return_music_value),
#     KeywordRule(condition=person_entity + Star(Any(), greedy=False) + romance + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=xsdPropertySet.return_romance_value),
#     KeywordRule(condition=person_entity + Star(Any(), greedy=False) + family + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=xsdPropertySet.return_family_value),
#     KeywordRule(condition=person_entity + Star(Any(), greedy=False) + war + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=xsdPropertySet.return_war_value),
#     KeywordRule(condition=person_entity + Star(Any(), greedy=False) + TV + Star(Any(), greedy=False) + (movie | Star(Any(), greedy=False)), action=xsdPropertySet.return_tv_value)
# ]
#
# compare_keyword_rules = [
#     KeywordRule(condition=person_entity + Star(Any(), greedy=False) + higher + number_entity + Star(Any(), greedy=False) + movie + Star(Any(), greedy=False), action=xsdPropertySet.return_higher_value),
#     KeywordRule(condition=person_entity + Star(Any(), greedy=False) + lower + number_entity + Star(Any(), greedy=False) + movie + Star(Any(), greedy=False), action=xsdPropertySet.return_lower_value)
# ]
#
# person_genre_type_rules = [
#     KeywordRule(condition=person_entity + Star(Any(), greedy=False) + comedy + actor + Star(Any(), greedy=False), action=IRIsPropertySet.return_comedian_iris),
#     KeywordRule(condition=person_entity + Star(Any(), greedy=False) + action + actor + Star(Any(), greedy=False), action=IRIsPropertySet.return_kungfuactor_iris)
# ]
#
# person_basic_keyword_rules = [
#     KeywordRule(condition=(person_entity + Star(Any(), greedy=False) + where + birth_place + Star(Any(), greedy=False)) | (person_entity + Star(Any(), greedy=False) + birth_place + Star(Any(), greedy=False)), action=IRIsPropertySet.return_birth_place_value),
#     KeywordRule(condition=person_entity + Star(Disjunction(Any(), where), greedy=False) + birth + Star(Any(), greedy=False), action=IRIsPropertySet.return_birth_value),
#     KeywordRule(condition=person_entity + Star(Any(), greedy=False) + english_name + Star(Any(), greedy=False), action=IRIsPropertySet.return_english_name_value),
#     KeywordRule(condition=person_entity + Star(Any(), greedy=False) + introduction + Star(Any(), greedy=False), action=IRIsPropertySet.return_person_introduction_value)
# ]
#
# movie_basic_keyword_rules = [
#     KeywordRule(condition=movie_entity + Star(Any(), greedy=False) + introduction + Star(Any(), greedy=False), action=IRIsPropertySet.return_movie_introduction_value),
#     KeywordRule(condition=movie_entity + Star(Any(), greedy=False) + release + Star(Any(), greedy=False), action=IRIsPropertySet.return_release_value),
#     KeywordRule(condition=movie_entity + Star(Any(), greedy=False) + rating + Star(Any(), greedy=False), action=IRIsPropertySet.return_rating_value),
# ]
