# -*- coding: utf-8  -*-

from ProductQuery import JenaFuseki
from ProductQuery import nl2sparql
from ProductQuery import wordTagging


if __name__ == '__main__':
    fuseki = JenaFuseki.JenaFuseki()
    q2s = nl2sparql.NL2Sparql()

    while True:
        question = input()
        question = wordTagging.pre_process(question)
        store = q2s.get_sparql(question)
        if store is not None:
            my_query, nums = store
            print(my_query)
            result = fuseki.get_sparql_result(my_query)
            value = fuseki.get_sparql_result_value(result)

            if isinstance(value, bool):
                if value is True:
                    print('Yes')
                else:
                    print('I don\'t know. :(')
            else:
                if len(value) == 0:
                    print('I don\'t know. :(')
                elif len(value) == 1:
                    print(value[0])
                else:
                    output = ''
                    for inx in range(0, min(len(value), 10*nums), nums):
                        for i in range(nums):
                            print(value[inx+i], end=" ")
                        print()

        else:
            print('I can\'t understand. :(')

        print('#' * 100)
