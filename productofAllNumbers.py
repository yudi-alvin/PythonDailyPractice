"""Uber
Given an array of integers return a new array such that each element at index i 
of the new array is te product of all te numbers in the original array except tat one at i
For example:
input: [1,2,3,4,5]
output: [120, 60, 40, 30, 24]

input: [3,2,1]
output: [2,3,6]
"""
l=[2,3,4,5]
#brute force 
def productSum(l):#Complexity: n^2
    res=[]
    for i in range(len(l)):
        total =1
        for j in range(len(l)):
            if l[i] != l[j]:
                total = l[j] * total
        res.append(total)
    return res
print(productSum(l))

def productSum1(l):#Complexity: 2n
    res=[]
    total =1
    for x in l:
        total = total * x
    for i in range(len(l)):
        res.append(round(total/l[i]))
    return res
print(productSum1(l))

#Challenge without using division?
def productSum2(arr):#Complexity: 3n
    n = len(l)
    if n == 1:
        return l
    left = [0]*n
    right= [0]*n
    res=[0]*n

    left[0]=1
    right[n-1]= 1

    #accumulative from left to right
    for i in range(1, n):  
        left[i] = arr[i - 1] * left[i - 1]  
    # print(left)

    # accumulative from right to left
    for j in range(n-2, -1, -1):  
        right[j] = arr[j + 1] * right[j + 1]  
    # print(right)
    for i in range(n):
        res[i] =left[i] * right[i]
    return res

print(productSum2(l))

def productSum3(arr):#same as product sum two but use only one container res instead of left and right
    n = len(arr)
    i, temp = 1, 1
    res=[1]*n
    for i in range(n): 
        res[i] = temp 
        temp *= arr[i] 
    temp = 1
    for i in range(n - 1, -1, -1): 
        res[i] *= temp 
        temp *= arr[i] 
    
    return res
print(productSum3(l))