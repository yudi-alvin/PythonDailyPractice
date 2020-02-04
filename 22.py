"""
This problem was asked by Microsoft.
Given a dictionary of words and a string made up of those words (no spaces), 
return the original sentence in a list. If there is more than one possible reconstruction, return any of them. 
If there is no possible reconstruction, then return null.
For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", 
you should return ['the', 'quick', 'brown', 'fox'].
Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", 
return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].


"""
l=['bedbath', 'bed', 'bath', 'and', 'beyond']
s="bedbathandbeyond"

def getSentence(l,s):
    start=0
    res=[]
    for i in range(len(s)+ 1):
        if s[start:i] in l:
            res.append(s[start:i])
            start = i
    if res == []:
        return None
    return res
print(getSentence(l,s))

#more correct
def getSentence(l,s):
    start=0
    res=[]
    while(s):
        for word in l:
            if s.startswith(word):
                res.append(word)
                s = s[len(word):]
    if res == []:
        return None
    return res

print(getSentence(l,s))