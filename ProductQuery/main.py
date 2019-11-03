# -*- coding: utf-8  -*-

from ProductQuery import JenaFuseki
from ProductQuery import nl2sparql


if __name__ == '__main__':
    fuseki = JenaFuseki.JenaFuseki()
    q2s = nl2sparql.NL2Sparql()

    while True:
        question = input()
        my_query = q2s.get_sparql(question)
        print(my_query)
        if my_query is not None:
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
                    for inx in range(0, len(value), 2):
                        print(f"{inx}. {value[inx]} {value[inx+1]}")

        else:
            print('I can\'t understand. :(')

        print('#' * 100)
