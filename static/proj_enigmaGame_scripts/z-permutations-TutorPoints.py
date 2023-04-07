#
# https://www.tutorialspoint.com/print-first-n-distinct-permutations-of-string-using-itertools-in-python
#


from itertools import permutations
import time

def k_permutations(str, k):
   s = sorted(list(str))
   p = permutations(s)
   m = 0
   set_1 = set()
   str = ''
   while m < k:
      str = ''.join(p.__next__())
      if str not in set_1:
         set_1.add(str)
         print(f"{m}: {str}")
         m += 1
         
   all_permutations = list(permutations(str))
   print(f"\nTotal permutations of alphabet: {len(all_permutations)}\n")

# Pausa ejecucion
def pausar():
	userInput = input('Presiona ENTER para continuar CTRL-C para salir. ');

# MAIN
if __name__ == "__main__":
   # time
   inicio = time.time()
   str = "abcdefghijk"
    #str = "abcdefghijklmnopqrstuvwxyz"

   """    
    # print all
    i=1
    for perm in all_permutations:       
       print(f"{i}: {perm}")
       i+=1
   """
   # print first 'numb_perm'
   numb_perm = 100
   print(f"First {numb_perm} permutations: ")
   k_permutations(str, numb_perm)
   print(f"Duración: {time.time()-inicio}/n/n")

   

