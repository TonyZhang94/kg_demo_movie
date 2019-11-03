# -*- coding: utf-8 -*-

from ProductQuery.template.prefix import SPARQL_PREXIX
from ProductQuery.template.sparql import SPARQL_SELECT_TEM, SPARQL_COUNT_TEM, SPARQL_ASK_TEM
from ProductQuery.rules import *


class ProductQuestionSet:
    def __init__(self):
        pass

    @staticmethod
    def has_function_question(word_objects):
        """
        某品牌-型号拥有某项功能
        :param word_objects:
        :return:
        """
        select = u"?brand ?model"

        sparql = None
        for w in word_objects:
            if w.pos == pos_function:
                e = u"?s :model_to_function ?m." \
                    u"?m :function_name '{function}'." \
                    u"?s :model_brand ?brand." \
                    u"?s :model_model ?model".format(function=w.token)

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break
        return sparql

    @staticmethod
    def has_subfunction_question(word_objects):
        """
        展现上下谓词搜索，喜剧演员与演员 subclass的关系
        :param word_objects:
        :return:
        """
        select = u"?brand ?model"

        sparql = None
        for w in word_objects:
            if w.pos == pos_function:
                e = u"?s :model_to_function ?m." \
                    u"?m :function_name '{function}'." \
                    u"?s :model_brand ?brand." \
                    u"?s :model_model ?model".format(function=w.token)

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break
        return sparql

    @staticmethod
    def has_xxx(word_objects):
        """
        数据上下手
        1。
        展现上下谓词搜索，喜剧演员与演员 subclass的关系，function都定义为class？？？,加入other，name表？正解
        推理怎么弄
        查询需要name与nickname，uninion

        2。
        搜索结果跨品类

        # :param word_objects:
        # :return:
        # """
        # select = u"?brand ?model"
        #
        # sparql = None
        # for w in word_objects:
        #     if w.pos == pos_function:
        #         e = u"?s :model_to_function ?m." \
        #             u"?m :function_name '{function}'." \
        #             u"?s :model_brand ?brand." \
        #             u"?s :model_model ?model".format(function=w.token)
        #
        #         sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
        #                                           select=select,
        #                                           expression=e)
        #         break
        # return sparql

    # 联合查找，找一个具体
    @staticmethod
    def has_cidname_question(word_objects):
        """
        我要一个低功率的料理机
        :param word_objects:
        :return:
        """

    @staticmethod
    def has_power_question(word_objects):
        """
        我要一个低功率的料理机
        （1）具体功率（2）低功率，排序输出
        :param word_objects:
        :return:
        """

    @staticmethod
    def has_cost_performance_question(word_objects):
        """
        要高/低性价比
        :param word_objects:
        :return:
        """

    @staticmethod
    def has_volume_question(word_objects):
        """
        指定容积
        （1）具体（2）形容
        :param word_objects:
        :return:
        """

    @staticmethod
    def has_applicable_number_question(word_objects):
        """
        多少人用
        :param word_objects:
        :return:
        """

    @staticmethod
    def is_high_cost_performance_question(word_objects):
        """
        性价比高不高
        :param word_objects:
        :return:
        """
