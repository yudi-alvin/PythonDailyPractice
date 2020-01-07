"""
This problem was asked by Facebook.
A builder is looking to build a row of N houses that can be of K different colors. 
He has a goal of minimizing costss while ensuring that no two neighboring houses are of the same color.
Given an N by K matrix where the nth row and kth column represents the costs to build the nth house with kth color, 
return the minimum costs which achieves this goal.

"""
#simple assume k = 3
costs =[[10,20,30],
[20,50,10], 
[80,50,10]]
n=len(costs)
k= len(costs[0])
for i in range(n-1):
    costs[i+1][0] = costs[i+1][0] + min(costs[i][1],costs[i][2])
    costs[i+1][1] = costs[i+1][1] + min(costs[i][0],costs[i][2])
    costs[i+1][2] = costs[i+1][2] + min(costs[i][1],costs[i][0])
   
print(min(costs[-1]))

#################################any k###############################################
#Complexity: O(n^2)
import math
costs =[[10,20,30],
[20,50,10], 
[80,50,10]]
n=len(costs)
k= len(costs[0])
preMin=0
preSecond=0
preMinIndex=-1

for i in range(n):
    currMin=math.inf # make large number
    currSecond = math.inf # make large number
    currMinIndex = 0

    for j in range(k):

        if(preMinIndex==j):#same column as the previous min index, add the previous secondmin instead
            costs[i][j] = costs[i][j] + preSecond
        else:
            costs[i][j] = costs[i][j] + preMin
        
        #update the min and second min
        if(costs[i][j]< currMin):
            currSecond = currMin
            currMin=costs[i][j]
            currMinIndex = j
        elif(costs[i][j]<currSecond ):
            currSecond = costs[i][j]
    
    preMin=currMin
    preSecond=currSecond
    preMinIndex =currMinIndex

print(currMin)
