import random

#non duplicate and one number missing
random.seed(1)
li = list(random.sample(range(1,101), 99))
sumS= 100*(100+1)/2
print(sumS-sum(li))

#more than one missing number and non duplicate
li = list(random.sample(range(1,101), 90))
def missingValues(li,n =100):
    random.seed(1)
    missingli=[]
    missingLength = 100 - len(li)
    #create a list of false 0 to 100
    mark = [False for i in range(100 + 1)] 
    # filling in the available values
    for i in range(100 - missingLength): 
        mark[li[i]] = True

    for i in range(1,100):
        if not mark[i]:
            missingli.append(i)
    print(missingli)
missingValues(li)

#duplicate values and more than one missing values
#use set to remove all the duplicate
li=[]
for i in range(98):
    li.append(random.randint(1,100))
li = list(set(li))
print(li)
print(100 - len(li))
missingValues(li)