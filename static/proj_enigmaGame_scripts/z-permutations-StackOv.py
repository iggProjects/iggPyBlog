from math import factorial
# xrange not working
def permutations(l):
    permutations=[]
    length=len(l)
    for x in xrange(factorial(length)):
        available=list(l)
        newPermutation=[]
        for radix in xrange(length, 0, -1):
            placeValue=factorial(radix-1)
            index=x/placeValue
            newPermutation.append(available.pop(index))
            x-=index*placeValue
        permutations.append(newPermutation)
    return permutations

# MAIN
if __name__ == "__main__":

    permutations(range(3))