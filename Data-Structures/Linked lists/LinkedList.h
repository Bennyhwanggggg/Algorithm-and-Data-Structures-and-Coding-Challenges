// Singly Linked List ADT Interface
// Written By Benny Hwang Jan 2018

#ifndef LINKEDLIST_H
#define LINKEDLIST_H

#include <stdio.h>

typedef struct LListRep *LList;

typedef struct node *NodeT;

NodeT makeNode(int);
LList newLList();
void freeLL(LList);
void showLL(LList);
LList append(LList, int val);
LList appendNode(LList, NodeT);
LList deleteHead(LList);
LList deleteTail(LList);
LList deleteByVal(LList, int);
int searchNodeID(LList, int);
int lenLL(LList);
void changeNodeData(LList, int, int);

NodeT getHead(LList);
NodeT getNext(NodeT);
NodeT getTail(LList);
NodeT copyNode(NodeT);

void swapNodes(LList, NodeT, NodeT);
void sortedInsert(LList, NodeT, int);
LList insertionSort(LList, int);

#endif