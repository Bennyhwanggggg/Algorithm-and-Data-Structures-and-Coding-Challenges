// Stack ADT header file		by Benny Hwang 30/12/2017

#include <stdio.h>

typedef struct StackRep *stack;

stack newStack();		// set up new stack
void dropStack(stack S);	// remove stack
int StackIsEmpty(stack S);	// check whether stack is empty
void StackPush(stack S, int v);	// push an element into the stack
int StackPop(stack S);		// pop an element from stack 


