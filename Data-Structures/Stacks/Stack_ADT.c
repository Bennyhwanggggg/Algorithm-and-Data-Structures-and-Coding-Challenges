/* 
Linked list implementation of integer stack

By Benny Hwang 30/12/2017
*/

#include <stdlib.h>
#include <assert.h>
#include "Stack_ADT.h"

// set up node structure
typedef struct node{
	int data;
	struct node *next;
} NodeT;

// create overall stack structure
typedef struct StackRep{
	int height;	// number of elements in the stack
	NodeT *top;	// pointer to the top of the stack
} StackRep;

// set up emoty stack
stack newStack(){
	stack new = malloc(sizeof(StackRep));
	new->height = 0;
	new->top = NULL;
	return new;
}

// remove the whole stack
void dropStack(stack S){
	NodeT *curr = S->top;
	// free the list
	while(curr != NULL){
		NodeT *temp = curr->next;
		free(curr);
		curr = temp;
	}
	// free the stackRep
	free(S);
}

// check whether stack is empty
int StackIsEmpty(stack S){
	return(S->height == 0);
}

void StackPush(stack S, int v){
	NodeT *new = malloc(sizeof(NodeT));
	assert(new!=NULL);
	new->data = v;
	new->next = S->top;	// insert new element
	S->top = new;		// set new element as top
	S->height ++;		// Update height
}

int StackPop(stack S){
	assert(S->height > 0);
	NodeT *head = S->top;
	S->top = S->top->next;
	S->height --;
	int d = head->data;
	free(head);
	return d;

}