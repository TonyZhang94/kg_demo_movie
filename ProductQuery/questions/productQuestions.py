# -*- coding: utf-8 -*-

from ProductQuery.template.prefix import SPARQL_PREXIX
from ProductQuery.template.sparql import SPARQL_SELECT_TEM, SPARQL_COUNT_TEM, SPARQL_ASK_TEM, ORDER_ASC_TEM, ORDER_DESC_TEM, LIMIT_TEM
from ProductQuery.rules import *
from ProductQuery import wordTagging


class ProductQuestionSet:
    def __init__(self):
        pass

    @staticmethod
    def has_attribute_question(word_objects):
        """
        拥有某项属性的某类产品
        e.g. 我想查看可以喷雾的电子美容仪有哪些
        e.g. 电子美容仪中可以喷雾的有哪些型号
        :param word_objects:
        :return:
        """
        select = u"?brand ?model ?biz"

        cidname = None
        for w in word_objects:
            if w.pos == pos_cidname:
                cidname = w.token
                break

        if cidname is None:
            return None, 0

        sparql = None
        suffix = ORDER_DESC_TEM.format(key="?biz")
        for w in word_objects:
            if w.pos == pos_attribute:
                e = u"?s :model_to_catalog ?cid." \
                    u"?cid :catalogid_cidname '{cidname}'." \
                    u"?s :model_to_function ?m." \
                    u"?s :model_brand ?brand." \
                    u"?s :model_model ?model." \
                    u"?s :model_biz30day ?biz." \
                    u"?m :function_name '{function}'.".format(cidname=cidname,
                                                              function=w.token)

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e,
                                                  suffix=suffix)
                break
        return sparql, len(select.split())

    @staticmethod
    def has_high_performance_question(word_objects):
        """
        某项属性高的某品牌-型号
        :param word_objects:
        :return:
        """
        select = u"?brand ?model ?attr ?score"

        sparql = None
        # suffix = ORDER_DESC_TEM.format(key="?score") + LIMIT_TEM.format(limit=10)
        suffix = ORDER_DESC_TEM.format(key="?score")
        for w in word_objects:
            if w.pos == pos_attribute:
                e = u"?s :model_to_function ?o." \
                    u"?s :model_brand ?brand." \
                    u"?s :model_model ?model." \
                    u"?o :function_name '{function}'." \
                    u"?o :function_name ?attr." \
                    u"?x :model_to_function_score ?score." \
                    u"?x :model_to_function_id ?s." \
                    u"?x :model_to_function_funcid ?o.".format(function=w.token)

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e,
                                                  suffix=suffix)
                break
        return sparql, len(select.split())

    @staticmethod
    def product_has_performance_score_question(word_objects):
        """
        某品牌-型号某项属性的得分
        :param word_objects:
        :return:
        """
        select = u"?brand ?model ?attr ?score"

        brand = None
        for w in word_objects:
            if w.pos == pos_brand:
                brand = w.token
                break

        model = None
        for w in word_objects:
            if w.pos == pos_model:
                model = w.token
                break

        if not brand or not model:
            return None, 0
        else:
            brand = wordTagging.after_process(brand)
            model = wordTagging.after_process(model)

        sparql = None
        suffix = ""
        for w in word_objects:
            if w.pos == pos_attribute:
                e = u"?s :model_to_function ?o." \
                    u"?s :model_brand '{brand}'." \
                    u"?s :model_brand ?brand." \
                    u"?s :model_model '{model}'." \
                    u"?s :model_model ?model." \
                    u"?o :function_name '{function}'." \
                    u"?o :function_name ?attr." \
                    u"?x :model_to_function_score ?score." \
                    u"?x :model_to_function_id ?s." \
                    u"?x :model_to_function_funcid ?o.".format(function=w.token,
                                                               brand=brand,
                                                               model=model)

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e,
                                                  suffix=suffix)
                break
        return sparql, len(select.split())

    @staticmethod
    def product_highest_performance_question(word_objects):
        """
        某属性的最高得分
        :param word_objects:
        :return:
        """
        select = u"?brand ?model ?attr ?highest"

        sparql = None
        suffix = ORDER_DESC_TEM.format(key="?highest") + LIMIT_TEM.format(limit=1)
        for w in word_objects:
            if w.pos == pos_attribute:
                e = u"?s :model_to_function ?o." \
                    u"?s :model_brand ?brand." \
                    u"?s :model_model ?model." \
                    u"?o :function_name '{function}'." \
                    u"?o :function_name ?attr." \
                    u"?x :model_to_function_score ?highest." \
                    u"?x :model_to_function_id ?s." \
                    u"?x :model_to_function_funcid ?o.".format(function=w.token)

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e,
                                                  suffix=suffix)
                break
        return sparql, len(select.split())

    @staticmethod
    def product_has_performance_rank_question(word_objects):
        """
        指定brand，model的产品某项属性的排名
        :param
        word_objects:
        :return:
        """
        select = u"?other_score"

        sparql = None
        rank = "?rank"
        suffix = ""

        brand = None
        for w in word_objects:
            if w.pos == pos_brand:
                brand = w.token
                break

        model = None
        for w in word_objects:
            if w.pos == pos_model:
                model = w.token
                break

        if not brand or not model:
            return None, 0
        else:
            brand = wordTagging.after_process(brand)
            model = wordTagging.after_process(model)

        for w in word_objects:
            if w.pos == pos_attribute:
                e = u"?s :model_to_function ?o." \
                    u"?s :model_brand ?brand." \
                    u"?s :model_model ?model." \
                    u"?o :function_name '{function}'." \
                    u"?o :function_name ?attr." \
                    u"?x :model_to_function_score ?other_score." \
                    u"?x :model_to_function_id ?s." \
                    u"?x :model_to_function_funcid ?o.".format(function=w.token) + \
                    u"{" \
                    u"  SELECT DISTINCT ?score WHERE {" + \
                    u"    ?s :model_to_function ?o." \
                    u"    ?o :function_name '{function}'." \
                    u"    ?s :model_brand '{brand}'." \
                    u"    ?s :model_model '{model}'." \
                    u"    ?x :model_to_function_score ?score." \
                    u"    ?x :model_to_function_id ?s." \
                    u"    ?x :model_to_function_funcid ?o." .format(function=w.token,
                                                                    brand=brand,
                                                                    model=model) + \
                    u"  }" \
                    u"}" \
                    u"Filter(?other_score >= ?score)."

                sparql = SPARQL_COUNT_TEM.format(prefix=SPARQL_PREXIX,
                                                 select=select,
                                                 res=rank,
                                                 expression=e,
                                                 suffix=suffix)
                break
        return sparql, len(select.split())

    @staticmethod
    def product_has_performance_total_question(word_objects):
        """
        某项属性有多少个
        :param
        word_objects:
        :return:
        """
        select = u"?s"

        sparql = None
        res = "?total"
        suffix = ""
        for w in word_objects:
            if w.pos == pos_attribute:
                e = u"?s :model_to_function ?o." \
                    u"?o :function_name '{function}'.".format(function=w.token)

                sparql = SPARQL_COUNT_TEM.format(prefix=SPARQL_PREXIX,
                                                 select=select,
                                                 res=res,
                                                 expression=e,
                                                 suffix=suffix)
                break
        return sparql, len(select.split())

    @staticmethod
    def product_has_performance_detail_question(word_objects):
        """
        指定brand，model的产品某项属性好不好高不高
        :param word_objects:
        :return:
        """
        select = "?brand ?model ?attr ?score ?highest ?rank ?total"

        sparql = None
        suffix = ""

        brand = None
        for w in word_objects:
            if w.pos == pos_brand:
                brand = w.token
                break

        model = None
        for w in word_objects:
            if w.pos == pos_model:
                model = w.token
                break

        if not brand or not model:
            return None, 0
        else:
            brand = wordTagging.after_process(brand)
            model = wordTagging.after_process(model)

        e = "{" + ProductQuestionSet.product_has_performance_score_question(word_objects)[0][296:] + "}" + \
            "{" + ProductQuestionSet.product_highest_performance_question(word_objects)[0][296:].replace("?brand ?model ", "") + "}" + \
            "{" + ProductQuestionSet.product_has_performance_rank_question(word_objects)[0][296:] + "}" + \
            "{" + ProductQuestionSet.product_has_performance_total_question(word_objects)[0][296:] + "}"

        sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                          select=select,
                                          expression=e,
                                          suffix=suffix)
        return sparql, len(select.split())

    @staticmethod
    def has_standard_property_question(word_objects):
        """
        推理：有具体的属性取值
        :param word_objects:
        :return:
        """
        select = "?brand ?model ?attr"

        sparql = None
        suffix = ORDER_DESC_TEM.format(key="?biz")
        for w in word_objects:
            if w.pos == pos_attribute:
                e = u"?s :model_to_function ?o." \
                    u"?s :model_brand ?brand." \
                    u"?s :model_model ?model." \
                    u"?s :model_biz30day ?biz." \
                    u"?o :function_name '{property}'." \
                    u"?o :function_name ?attr.".format(property=w.token)

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e,
                                                  suffix=suffix)
                break
        return sparql, len(select.split())

    @staticmethod
    def catalog_has_performance_question(word_objects):
        """
        具有某个属性的品类有哪些
        :param
        word_objects:
        :return:
        """
        select = "?cidname ?brand ?model ?attr"

        cidname = None
        for w in word_objects:
            if w.pos == pos_cidname:
                cidname = w.token
                break

        if not cidname:
            return None, 0

        sparql = None
        suffix = ""
        for w in word_objects:
            if w.pos == pos_cidname:
                e = u"?s :model_to_catalog ?cid." \
                    u"?cid :catalogid_cidname ?cidname." \
                    u"?s :model_brand ?brand." \
                    u"?s :model_model ?model." \
                    u"?s :model_to_function ?o." \
                    u"?o :function_name '{property}'." \
                    u"?o :function_name ?attr.".format(property=w.token)

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e,
                                                  suffix=suffix)
                break
        return sparql, len(select.split())
