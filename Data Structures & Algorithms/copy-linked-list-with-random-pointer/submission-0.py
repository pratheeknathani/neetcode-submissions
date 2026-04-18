"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        my_dict = {None: None}

        curr = head
        while curr:
            temp = Node(curr.val) #create a copy of the value
            my_dict[curr] = temp # map the key to the correspond
            curr = curr.next
        
        curr = head
        while curr:
            temp = my_dict[curr]
            temp.next = my_dict[curr.next]
            temp.random = my_dict[curr.random]
            curr = curr.next
    
        return my_dict[head]
