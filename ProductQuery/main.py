# -*- coding: utf-8  -*-

from ProductQuery import JenaFuseki
from ProductQuery import nl2sparql
from ProductQuery import wordTagging
from ProductQuery import answerTemplate


if __name__ == '__main__':
    fuseki = JenaFuseki.JenaFuseki()
    q2s = nl2sparql.NL2Sparql()

    while True:
        question = input()
        question = wordTagging.pre_process(question)
        store = q2s.get_sparql(question)
        if store is not None:
            my_query, selects, rule_id = store
            print(my_query)
            print("rule id =", rule_id)
            result = fuseki.get_sparql_result(my_query)
            values = fuseki.get_sparql_result_value(result)

            if 1 == int(rule_id):
                answerTemplate.answer_select(values, selects, mode="SIGROW")
            elif 2 == int(rule_id):
                answerTemplate.answer_select(values, selects, mode="SIGROW")
            elif 3 == int(rule_id):
                answerTemplate.answer_ask(values)
            elif 4 == int(rule_id):
                answerTemplate.answer_select(values, selects, mode="SIGROW")
            elif 5 == int(rule_id):
                answerTemplate.answer_whether_nice(values)
            elif 6 == int(rule_id):
                answerTemplate.answer_count(values)
            elif 7 == int(rule_id):
                answerTemplate.answer_select(values, selects, mode="SIGROW")
            elif 8 == int(rule_id):
                answerTemplate.answer_select(values, selects, mode="SIGROW")
            elif 9 == int(rule_id):
                answerTemplate.answer_select(values, selects, mode="SIGROW")
            elif 10 == int(rule_id):
                answerTemplate.answer_detail(values)
            elif 0 == int(rule_id):
                answerTemplate.answer_select(values, selects, mode="SIGROW")
        else:
            print('I can\'t understand. :(')

        print('#' * 100)
