def num_ways(n):
    #base case
    if n == 0 or n ==1:
        return 1
    else:
        return num_ways(n-1) + nu,_ways(n-2)
    #bottom up approach
def num_ways_bottomup(n): #x=[1,2]
    if n == 0 or n ==1:
        return 1
    else:
        nums = {}
        nums[0]= 1
        nums[1]=1
        for i in range(2,n+1):
            nums[i] = nums[i-1] + nums[i-2]
        return nums[n]

print(num_ways_bottomup(4))

def num_ways_x(n):
    if n ==0:
        return 1
    else:
        total = 0
        for i in [1,3,5]:
            if n-i >=0:
                total = total + num_ways_x(n-i)
        return total
print(num_ways_x(4))

def num_ways_x_bottomup(n): #x=[1,3,5]
    if n == 0:
        return 1
    else:
        nums = {}
        nums[0]= 1
        for i in range(1,n+1):
            total = 0
            for j in [1,3,5]:
                if i-j >=0:
                    total = total + num_ways_x_bottomup(i-j)
            nums[i]=total
        return nums[n]
print(num_ways_x_bottomup(4))