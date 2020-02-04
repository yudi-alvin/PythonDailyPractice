# Python3 implementation this is to use itertools. 
# permutations as coded below: 
  
from itertools import permutations 
def largest(l): 
    lst = [] 
    for x in permutations(l, len(l)): 
        # provides all permutations of the list values, 
        # store them in list to find max 
        lst.append("".join(map(str,x)))  
    return max(lst) 
  
print(largest([54, 546, 548, 60])) #Output 6054854654 
  
# This code is contributed by Raman Monga 