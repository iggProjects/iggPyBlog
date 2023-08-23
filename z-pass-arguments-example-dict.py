import sys
import json
from ast import literal_eval


"""
https://stackoverflow.com/questions/18006161/how-to-pass-dictionary-as-command-line-argument-to-python-script

Print dictionary key values
py .\z-pass-arguments-example-dict.py "{ 'key1': 'val1', 'key2': 'val2' }"

"{'name': ['J.J.', 'April'], 'age': ['25', '29']}"  vs  "{1: ['J.J.', 'April'], 2: ['25', '29']}"

import json
data=json.loads(argv[1])
"""

def print_dict_data(dict):
    print(f"dict variable is type: {type(dict)}")
    print(f"dict is: {dict}")
    for k in dict:
        print(f"key: {k}, type of key: {type(k)} ||| value: {dict[k]}, type of value: {type(dict[k])} ")

if __name__ == "__main__":
    # argument is a json
    # dict_k_v= json.loads(sys.argv[1])
    data= sys.argv[1]
    dict_k_v = literal_eval(data)
    print_dict_data(dict_k_v)
