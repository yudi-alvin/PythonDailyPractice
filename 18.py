"""
This problem was asked by Google.
Given an array of integers and a number k, where 1 <= k <= length of the array, 
compute the maximum values of each subarray of length k.
For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
•	10 = max(10, 5, 2)
•	7 = max(5, 2, 7)
•	8 = max(2, 7, 8)
•	8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.

"""
def getMaxValue(arr,k):
    res=[]
    for i in range(len(arr) - k + 1):#O(k*n)
        res.append(max(arr[i:i+k]))
    return res

arr=[10, 5, 2, 7, 8, 7] 
k=3
print(getMaxValue(arr,k))



"""
Deque can be implemented in python using the module “collections“. 
Deque is preferred over list in the cases where we need quicker append and pop operations from both the ends of container, 
as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity.
Operations on deque :
1. append() :- This function is used to insert the value in its argument to the right end of deque.
2. appendleft() :- This function is used to insert the value in its argument to the left end of deque.
3. pop() :- This function is used to delete an argument from the right end of deque.
4. popleft() :- This function is used to delete an argument from the left end of deque.
5. index(ele, beg, end) :- This function returns the first index of the value mentioned in arguments, starting searching from beg till end index.
6. insert(i, a) :- This function inserts the value mentioned in arguments(a) at index(i) specified in arguments.
7. remove() :- This function removes the first occurrence of value mentioned in arguments.
8. count() :- This function counts the number of occurrences of value mentioned in arguments.
9. extend(iterable) :- This function is used to add multiple values at the right end of deque. The argument passed is an iterable.
10. extendleft(iterable) :- This function is used to add multiple values at the left end of deque. The argument passed is an iterable. Order is reversed as a result of left appends.
11. reverse() :- This function is used to reverse order of deque elements.
12. rotate() :- This function rotates the deque by the number specified in arguments. If the number specified is negative, rotation occurs to left. Else rotation is to right.

"""
from collections import deque

def getMaxValue(arr,k):
    """The queue will store indexes of useful  
    elements in every window and it will 
    maintain decreasing order of values from 
    front to rear in Qi, i.e., arr[Qi.front[]] 
    to arr[Qi.rear()] are sorted in decreasing 
    order"""
    Qi= deque()
    for i in range(len(arr)): #complexity O(n)
        if i >=k:
        # print the front que (largest element) 
            print(str(arr[Qi[0]]) + ", ", end = "") 
        
        # Remove the elements which are out of this window 
        while Qi and Qi[0] <= i-k: 
            Qi.popleft()  
        
        # Remove all elements smaller than the currently being added element 
        while Qi and arr[i] >= arr[Qi[-1]] : 
            Qi.pop() 

        Qi.append(i) 

        # Print the maximum element of last window 
    print(str(arr[Qi[0]])) 


arr=[10, 15, 2, 7, 8, 7] 
k=3
getMaxValue(arr,k)
