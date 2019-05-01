// Binary Search Tree ADT interface ... COMP9024 17s2

// Modified by Benny Hwang Feb 2018

#include <stdbool.h>

typedef int Item;      // item is just a key

typedef struct Node *Tree;

Tree newTree();        // create an empty Tree
void freeTree(Tree);   // free memory associated with Tree
void showTree(Tree);   // display a Tree (sideways)

bool TreeSearch(Tree, Item);   // check whether an item is in a Tree
int  TreeHeight(Tree);         // compute height of Tree
int  TreeNumNodes(Tree);       // count #nodes in Tree
Tree TreeInsert(Tree, Item);   // insert a new item into a Tree
Tree TreeDelete(Tree, Item);   // delete an item from a Tree

// internal functions made visible for testing
Tree rotateRight(Tree);
Tree rotateLeft(Tree);
Tree insertAtRoot(Tree, Item);
Tree partition(Tree, int);
Tree rebalance(Tree);

void preOrder(Tree);
void inOrder(Tree);
void postOrder(Tree);

int countNodes(Tree);
int isBST(Tree);
int isAVL(Tree);
int countInRange(Tree, int, int);
Tree AddHeightToAll(Tree);
int sumInRange(Tree, int, int);
