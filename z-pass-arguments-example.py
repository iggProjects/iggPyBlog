import sys

"""
First and second argument are type string, and third argument represent a list of string separated by ','
https://stackoverflow.com/questions/17544307/how-do-i-run-python-script-using-arguments-in-windows-command-line
"""

def hello(a,b):
    print(f"Hello, your sum is: {a + b}")

def hello1(list_numb):
    numb_sum = 0
    for numb in list_numb:
        numb_sum += int(numb)
    print(f"Hello, the sum of list is: {numb_sum}")

if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    # third argument is a list of strings
    l = sys.argv[3].split(',')
    hello(a, b)
    hello1(l)