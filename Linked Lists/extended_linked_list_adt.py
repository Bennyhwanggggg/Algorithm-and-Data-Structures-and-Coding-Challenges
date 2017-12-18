'''
Written by Benny Hwang 12/09/2017

 Extends the module, linked_list_adt by adding a remove duplicate value feature
'''

from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        # The super keyword allows it to inherit the class used in the argumet (LinkedList) in this case
        super().__init__(L)
        
    def remove_duplicates(self):

        # If empty list, return
        if not self.head:
            return
        # Start from head
        current_node = self.head
        
        # set a node and move through the list comparing each node to the current node
        while current_node:
            # node to compare
            node = current_node
            while node.next_node:
                # If a duplicate is found
                if node.next_node.value == current_node.value:
                    # delink the next node and connect the next next node
                    node.next_node = node.next_node.next_node
                else:
                    node = node.next_node
            current_node = current_node.next_node
                    


