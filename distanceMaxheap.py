import heapq

k=3
res=[]
d= {18:(3,4), 42:(6,7), 37:(4,7), 8:(2,1), 2:(2,2), 23:(4,5), 7:(2,3), -4:(2,-2)}

#using sort
l=sorted(d) #complexity: O(nlogn)
for i in range(k):
    res.append(d.get(l[i]))
print(res)

#USING HEAP O(k + (n-k)logk)
l=list(d.keys())
heapq.heapify(l)#must be a list
# print(heapq.nlargest(3, l))  # [42, 42, 37]
# print(heapq.nsmallest(3, l)) # [-4, -4, 2]

res=[]
for i in heapq.nsmallest(3, l):
    res.append(d.get(i))
print(res)


#Selection sort 
res=[]
l=list(d.keys())
min_ind=0
    #Complexity: O(n^)
n=len(l)
for i in range(k): #k
    min_value=l[0]
    for j in range(n-i): #n
        if l[j] < min_value:
            min_value = l[j]
            min_ind =j
    if min_ind == n-1-i:
        pass
    else:
        temp=l[n-i-1]
        l[n-i-1]=min_value
        l[min_ind]=temp        
res=[]
for i in range(k):
    res.append(d.get(l[n-1-i]))
print(res)



