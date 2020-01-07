"""
   This problem was asked by Twitter.
You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, 
with the following API:
•	record(order_id): adds the order_id to the log
•	get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
 
    
"""
class data():
    def __init__(self, l):
        self.l = l
    
    def record(self,order_id):
        self.l.append(order_id)
    
    def get_last(self, i):
        index = len(self.l) - i
        if 0 <= index < len(self.l):
            return self.l[index]
        else:
            return -1
    
test = data([])
test.record(3)
test.record(4)
test.record(1)
print(test.get_last(0))