// Binary Search Tree ADT implementation ... COMP9024 17s2
// Modified by Benny Hwang Feb 2018
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "BSTree.h"
#include <limits.h>

#define data(tree)  ((tree)->data)
#define left(tree)  ((tree)->left)
#define right(tree) ((tree)->right)

typedef struct Node {
   int  data;
   Tree left, right;
} Node;

// make a new node containing data
Tree newNode(Item it) {
   Tree new = malloc(sizeof(Node));
   assert(new != NULL);
   data(new) = it;
   left(new) = right(new) = NULL;
   return new;
}

// create a new empty Tree
Tree newTree() {
   return NULL;
}

// free memory associated with Tree
void freeTree(Tree t) {
   if (t != NULL) {
      freeTree(left(t));
      freeTree(right(t));
      free(t);
   }
}

// display Tree sideways
void showTreeR(Tree t, int depth) {
   if (t != NULL) {
      showTreeR(right(t), depth+1);
      int i;
      for (i = 0; i < depth; i++)
	 putchar('\t');            // TAB character
      printf("%d\n", data(t));
      showTreeR(left(t), depth+1);
   }
}

void showTree(Tree t) {
   showTreeR(t, 0);
}

// compute height of Tree
int TreeHeight(Tree t) {
    if(t==NULL){
	return -1;
    }
    int lh = 1+TreeHeight(left(t));
    int rh = 1+TreeHeight(right(t));
    return lh < rh ? rh:lh;
}

// count #nodes in Tree
int TreeNumNodes(Tree t) {
   if (t == NULL)
      return 0;
   else
      return 1 + TreeNumNodes(left(t)) + TreeNumNodes(right(t));
}

// check whether a key is in a Tree
bool TreeSearch(Tree t, Item it) {
   if (t == NULL)
      return false;
   else if (it < data(t))
      return TreeSearch(left(t), it);
   else if (it > data(t))
      return TreeSearch(right(t), it);
   else                                 // it == data(t)
      return true;
}

// insert a new item into a Tree
Tree TreeInsert(Tree t, Item it) {
   if (t == NULL)
      t = newNode(it);
   else if (it < data(t))
      left(t) = TreeInsert(left(t), it);
   else if (it > data(t))
      right(t) = TreeInsert(right(t), it);
   return t;
}

Tree joinTrees(Tree t1, Tree t2) {
   if (t1 == NULL)
      return t1;
   else if (t2 == NULL)
      return t2;
   else {
      Tree curr = t2;
      Tree parent = NULL;
      while (left(curr) != NULL) {    // find min element in t2
	 parent = curr;
	 curr = left(curr);
      }
      if (parent != NULL) {
	 left(parent) = right(curr);  // unlink min element from parent
	 right(curr) = t2;
      }
      left(curr) = t1;
      return curr;                    // min element is new root
   }
}

// delete an item from a Tree
Tree TreeDelete(Tree t, Item it) {
   if (t != NULL) {
      if (it < data(t))
	 left(t) = TreeDelete(left(t), it);
      else if (it > data(t))
	 right(t) = TreeDelete(right(t), it);
      else {
	 Tree new;
	 if (left(t) == NULL && right(t) == NULL) 
	    new = NULL;
	 else if (left(t) == NULL)    // if only right subtree, make it the new root
	    new = right(t);
	 else if (right(t) == NULL)   // if only left subtree, make it the new root
	    new = left(t);
	 else                         // left(t) != NULL and right(t) != NULL
	    new = joinTrees(left(t), right(t));
	 free(t);
	 t = new;
      }
   }
   return t;
}

Tree rotateRight(Tree n1) {
   if (n1 == NULL || left(n1) == NULL)
      return n1;
   Tree n2 = left(n1);
   left(n1) = right(n2);
   right(n2) = n1;
   return n2;
}

Tree rotateLeft(Tree n2) {
   if (n2 == NULL || right(n2) == NULL)
      return n2;
   Tree n1 = right(n2);
   right(n2) = left(n1);
   left(n1) = n2;
   return n1;
}

Tree insertAtRoot(Tree t, Item it) {
    if(t==NULL){
	t = newNode(it);
    } else if(it > data(t)){
	right(t) = insertAtRoot(right(t), it);
	t = rotateLeft(t);
    } else if(it < data(t)){
	left(t) = insertAtRoot(left(t), it);
	t = rotateRight(t);
    }
    return t;
}

Tree partition(Tree t, int i) {
   if (t != NULL) {
      assert(0 <= i && i < TreeNumNodes(t));
      int m = TreeNumNodes(left(t));
      if (i < m) {
	 left(t) = partition(left(t), i);
	 t = rotateRight(t);
      } else if (i > m) {
	 right(t) = partition(right(t), i-m-1);
	 t = rotateLeft(t);
      }
   }
   return t;
}

Tree rebalance(Tree t) {
   int n = TreeNumNodes(t);
   if (n >= 3) {
      t = partition(t, n/2);           // put node with median key at root
      left(t) = rebalance(left(t));    // then rebalance each subtree
      right(t) = rebalance(right(t));
   }
   return t;
}


void preOrder(Tree t){
	if(t==NULL){
		return;
	} 
	printf("%d ", data(t));
	preOrder(left(t));
	preOrder(right(t));
}
void inOrder(Tree t){
	if(t==NULL){
		return;
	} 	
	inOrder(left(t));
	printf("%d ", data(t));
	inOrder(right(t));
}

void postOrder(Tree t){
	if(t==NULL){
		return;
	} 
	postOrder(left(t));
	postOrder(right(t));
	printf("%d ", data(t));
}


int countNodes(Tree t){
	if(t==NULL){
		return 0;
	}
	return 1+countNodes(left(t))+countNodes(right(t));
}

int isBSTH(Tree t, int min, int max){
	if(t==NULL){
		return 1;
	} else if(data(t)<min || data(t) > max){
		return 0;
	}
	return isBSTH(left(t), min, data(t)-1) && isBSTH(right(t), data(t)+1, max);
}

int isBST(Tree t){
    if(t==NULL){
	return 1;
   }
   return isBSTH(t, INT_MIN, INT_MAX);
}
int isAVL(Tree t){
	if(t==NULL){
		return 1;
	} else if((abs(TreeHeight(left(t))-TreeHeight(right(t)))<=1) && isAVL(left(t)) && isAVL(right(t))){
		return 1;
	}
	return 0;
}
int countInRange(Tree t, int a, int b){
	int n = 0;
	if(t==NULL){
		return 0;
	} else if(a <= data(t) && data(t) <= b){
		n++;
		n+=countInRange(left(t), a, b);
		n+=countInRange(right(t), a, b);
	} else if(b < data(t)){
		n+=countInRange(left(t), a, b);
	} else if(data(t) < a){
		n+=countInRange(right(t), a, b);
	}
	return n;
}
Tree AddHeightToAll(Tree t){
	if(t!=NULL){
		data(t) += TreeHeight(t);
		if(left(t)){
			left(t) = AddHeightToAll(left(t));
		} 
		if(right(t)){
			right(t) = AddHeightToAll(right(t));
		}
	}
	return t;
}

int sumInRange(Tree t, int a, int b){
	int n = 0;
	if(t==NULL){
		return 0;
	} else if(a<data(t) && data(t) <b){
		n += data(t);
		n += sumInRange(left(t), a, b);
		n += sumInRange(right(t), a, b);
	} else if(data(t) <= a){
		n += sumInRange(right(t), a, b);
	} else if(b <= data(t)){
		n += sumInRange(left(t), a, b);
	}
	return n;
}



