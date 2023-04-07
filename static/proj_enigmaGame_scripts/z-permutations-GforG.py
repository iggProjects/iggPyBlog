# Python3 program to print first n unique
# permutations of the string using itertools
from itertools import permutations

# Function to print first n unique
# permutation using itertools
def nPermute(string, n):

	# Convert the string to list and sort the characters in alphabetical order
	#strList = sorted(list(string))	
	# Create an iterator
	permList = permutations(string)
	# Keep iterating until we reach nth unique permutation

	"""
	# Convert the string to list and sort the characters in alphabetical order
	strList = sorted(list(string))	
	# Create an iterator
	permList = permutations(strList)
	# Keep iterating until we reach nth unique permutation
	"""
	permSet = set()
	tempStr = ''
	print(f"==== List of n permutations strings for \"{string}\"")
	i=1
	while i < n:
		
		#tempStr = permList.__next__()		
		tempStr = ''.join(permList.__next__())		
		# Insert the string in the set. If it is not already included print it out.
		if tempStr not in permSet:
			permSet.add(tempStr)
			print(f"{i}: {tempStr}")
			i += 1
	print(f"\n==================================\n")
	for perm in permList:
		print(perm)		
	
# MAIN
if __name__ == "__main__":

	string = "abcde"
	n = 6
	nPermute(string, n)
