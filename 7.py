import time
import itertools
import operator
start_time = time.time()
"""
This problem was asked by Facebook.
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.

"""
#O(2^n)
def decode(s):
    k=len(s)
    if k ==0:
        return 1
    if s=="":
        return 0
    #example decode 12345
    # a + decode(2345) and L + decode (345)
    result = decode(s[1:k])
    if (k >=2 and int(s[0:2])<=26):
        result += decode(s[2:k])
    return result



decode("111111111111111111111111111111")
print("--- %s seconds ---" % (time.time() - start_time))
#memoization O(n)
#example decode 1111
    # a + decode(111)                       | k + decode (11)
    # a + decode(11) and k + decode(1)      |2
    # a + decode(1) and k + decode(0)      
    # 1 + 1 + 1
start_time = time.time()
def decode(s, memo=dict()):
    k=len(s)
    if k ==0:
        return 1
    if s=="":
        return 0
    if memo.get(k) != None:
        return memo[k]
    
    result = decode(s[1:k])
    if (k >=2 and int(s[0:2])<=26):
        result += decode(s[2:k])
    memo[k]=result
    return result
print(decode("1234"))
decode("111111111111111111111111111111111111111111111111111111111111111111111111")
print("--- %s seconds ---" % (time.time() - start_time))
