// DLList.h - Interface to doubly-linked list ADT
// Written by John Shepherd, March 2013
// Last modified, Benny Hwang, December 2017 

#ifndef DLLIST_H
#define DLLIST_H

#include <stdio.h>
#include "DLList.h"

// External view of DLList
// Implementation given in DLList.c
// Implements a DLList of integers 

typedef struct DLListRep *DLList;

// create a new empty DLList
DLList newDLList();

// free up all space associated with list
void freeDLList(DLList);

// display items from a DLList, comma separated
void showDLList(DLList L);

// return item at current position
int DLListCurrent(DLList);

// move current position (+ve forward, -ve backward)
// return 1 if reach end of list during move
int DLListMove(DLList, int);

// move to specified position in list
// i'th node, assuming first node has i==1
int DLListMoveTo(DLList, int);

// insert an item before current item
// new item becomes current item
void DLListBefore(DLList, int);

// insert an item after current item
// new item becomes current item
void DLListAfter(DLList, int);

// delete current item
// new item becomes item following current
// if current was last, current becomes new last
// if current was only item, current becomes null
void DLListDelete(DLList);

// return number of elements in a list
int DLListLength(DLList);

// is the list empty?
int DLListIsEmpty(DLList);

#endif
