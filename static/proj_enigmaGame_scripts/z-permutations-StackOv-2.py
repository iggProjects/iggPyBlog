import string, time

STR = 'abcdefghijk'
LIST = list(STR)
# ORIG_STR = list(string.ascii_lowercase)      # in list mode

global result
result = []
alphab_list=[] 

def permutation(li):
    if li == [] or li == None:
        return

    if len(li) == 1:
        result.append(li[0])
        #print(f"{result}")
        alphab_list.append(result)
        result.pop()
        return

    for i in range(0,len(li)):
        result.append(li[i])
        permutation(li[:i] + li[i+1:])
        result.pop()   

# MAIN
if __name__ == "__main__":

    # time
    inicio = time.time()
    print(f"orig string--> {LIST}")

    permutation(LIST)
    print(f"\nresult lenght: {len(alphab_list)}\n")

    print(f"\nDuración: {time.time()-inicio}\n\n")