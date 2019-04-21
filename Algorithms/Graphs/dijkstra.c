// Dijkstra path search algorithm using queue

// By Benny Hwang Feb 2018

#include <stdlib.h>
#include <stdio.h>
#include "WGraph.h"
#include <limits.h>

#define MAX_NODES 1000

typedef struct {
	Vertex item[MAX_NODES];
	int length;
} PQueueT;

PQueueT PQueue;

void PQueueInit(){
	PQueue.length = 0;
}

void joinPQueue(Vertex v){
	Vertex i;
	for(i=0; i<PQueue.length; i++){
		if(PQueue.item[i] == v){
			return;
		}
	}
	PQueue.item[PQueue.length] = v;
	PQueue.length++;
}

Vertex leavePQueue(int priority[]){
	int i, bestIndex, highest_priority = INT_MAX;
	Vertex bestVertex;
	for(i=0; i<PQueue.length; i++){
		if(priority[PQueue.item[i]] < highest_priority){
			highest_priority = priority[PQueue.item[i]];
			bestIndex = i;
			bestVertex = PQueue.item[i];
		}
	}

	PQueue.length --;
	PQueue.item[bestIndex] = PQueue.item[PQueue.length];
	
	return bestVertex;
}

int isPQueueEmpty(){
	return (PQueue.length == 0);
}

void showPath(Vertex src, int pred[]){
	if(pred[src] == -1){
		printf("%d", src);
	} else {
		showPath(pred[src], pred);
		printf("-%d", src);
	}
}

void dijkstrasssP(Graph g, int nV, Vertex src, Vertex dest){
	int dist[nV];
	int vSet[nV];
	int pred[nV];
	
	int s, t;
	PQueueInit();
	for(s=0; s<nV; s++){
		joinPQueue(s);
		dist[s] = INT_MAX;
		vSet[s] = 1;
		pred[s] = -1;
	}
	dist[src] = 0;
	while(!isPQueueEmpty()){
		s = leavePQueue(dist);
		vSet[s] = 0;
		for(t=0; t<nV; t++){
			if(vSet[t]){
				int weight = adjacent(g, s, t);
				if(weight > 0 && dist[s]+weight < dist[t]){
					dist[t] = dist[s]+weight;
					pred[t] = s;
				}
			}
		}
	}
	// Show all possible path
	/*
	for(s=0; s<nV; s++){
		printf("%d: ", s);
		if(dist[s] < INT_MAX){
			printf("distance = %d, shortest path: ", dist[s]);
			showPath(s, pred);
			putchar('\n');
		} else {
			printf("no path\n");
		}
	}
	*/
	// Just show path from src to dest
	printf("%d: ", dest);
	if(dist[dest] < INT_MAX){
		printf("distance = %d, shortest path: ", dist[dest]);
		showPath(s, pred);
		putchar('\n');
	} else {
		printf("no path\n");
	}
}



int main(void){
	
	int nV;
	Edge e;
	printf("Enter number of vertices: ");
	scanf("%d", &nV);

	Graph g = newGraph(nV);
	Vertex src, dest;
	printf("Enter source node: ");
	scanf("%d", &src);
	printf("Enter destination node: ");
	scanf("%d", &dest);
	printf("Enter edge (from): ");
	while(scanf("%d", &e.v)){
		printf("Enter edge (to): ");
		scanf("%d", &e.w);
		printf("Enter cost of edge: ");
		scanf("%d", &e.weight);
		insertEdge(g, e);
		printf("Enter edge (from): ");
	}

	showGraph(g);

	dijkstrasssP(g, nV, src, dest);	
	freeGraph(g);
	return EXIT_SUCCESS;
}	
