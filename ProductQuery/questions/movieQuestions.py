# -*- coding: utf-8 -*-

from ProductQuery.template.prefix import SPARQL_PREXIX
from ProductQuery.template.sparql import SPARQL_SELECT_TEM, SPARQL_COUNT_TEM, SPARQL_ASK_TEM
from ProductQuery.rules import *


class MovieQuestionSet:
    def __init__(self):
        pass

    @staticmethod
    def has_movie_question(word_objects):
        """
        某演员演了什么电影
        :param word_objects:
        :return:
        """
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == pos_person:
                e = u"?s :personName '{person}'." \
                    u"?s :hasActedIn ?m." \
                    u"?m :movieTitle ?x".format(person=w.token)

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break
        return sparql

    @staticmethod
    def has_actor_question(word_objects):
        """
        哪些演员参演了某电影
        :param word_objects:
        :return:
        """
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == pos_movie:
                e = u"?m :movieTitle '{movie}'." \
                    u"?m :hasActor ?a." \
                    u"?a :personName ?x".format(movie=w.token)

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def has_cooperation_question(word_objects):
        """
        演员A和演员B有哪些合作的电影
        :param word_objects:
        :return:
        """
        select = u"?x"

        person1 = None
        person2 = None

        for w in word_objects:
            if w.pos == pos_person:
                if person1 is None:
                    person1 = w.token
                else:
                    person2 = w.token
        if person1 is not None and person2 is not None:
            e = u"?p1 :personName '{person1}'." \
                u"?p2 :personName '{person2}'." \
                u"?p1 :hasActedIn ?m." \
                u"?p2 :hasActedIn ?m." \
                u"?m :movieTitle ?x".format(person1=person1, person2=person2)

            return SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                          select=select,
                                          expression=e)
        else:
            return None

    @staticmethod
    def has_compare_question(word_objects):
        """
        某演员参演的评分高于X的电影有哪些？
        :param word_objects:
        :return:
        """
        select = u"?x"

        person = None
        number = None
        keyword = None

        for r in compare_keyword_rules:
            keyword = r.apply(word_objects)
            if keyword is not None:
                break

        for w in word_objects:
            if w.pos == pos_person:
                person = w.token

            if w.pos == pos_number:
                number = w.token

        if person is not None and number is not None:

            e = u"?p :personName '{person}'." \
                u"?p :hasActedIn ?m." \
                u"?m :movieTitle ?x." \
                u"?m :movieRating ?r." \
                u"filter(?r {mark} {number})".format(person=person, number=number,
                                                     mark=keyword)

            return SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                            select=select,
                                            expression=e)
        else:
            return None

    @staticmethod
    def has_movie_type_question(word_objects):
        """
        某演员演了哪些类型的电影
        :param word_objects:
        :return:
        """
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == pos_person:
                e = u"?s :personName '{person}'." \
                    u"?s :hasActedIn ?m." \
                    u"?m :hasGenre ?g." \
                    u"?g :genreName ?x".format(person=w.token)

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break
        return sparql

    @staticmethod
    def has_specific_type_movie_question(word_objects):
        """
        某演员演了什么类型（指定类型，喜剧、恐怖等）的电影
        :param word_objects:
        :return:
        """
        select = u"?x"

        keyword = None
        for r in genre_keyword_rules:
            keyword = r.apply(word_objects)

            if keyword is not None:
                break

        sparql = None
        for w in word_objects:
            if w.pos == pos_person:
                e = u"?s :personName '{person}'." \
                    u"?s :hasActedIn ?m." \
                    u"?m :hasGenre ?g." \
                    u"?g :genreName '{keyword}'." \
                    u"?m :movieTitle ?x".format(person=w.token, keyword=keyword)

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break
        return sparql

    @staticmethod
    def has_quantity_question(word_objects):
        """
        某演员演了多少部电影
        :param word_objects:
        :return:
        """
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == pos_person:
                e = u"?s :personName '{person}'." \
                    u"?s :hasActedIn ?x.".format(person=w.token)

                sparql = SPARQL_COUNT_TEM.format(prefix=SPARQL_PREXIX, select=select, expression=e)
                break

        return sparql

    @staticmethod
    def is_specific_genre_actor_question(word_objects):
        """
        某演员是什么类型的演员吗
        :param word_objects:
        :return:
        """
        sparql = None

        keyword = None
        for r in person_genre_type_rules:
            keyword = r.apply(word_objects)
            if keyword is not None:
                break

        for w in word_objects:
            if w.pos == pos_person:
                e = u"?s :personName '{person}'." \
                    u"?s rdf:type {genre_type}.".format(person=w.token, genre_type=keyword)

                sparql = SPARQL_ASK_TEM.format(prefix=SPARQL_PREXIX, expression=e)
                break

        return sparql

    @staticmethod
    def has_basic_person_info_question(word_objects):
        """
        某演员的基本信息是什么
        :param word_objects:
        :return:
        """

        keyword = None
        for r in person_basic_keyword_rules:
            keyword = r.apply(word_objects)
            if keyword is not None:
                break

        select = u"?x"
        sparql = None
        for w in word_objects:
            if w.pos == pos_person:
                e = u"?s :personName '{person}'." \
                    u"?s {keyword} ?x.".format(person=w.token, keyword=keyword)

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX, select=select, expression=e)

                break

        return sparql

    @staticmethod
    def has_basic_movie_info_question(word_objects):
        """
        某电影的基本信息是什么
        :param word_objects:
        :return:
        """

        keyword = None
        for r in movie_basic_keyword_rules:
            keyword = r.apply(word_objects)
            if keyword is not None:
                break

        select = u"?x"
        sparql = None
        for w in word_objects:
            if w.pos == pos_movie:
                e = u"?s :movieTitle '{movie}'." \
                    u"?s {keyword} ?x.".format(movie=w.token, keyword=keyword)

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX, select=select, expression=e)

                break

        return sparql
