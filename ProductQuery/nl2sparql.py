# -*- coding: utf-8 -*-

from ProductQuery import wordTagging
from ProductQuery.rules.primary import rules


class NL2Sparql:
    def __init__(self):
        self.tw = wordTagging.Tagger()
        self.rules = rules

    def get_sparql(self, question):
        word_objects = self.tw.get_word_objects(question)
        queries_dict = dict()

        for rule in self.rules:
            query, num = rule.apply(word_objects)

            if query is not None:
                queries_dict[num] = query

        if len(queries_dict) == 0:
            return None
        elif len(queries_dict) == 1:
            return list(queries_dict.values())[0]
        else:
            sorted_dict = sorted(queries_dict.items(), key=lambda item: item[0], reverse=True)
            return sorted_dict[0][1]
