"""
In the XOR linked list, instead of storing actual memory addresses, every node stores the XOR of addresses of previous and next nodes.
This problem was asked by Google.
An XOR linked list is a more memory efficient doubly linked list. 
Instead of each node holding next and prev fields, it holds a field named both, 
which is an XOR of the next node and the previous node. Implement an XOR linked list; 
it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.
If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and 
dereference_pointer functions that converts between nodes and memory addresses.

    >>> l = coding_problem_6()
    >>> for cnt in xrange(0, 4):
    ...     l.add(cnt)
    >>> l.get(2) == 2
    True

    Note: python does not have actual pointers (id() exists but it is not an actual pointer in all implementations).
    For this reason, we use a python list to simulate memory. Indexes are the addresses in memory. This has the
    unfortunate consequence that the travel logic needs to reside in the List class rather than the Node one.
    """
def coding_problem_6():
    class XORLinkedListNode(object):

        def __init__(self, val, prev, next):
            self.val = val
            self.both = prev ^ next

        def next_node(self, prev_idx):
            return self.both ^ prev_idx

        def prev_node(self, next_idx):
            return self.both ^ next_idx

    class XORLinkedList(object):

        def __init__(self):
            self.memory = [XORLinkedListNode(None, -1, -1)]

        def head(self):
            return 0, -1, self.memory[0]  # head node index, prev node index, head node

        def add(self, val):
            current_node_index, previous_node_index, current_node = self.head()
            while True:  # walk down the list until we find the end
                next_node_index = current_node.next_node(previous_node_index)
                if next_node_index == -1:  # we reached the end on the list
                    break
                previous_node_index, current_node_index = current_node_index, next_node_index
                current_node = self.memory[next_node_index]

            new_node_index = len(self.memory)  # "allocation"
            current_node.both = previous_node_index ^ new_node_index
            self.memory.append(XORLinkedListNode(val, current_node_index, -1))

        def get(self, index):
            current_index, previous_index, current_node = self.head()
            for cnt in range(index + 1):
                previous_index, current_index = current_index, current_node.next_node(previous_index)
                current_node = self.memory[current_index]
            return current_node.val

    return XORLinkedList()

l = coding_problem_6()
for cnt in range(0, 4):
    l.add(cnt)
print(l.get(6))
