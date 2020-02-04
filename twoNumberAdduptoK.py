"""Given a list of integer and k, return true if any two integer in the list add up to k
l=[10,15,3,7]
k=17
since 10 + 7 = 17
return true"""
l=[10,15,3,7]
k=17
#brute force
def numberVerification(l,k):# Complexity n^2
    for i in range(len(l)-1): #n
        for j in range(i+1,len(l)):
            if l[i] + l[j] ==17:
                return True
    return False

print(numberVerification(l,k))

#induction
l= [7,6,6,3,9,3,5,1,12]
k=12
def numberVerification2(l,k):#Complexity nlog(n) + n/2
    l= sorted(l)
    print(l)
    i=0
    j=len(l)-1
    a=[]
    for x in range(int(j/2)+2):
        if l[i] + l[j] <k:
            i= i + 1
        elif l[i]+ l[j]> k:
            j = j - 1
        elif l[i]+ l[j]==k:
            a.append([l[i], l[j]])
    return a

print(numberVerification2(l,k))

