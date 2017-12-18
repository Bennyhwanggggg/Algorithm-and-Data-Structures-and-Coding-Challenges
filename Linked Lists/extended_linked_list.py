# Written by Benny Hwang 21/09/2017

from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def rearrange(self):
        
        if not self.head or not self.head.next_node:
            return
        
        current_node = None
        previous_node = self.head
        tail = None

        if previous_node.value%2:
            tail = self.head
            current_node = previous_node.next_node
        else:
            while previous_node.next_node:
                
                if previous_node.next_node.value%2:
                    tail = previous_node.next_node
                    previous_node.next_node = tail.next_node
                    tail.next_node = self.head
                    self.head = tail
                    current_node = previous_node.next_node
                    break
                previous_node = previous_node.next_node


        while current_node:
            if current_node.value%2:
                previous_node.next_node = current_node.next_node
                current_node.next_node = tail.next_node
                tail.next_node = current_node
                
                if previous_node is tail:
                    previous_node = current_node
                    tail = current_node
                    current_node = current_node.next_node
                else:
                    tail = current_node
                    current_node = previous_node.next_node
            else:
                previous_node = current_node
                current_node = current_node.next_node

        
    
    

