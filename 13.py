"""
This problem was asked by Amazon.
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

"""
def longestSubstring(k,s):
    #Assume that there is always a longest string
    longeststr=""
    for i in range(len(s)-k):
        length = k
        while True:
            if i + length > len(s):
                break
            if len(set(s[i:i+ length])) ==k:
                length = length + 1
            else:
                break

        length = length - 1
        if len(s[i:i+ length]) > len(longeststr):
            longeststr = s[i:i+ length]
        
    return longeststr
        
s = "abcbadsf"
k = 2
print(longestSubstring(k,s))
