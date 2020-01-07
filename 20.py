"""
This problem was asked by Google.
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
In this example, assume nodes with the same value are the exact same node objects.
Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

"""
class Node:
    def __init__(self, val=None):
        self.val = val
        self.nextnode = None
class SLinkedList:
    def __init__(self):
        self.headnode = None

    def printLinkedList(self):
        node=self.headnode
        while node != None:
            print(node.val)
            node = node.nextnode

    def getList(self):
        l=[]
        node=self.headnode
        while node != None:
            l.append(node.val)
            node = node.nextnode
        return l
    def getDict(self):
        d={}
        node=self.headnode
        while node.nextnode != None:
            d[node.val]= node.nextnode.val
            node = node.nextnode
        return d


    def addNode(self, newNode,index):
        count = 0
        curNode=self.headnode
        while curNode != None:
            count = count + 1
             
            if index == 0:
                if newNode.nextnode == None or newNode.nextnode == curNode.nextnode:
                    newNode.nextnode = curNode
                    self.headnode = newNode
                else:
                    print("error the node value inserted is not correct")
                    break
            elif index > 0 and index == count:
                if newNode.nextnode == None or newNode.nextnode == curNode.nextnode:
                    newNode.nextnode = curNode.nextnode
                    curNode.nextnode = newNode  
                else:
                    print("error the node value inserted is not correct")
                    break
            
            curNode = curNode.nextnode
            

#adding nodes examples
linkedList = SLinkedList()
linkedList.headnode= Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
linkedList.headnode.nextnode = e2
e2.nextnode = e3
linkedList.printLinkedList()
linkedList.addNode(Node("add"),2)
print(linkedList.getDict())
#################################################################################################################



A = {3:7, 7:8, 8:10}
B = {99:1, 1:8, 8:10}
def getIntersectingNode(A,B): #complexity: O(n^2)
    for k1,v1 in A.items():
        for k2, v2 in B.items():
            if k1 == k2 and v1 == v2:
                return k1
# print(getIntersectingNode(A,B))

def getIntersectingNode(A,B): #xomplexity: O(n + m) n from creating the hash table
    for x in A:
        if B.get(x) != None:
            print(x)
getIntersectingNode(A,B)