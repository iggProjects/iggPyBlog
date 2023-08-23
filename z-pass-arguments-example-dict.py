import sys
import json
from ast import literal_eval


"""
Print dictionary key values
py .\z-pass-arguments-example-dict.py "{ 'key1': 'val1', 'key2': 'val2' }"
"{'name': ['J.J.', 'April'], 'age': ['25', '29']}"

import json
data=json.loads(argv[1])
"""

def print_dict_data(dict):
    print(f"dict variable is type: {type(dict)}")
    print(f"dict is: {dict}")
    for k in dict:
        print(f"key: {k}, value: {dict[k]} ")

if __name__ == "__main__":
    # argument is a json
    # dict_k_v= json.loads(sys.argv[1])
    data= sys.argv[1]
    dict_k_v = literal_eval(data)
    print_dict_data(dict_k_v)
