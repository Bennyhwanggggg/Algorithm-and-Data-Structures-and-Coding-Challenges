/*
Write a C program that computes the connected components in a graph.

By Benny Hwang 06/01/2018
*/

#include "Graph.h"
#include <stdio.h>
#include <stdlib.h>

#define MAXNODE 1000

int componentOf[MAXNODE];

void dfsComponents(Graph g,Vertex v,int id, int nV);

void components(Graph g,int nV){
	
	int i;
	for(i=0; i<nV; i++){
		componentOf[i] = -1;
	}
	int compID = 0;
	for(i=0; i<nV; i++){
		if(componentOf[i] == -1){
			dfsComponents(g,i,compID,nV);
			compID++;
		}
	}

	printf("Number of components: %d\n", compID);
	for(i=1; i<=compID; i++){
		printf("Component %d:\n",i);
		for(int j=0; j<nV; j++){
			if(componentOf[j] == i-1){
				printf("%d\n",j);
			}
		}
	}

}

void dfsComponents(Graph g,Vertex v,int id, int nV){
	componentOf[v] = id;
	Vertex i;
	for(i=0; i<nV; i++){
		if(i!=v && adjacent(g,v,i) && componentOf[i] == -1){
			dfsComponents(g,i,id,nV);
		}
	}
}


int main(void){
	int n;
	Edge e;
	printf("Enter the number of vertices: ");
	scanf("%d",&n);
	
	Graph g = newGraph(n);
	int i = 0;
	printf("Enter an edge (from): ");
	while(scanf("%d",&e.v) && (i <= n)){
		printf("Enter an edge (to): ");
		scanf("%d",&e.w);
		insertEdge(g,e);
		i++;
		printf("Enter an edge (from): ");
	}
	printf("Finished\n");
	components(g,n);
	showGraph(g);
	return 0;
}
