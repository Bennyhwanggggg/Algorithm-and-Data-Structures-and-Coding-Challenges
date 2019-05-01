// Queue ADO implementation ... by Benny Hwang Dec 2017

#include "intQueue.h"
#include <assert.h> // assert is used to check for situations that cannot happen; If it does happen, process is aborted and an error message will be printed.

#define MAXITEMS 10

static struct {
	int item[MAXITEMS];
	int first;
} queueObject; // define the Data Object

void QueueInit(){
	queueObject.first = -1;
}	// set up empty queue

int QueueIsEmpty(){
	return (queueObject.first < 0)	//return a boolean 1 or 0 (true or false), whether there is any item in the queue
}

// The front of the queue is actually the last element and first element is the end of the queue
// Therefore, we want to increase the last element index and move everything up, then
// the first index will become empty for us to insert the new value
void QueueEnqueue(int n){ // insert int at end of the queue
	assert(queueObject.first < MAXITEMS-1); // Make sure queue is not oversized
	queueObject.first++;
	int i = queueObject.first;
	// When we add something to the queue, we need to move everything up
	for(i=queueObject.first; i>0; i--){
		queueObject.item[i] = queueObject.itemp[i-1];	//move all element up.
	}
	queueObject.item[0] = n;	// add the element at end of the queue
}

int QueueDequeue(){	// remove int from front of the queue
	assert(queueObject.first >=-1);	// Make sure not an empty queue
	int i = queueObject.first;	// get the first element index
	int n = queueObject.item[i]; //get the firzt element in queue
	queueObject.first--;	// change pointer of first to the second element in the queue
	return n;
}