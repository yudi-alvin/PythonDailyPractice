"""
This problem was asked by Twitter.
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, 
return all strings in the set that have s as a q.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

"""

q="de"
l=["dog", "deer", "deal",'able', 'abode', 'about', 'above', 'abuse', 'syzygy']

def autocomplete(q, strList):
    res=[]
    for x in strList:   #O(n)
        if q == x[:len(q)]:
            res.append(x)
    return res

print(autocomplete(q,l))

def autocomplete(q, strList):
    res=[]
    sorted(strList)
    for x in strList:   #O(n)
        if q == x[:len(q)]:
            res.append(x)
        elif q != x[:len(q)] and len(res)!=0:
            break
    return res

print(autocomplete(q,l))

import bisect


def autocomplete(q, strList):

    dictionary = [s.lower() for s in sorted(strList)]
    next_q = q + 'a' if q[-1] == 'z' else q[:-1] + chr(ord(q[-1]) + 1)
    #df
    return dictionary[bisect.bisect_left(dictionary, q):bisect.bisect_left(dictionary, next_q)]

print(autocomplete(q,l))