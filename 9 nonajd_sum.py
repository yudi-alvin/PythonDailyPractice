"""
This problem was asked by Airbnb.
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
Follow-up: Can you do this in O(N) time and constant space?

"""
def nonadjecent_sum(numbers):#complexity O(n)
    if not numbers:
        return 0

    if len(numbers) <= 2:
        return max(numbers)
	
    with_last = nonadjecent_sum(numbers[:-2]) + numbers[-1]  # sum include last number [5,1,3,1] +5
    without_last = nonadjecent_sum(numbers[:-1])  # sum without last number 
    return max(with_last, without_last)

print(nonadjecent_sum([5, 1, 3, 1, 2, 5]))