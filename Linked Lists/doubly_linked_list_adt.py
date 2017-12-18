'''
Written by Benny Hwang 13/10/2017

 A Doubly Linked List abstract data type
'''

from copy import deepcopy

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next_node = None
        self.previous_node = None

class DoublyLinkedList:
    # Creates an empty list or a list built from a subscriptable object,
        the key of each value being by default the value itself.
    def  __init__(self, L = None, key = lambda x: x):
        self.key = key
        if L is None:
            self.head = None
            self.tail = None
            return
        if not len(L[: 1]):
            self.head = None
            self.tail = None
            return
        node = Node(L[0])
        self.head = node
        for e in L[1: ]:
            node.next_node = Node(e)
            node.next_node.previous_node = node
            node = node.next_node
        self.tail = node

    def print_from_head_to_tail(self, separator = ', '):
        if not self.head:
            return
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(str(current_node.value))
            current_node = current_node.next_node

        print(separator.join(nodes))
    
    def print_from_tail_to_head(self, separator = ', '):
        if not self.head:
            return
        nodes = []
        current_node = self.tail
        while current_node:
            nodes.append(str(current_node.value))
            current_node = current_node.previous_node

        print(separator.join(nodes))
        

    def duplicate(self):
        if not self.head:
            return
        current_node = self.head
        # Deepcopy the value and create a new node with the same value
        copied_node = Node(deepcopy(current_node.value))
        # Create a new doublylinkedlist object with the same keys
        L = DoublyLinkedList(key = self.key)
        # insert the copied node as the head and tail
        L.head = copied_node
        L.tail = copied_node

        # Since the head node is already copied, we can move on to the next one
        current_node = current_node.next_node

        while current_node:
                # link the copied_node's next_node to the current_node
                # We cannot simply link the object like we did previously, we have to deepy copy and
                # create a new node everytime and link it to the copy
            copied_node.next_node = Node(deepcopy(current_node.value))
            # link in other direction
            copied_node.next_node.previous_node = copied_node
            # If at end of the list, set the tail
            if not current_node.next_node:
                L.tail = copied_node.next_node
            # move copied_node position
            copied_node = copied_node.next_node
            # move current
            current_node = current_node.next_node
        return L
            
                

    def __len__(self):
        if not self.head:
            return 0
        length = 0
        current_node = self.head
        while current_node:
            length += 1
            current_node = current_node.next_node
        return length

    def apply_function(self, function):
        if not self.head:
            return
        current_node = self.head
        while current_node:
            current_node.value = function(current_node.value)
            current_node = current_node.next_node
            

    def is_sorted(self):
        if not self.head or (self.head is self.tail):
            return True
        current_node = self.head
        while current_node:
            if current_node.next_node:
                node = current_node.next_node
                while node:
                    # Need to take the function applied into consideration
                    if self.key(node.value) < self.key(current_node.value):
                        return False
                    node = node.next_node
            current_node = current_node.next_node
        return True

    def extend(self, LL):
        # If initial list is empty, the new list becomes THE list
        if not self.head:
            self.head = LL.head
            self.tail = LL.tail
            return
        if LL.head:
            # connect the initial tail to LL's head
            self.tail.next_node = LL.head
            # connect in reverse direction
            self.tail.next_node.previous_node = self.tail
            # Set new tail
            self.tail = LL.tail
            

    def reverse(self):
        if not self.head or (self.head is self.tail):
            return
        # We need to change the tail to head and then head to tail then reverse the links
        # move the head pointer to tail
        self.tail = self.head
        # store the initial second node into node
        node = self.head.next_node
        # delink the initial head and its next node
        self.head.next_node = None

        while node:
            # store the next node
            next_node = node.next_node
            # remove the link to previous node
            node.previous_node = None
            # reverse the link such that the previous node becomes the next node
            # We can use head since it is still pointing at the previous node
            node.next_node = self.head
            # rebuild the reverse link (This is equivalent to using self.head as the pointer e.g self.head.previous_node = node
            node.next_node.previous_node = node
            # move head pointer
            self.head = node
            # move node pointer using the previously stored next node pointer
            node = next_node
                  

    def index_of_value(self, value):
        if not self.head:
            return -1
        current_node = self.head
        index = 0
        while current_node:
            if current_node.value == value:
                return index
            index += 1
            current_node = current_node.next_node
        return -1
    

    def value_at(self, index):
        if not self.head:
            return
        if index < 0:
            return
        current_node = self.head
        while current_node:
            if not index:
                return current_node.value
            current_node = current_node.next_node
            index-=1
        return

    def prepend(self, LL):
        if not self.head:
            self.head = LL.head
            self.tail = LL.tail
            return
        # Need to link the self.head to LL's tail and then set LL's head as self.head
        self.head.previous_node = LL.tail
        LL.tail.next_node = self.head
        self.head = LL.head
        
            
    def append(self, value):
        # create new node with the desired value
        new_node = Node(value)
        # if list is empty, make the new node the list
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        # Attach the new node to the current tail
        self.tail.next_node = new_node
        # link in reverse direction
        self.tail.next_node.previous_node = self.tail
        # make new tial
        self.tail = self.tail.next_node

    def insert_value_at(self, value, index):
        node_to_insert = Node(value)

        if not self.head:
            self.head = node_to_insert
            self.tail = node_to_insert
            return

        # Special case when inserting at the start of the list
        if index <= 0:
            node_to_insert.next_node = self.head
            self.head.previous_node = node_to_insert
            self.head = node_to_insert
            return

        current_node = self.head
        # move to either the end of the list or the desired index
        while current_node and index:
            current_node = current_node.next_node
            index -= 1
           #****** the solution moves to a spot just before the insert position. Idea is the same 
        # if we are not at end of the list
        # when inserting, we push the original node back
        if current_node:
            node = current_node
            prev_node = current_node.previous_node
            current_node = node_to_insert
            current_node.previous_node = prev_node
            current_node.previous_node.next_node = current_node
            current_node.next_node = node
            current_node.next_node.previous_node = current_node
        else:
            # append
            self.tail.next_node = node_to_insert
            node_to_insert.previous_node = self.tail
            self.tail = node_to_insert

    def insert_value_before(self, value_1, value_2):
        # Insert value 1 before value 2 if value 2 is in the list
        current_node = self.head
        while current_node:
            if current_node.value == value_2:
                new_node = Node(value_1)
                # Special case if inserting at the start
                if current_node is self.head:
                    self.head.previous_node = new_node
                    new_node.next_node = self.head
                    self.head = new_node
                    return True

                prev_node = current_node.previous_node
                next_node = current_node
                current_node = new_node
                current_node.next_node = next_node
                current_node.next_node.previous_node = current_node
                current_node.previous_node = prev_node
                current_node.previous_node.next_node = current_node
                return True
            current_node = current_node.next_node
        return False

    def insert_value_after(self, value_1, value_2):
        # Find value 2 and insert value 1 after it
        current_node = self.head
        while current_node:
            # If value 2 node found
            if current_node.value == value_2:
                # Create new node with value as value 1
                new_node = Node(value_1)
                # Insert the new node behind the current node
                # If not at end of the list
                if current_node.next_node:
                    # save current next node
                    next_node = current_node.next_node
                    # relink current nodes next node to new node
                    current_node.next_node = new_node
                    # create reverse link
                    new_node.previous_node = current_node
                    # link new_node's next node to the original next node
                    new_node.next_node = next_node
                    next_node.previous_node = new_node
                    
                # if not at end of the list
                else:
                    current_node.next_node = new_node
                    new_node.previous_node = current_node
                    self.tail = new_node
                return True
            current_node = current_node.next_node
        return False
                

    def insert_sorted_value(self, value):
        # Insert a value at appropriate location. Assume initial list is alread sorted
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        current_node = self.head
        while current_node:
            # we want to find the position where the current node is larger than the inserted node
            # and insert the new node before this current node
            if self.key(current_node.value) >= self.key(new_node.value):
                self.insert_value_before(new_node.value, current_node.value)
                return
            
            current_node = current_node.next_node
            
        
        self.tail.next_node = new_node
        new_node.previous_node = self.tail
        self.tail = new_node
                

    def delete_value(self, value):
        # If no list, nothing to delete from
        if not self.head:
            return False

        # Special case when the value we wnat to delete is at the start of the list
        if value == self.head.value:
            # Change the head pointer to the next node and remove this one
            # If not the only item in the list
            if self.head.next_node:
                self.head = self.head.next_node
                # remove the link
                
                self.head.previous_node = None
            else:
                self.head = None
                self.tail = None
            return True
            
        current_node = self.head
        
        while current_node:
            if value == current_node.value:
                # If not at end of the list
                if current_node.next_node:
                    # store the previous_node and the next one
                    previous_node = current_node.previous_node
                    next_node = current_node.next_node
                    # link the previous_node and the next node
                    previous_node.next_node = next_node
                    next_node.previous_node = previous_node
                else:
                    # store the previous_node and the next one
                    previous_node = current_node.previous_node
                    current_node.previous_node = None
                    previous_node.next_node = None
                    self.tail = previous_node
                return True
            current_node = current_node.next_node
        return False
                
