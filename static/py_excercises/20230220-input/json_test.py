# Python3 code to demonstrate
# convert dictionary string to dictionary
# using json.loads()
import json, sys, os
os.system('cls') 
# initializing string
test_string = '{"Nikhil" : 1, "Akshat" : 2, "Akash" : 3}'
# printing original string
print(f"The original string : {str(test_string)} | type: {type(test_string)}")
# using json.loads()
# convert dictionary string to dictionary
myDict = json.loads(test_string)
# print result
print(f"The converted dictionary : {str(myDict)} | type: {type(myDict)}")

print()
print()

# case argument '{"A" : 22, "B" : 33}' 
test_string1 = sys.argv[1]
print(f"The argument string : {str(test_string1)} | type: {type(test_string1)}")
#
myDict1 = json.loads(test_string1)
print(f"The converted argument : {str(myDict1)} | type: {type(myDict1)}")
print()

for k in myDict1:
    print(f"key: {k} | value: {myDict1[k]}")

