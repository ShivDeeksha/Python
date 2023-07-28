'''
Find Kth Permutation:
Given two integers N(1<=N<=9) and k. 
Find the Kth Permutation sequence of firt N natural Numbers.
Return answer in string format.
'''
from itertools import permutations
li = []
n = int(input("Enter value of N: "))
k = int(input("Enter value of K: "))
for i in range(1, n + 1):
  li.append(str(i))

perm=[''.join(p) for p in permutations(li)]
print("\nThe 3rd permutation of sequence of natural numbers till",n,"is: ")
print(str(perm[k-1]))
