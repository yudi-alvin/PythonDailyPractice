"""
This problem was asked by Stripe.
Given an array of integers, find the first missing positive integer in linear time O(n) and constant space O(1). In other words, 
find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.

From Stack Overflow
Hash tables are O(1) average and amortized case complexity, however it suffers from O(n) worst case time complexity. 
[And I think this is where your confusion is] Hash tables suffer from O(n) worst time complexity due to two reasons:
If too many elements were hashed into the same key: looking inside this key may take O(n) time.
Once a hash table has passed its load balance - it has to rehash [create a new bigger table, and re-insert each element to the table].
However, it is said to be O(1) average and amortized case because:
It is very rare that many items will be hashed to the same key [if you chose a good hash function and you don't have too big load balance.
The rehash operation, which is O(n), can at most happen after n/2 ops, which are all assumed O(1): 
Thus when you sum the average time per op, you get : (n*O(1) + O(n)) / n) = O(1)

"""
l=[3,4,-1,1]
l=[1,2,0]
#brute force
def fun1(l): #O(nlogn + n)
    s = set(l)
    l = sorted(list(s)) #O(n log n)
    for i in range(len(l)): #O(n)
        if l[i] <= 1:
            pass
        elif l[i] - 1 != l[i-1]:
            return (l[i-1] +1 )
    return l[-1]+1
# print(fun1(l))


def fun2(l): # complexity time: O(n) + O(n) Space:O(n)
    m =max(l)
    if m < 1:
        return 1
    
    d=dict()
    for x in l: #O(n)
        if x > 0:
            d[x]= 0 #remove duplicate

    for i in range(1,len(l)+1): #O(n)
        if d.get(i) == None:
            return i
    return (m +1)
# print(fun2(l))


def fun3(l): # complexity time: O(n) + O(n) Space:O(1)
    m =max(l)
    if m < 1:
        return 1
    arr=[0]*100
    for i in range(len(l)):
        if l[i]>0:
            arr[l[i]]= l[i]
    for i in range(len(arr)):
        if i != arr[i]:
            return i
        
print(fun3(l))

    



