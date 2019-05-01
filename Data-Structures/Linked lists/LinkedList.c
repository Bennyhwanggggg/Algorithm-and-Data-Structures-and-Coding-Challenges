/*
Singly Linked List Implementation 
Weitten by Benny Hwang Jan 2018
*/

#include <stdlib.h>
#include <assert.h>
#include <stdio.h>
#include <string.h>
#include "LinkedList.h"


// Initialise a self-referential type for the linked list structure
//typedef struct node{
struct node{
	int data;
	NodeT next;
};

// Linked list representaiton.
//typedef struct LListRep {
struct LListRep {
	int nitems;		// count of items in list
	NodeT head;	// head node
	NodeT tail;	// last node
} LListRep;

// Create a node
NodeT makeNode(int val){
	NodeT new = malloc(sizeof(struct node));
	assert(new!=NULL);
	new->data = val;
	new->next = NULL;
	return new;
}

// Create a new empty LList.
LList newLList(){
	LList new = malloc(sizeof(struct LListRep));
	assert(new != NULL);
	new->nitems = 0;
	new->head = NULL;
	new->tail = NULL;
	return new;
}

// free the whole linked list from memory
void freeLL(LList L){
	assert(L != NULL);

	NodeT current = L->head;
	NodeT temp;
	while(current!=NULL){
		temp = current->next;
		free(current);
		current = temp;
	}
	free(L);
}

// show the whole linked list
void showLL(LList L){
	if(L == NULL){
		return;
	}
	NodeT curr;
	for(curr = L->head; curr != NULL; curr = curr->next){
		printf("%d ", curr->data);
		if(curr->next != NULL){
			printf(" -> ");
		}
	}
	putchar('\n');
}

// Append a url to the end of the linked list by creating a new node and appending that node.
// Input: Linked list, url string.
LList append(LList L, int val){
	NodeT new = makeNode(val);	// give new node ID of the last number
	assert(new != NULL);
	if(L->head == NULL){ // If the linked list is currently empty, new node becomes head and only item
		L->head = new;
		L->tail = new;
		L->nitems++;
	} else { // Otherwise, add to end of the list and set new tail.
		L->tail->next = new;
		L->tail = new;
		L->nitems++;
	}
	return L;
}

// Apend a node to end of the list. Node need to be already created.
LList appendNode(LList L, NodeT new){
	if(new == NULL){
		return L;
	}
	if(L->head == NULL){ // If the linked list is currently empty, new node becomes head and only item
		L->head = new;
		L->tail = new;
		L->nitems++;
	} else { // Otherwise, add to end of the list and set new tail.
		L->tail->next = new;
		L->tail = new;
		L->nitems++;
	}
	return L;
}

// Delete the first node.
LList deleteHead(LList L){
	if(L->head == NULL){
		return L;
	}
	NodeT first = L->head;
	L->head = first->next;
	free(first);
	L->nitems --;
	return L;
}

LList deleteTail(LList L){
	if(L->tail == NULL){
		return L;
	}
	NodeT current = L->head;
	// If only one element
	if(current == L->tail){
		free(current);
	} else {
		NodeT previousToTail, last;
		// move to the second last element
		while(current->next != L->tail){
			current = current->next;
		}
		previousToTail = current;
		last = current->next;
		free(last);
		L->tail = previousToTail;
	}
	L->nitems --;
	return L;
}

LList deleteByVal(LList L, int val){
	if(L==NULL){
		return L;
	} 
	NodeT current = L->head;
	NodeT prev;
	// Traverse through the list and find the data
	while(current->data != val && current->next != NULL){
		prev = current;
		current = current->next;
	}
	// if deleting at the start
	if(current == L->head){
		// If only element in the list and the data doesn't match, just return L
		if(current->data != val){
			return L;
		} else {
			deleteHead(L);
		}
	}

	// if reached the end of the list
	if(current == L->tail){
		// If data not found
		if(current->data != val){
			return L;
		} else {
			return deleteTail(L);
		}
	}

	// if found the data somwhere in the middle of the list
	prev->next = current->next;
	free(current);
	L->nitems --;
	return L;
}

// Find a val in the list, return 1 if exist, otherwise 0
int searchNode(LList L, int val){
	// if L is empty
	if(L==NULL){
		return -1;
	}
	NodeT current = L->head;
	while(current != NULL && current->data != val){
		current = current->next;
	}
	// if node not found
	if(current == NULL){
		return 0;
	}
	return 1;
}


// find a node in the list and change its value
void changeNodeData(LList L, int data, int newData){
	if(L==NULL){
		return;
	}
	NodeT current = L->head;
	while(current != NULL && current->data != val){
		current = current->next;
	}
	// if node not found
	if(current == NULL){
		return;
	}
	current->data = newData;
}

// count numbe rof nodes in the list
int lenLL(LList L){
	return (L->nitems);
}

NodeT copyNode(NodeT toCopy){
	NodeT new = malloc(sizeof(struct node));
	assert(new!=NULL);
	new->data = toCopy->data;
	new->next = NULL;
	return new;
}

// return a list's head node
NodeT getHead(LList L){
	return (L->head);
}

NodeT getNext(NodeT n){
	return (n->next);
}

// return a list's tail node
NodeT getTail(LList L){
	return (L->tail);
}



// swap two nodes in a singly linked list.
void swapNodes(LList L, NodeT n1, NodeT n2){
	if(n1 == n2){
		return;
	}

	// Traverse through the list and find the first node while storing the previous node.
	NodeT prev1, current1 = L->head;
	while(current1 != NULL && current1 != n1){
		prev1 = current1;
		current1 = current1->next;
	}

	// Do the same for the second node
	NodeT prev2, current2 = L->head;
	while(current2 != NULL && current2 != n2){
		prev2 = current2;
		current2 = current2->next;
	}

	// If not both not found, we cannot swap.
	if(current1 == NULL || current2 == NULL){
		return;
	}

	// switch previous nodes link
	// When the node to swap is the head, make it the head. Otherwise, swap normally.
	if(prev1 == NULL){
		L->head = current2;
	} else { 
		prev1->next = current2;
	}

	if(prev2 == NULL){
		L->head = current1;
	} else {
		prev2->next = current1;
	}
	// switch next node link
	NodeT temp = current2->next;
	current2->next = current1->next;
	current1->next = temp;
}

// insert a node at appropriate location based on size of its data
void sortedInsert(LList L, NodeT new, int mode){
	NodeT current = L->head;
	if(mode == 1 || mode == 2){
		if(L->head == NULL || (current->data >= new->data && mode == 1) || (current->data <= new->data && mode == 2)){
			new->next = L->head;
			L->head = new;
		} else {
			// move to the node before location of insert so we can insert new node after it.
			if(mode == 5){
				while(current->next != NULL && current->next->data < new->data){
					current = current->next;
				}
			} else if(mode == 6){
				while(current->next != NULL && current->next->data > new->data){
					current = current->next;
				}
			}
			new->next = current->next;
			current->next = new;
		}
	}
}

// Use insertion sort to sort a singly linked list. Will modify the original.
// mode 1 = ascending order, mode 2 = descending order
LList insertionSort(LList L, int mode){
	assert(L != NULL);
	// Create a new list to put the sorted list in.
	LList sortedList = newLList();
	NodeT current = L->head;
	while(current != NULL){
		NodeT currNext = current->next;	// store next node
		// insert current node into sortedlist
		sortedInsert(sortedList, current, mode);
		current = currNext; // set next node.
	}
	return sortedList;
}


