"""
This problem was asked by Facebook.
Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

concept:
Reservoir sampling is a family of randomized algorithms for randomly choosing k samples from a list of n items, 
where n is either a very large or unknown number. Typically n is large enough that the list doesn’t fit into main memory. 
For example, a list of search queries in Google and Facebook.
"""
import random
stream = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]; 
n = len(stream); #unknown

def random_num(stream, k):
    #list cannot fit into memory
    res = stream[:k]
    i=k
    while True:
        try:
            index = random.randint(0,i) #for i =n, p(k selected)= k/n
            if index < k:               # [
                res[index] = stream[i]
        except:
            print("This is the end of the line")
            return res
        finally:
            i = i + 1
    
print(random_num(stream,2))

"""
Algorithm explanation
To simplify the proof, let us first consider the last item. The probability that the last item is in final reservoir = 
The probability that one of the first k indexes is picked for last item = k/n 
(the probability of picking one of the k items from a list of size n)

Let us now consider the second last item. The probability that the second last item is in final reservoir[] 
= [Probability that one of the first k indexes is picked in iteration for stream[n-2]] 
    X [Probability that the index picked in iteration for stream[n-1] is not same as index picked for stream[n-2] ] 
= [k/(n-1)]*[(n-1)/n] = k/n.


For first k stream items, i.e., for stream[i] where 0 <= i < k
The first k items are initially copied to reservoir[] and may be removed later in iterations for stream[k] to stream[n].
The probability that an item from stream[0..k-1] is in final array = Probability that the item is not picked when items stream[k],
stream[k+1], …. stream[n-1] are considered = [k/(k+1)] x [(k+1)/(k+2)] x [(k+2)/(k+3)] x … x [(n-1)/n] = k/n
"""