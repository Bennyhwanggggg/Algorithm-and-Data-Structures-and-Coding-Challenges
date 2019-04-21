// Check if a graph has a cycle using depth first search. By Benny Hwang Feb 2018

#include "Graph.h"
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


bool dfsCycleCheck(Graph g, int nV, bool visited[], Vertex v, Vertex u, int pathLen){
	visited[v] = true;
	Vertex w;
	for(w=0; w<nV; w++){
		if(adjacent(g, v,w)){
			if(!visited[w]){
				pathLen++;
				return dfsCycleCheck(g, nV, visited, w, u, pathLen);
			} else if(w!=u && pathLen>1){ // Cycles need to be at least a triangle
				return true;
			}
		}
	}	
	return false;
}

bool hasCycle(Graph g, int nV){
	bool visited[nV];
	Vertex v;
	for(v=0; v<nV; v++){
		visited[v] = false;
	}
	for(v=0; v<nV; v++){
		if(!visited[v]){
			if (dfsCycleCheck(g, nV, visited, v, v, 0)){
				return true;
			}
		}
	}
	return false;
}

int main(void){
	int nV;
	Edge e;
	printf("Enter the number of vertices: ");
	scanf("%d",&nV);

	Graph g = newGraph(nV);	

	printf("Enter an edge (from): ");
	while(scanf("%d", &e.v)){
		printf("Enter an edge (to): ");
		scanf("%d", &e.w);
		insertEdge(g, e);
		printf("Enter an edge (from): ");
	}

	showGraph(g);

	if(hasCycle(g, nV)){
		printf("Cycle found\n");
	} else {
		printf("Cycle not found\n");
	}	

	freeGraph(g);
	return EXIT_SUCCESS;
}
