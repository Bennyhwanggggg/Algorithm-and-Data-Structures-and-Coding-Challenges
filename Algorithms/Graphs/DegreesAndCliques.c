/*
Graph Analyser

- Ask user to create a graph
- computes and output the minimum and maximum degree of vertices in the graph.
- prints all vertices of minium degree and maximum degree in the graph
- Display all 3 cliques in the graph

By Benny Hwang 07/01/2018
*/

#include <stdio.h>
#include <stdlib.h>
#include "Graph.h"

#define MAXNODES 1000

void MinMaxDegree(Graph g, int nV){
	int max = 0, min = nV-1;
	Vertex v, w;
	int degree[MAXNODES];
	for(v=0; v<nV; v++){
		degree[v] = 0;
		for(w=0; w<nV; w++){
			if(adjacent(g,v,w)){
				degree[v]++;
			}
		}
		if(degree[v]>max){
			max = degree[v];
		} 
		if (degree[v]<min) {
			min = degree[v];
		}
	}

	printf("Min degree is %d\n", min);
	printf("Max degree is %d\n", max);
	
	printf("Nodes of minimum degree:\n");
	for(v=0; v<nV; v++){
		if(degree[v] == min){
			printf("%d\n",v);
		}
	}
	printf("Nodes of maximum degree:\n");
	for(v=0; v<nV; v++){
		if(degree[v] == max){
			printf("%d\n",v);
		}
	}
}
			
void show3Cliques(Graph g, int nV){
	Vertex v, w, u;
	printf("Triangles:\n");
	for(v=0; v<nV-3; v++){
		for(w=0; w<nV-2; w++){
			if(adjacent(g,v,w)){
				for(u=0; u<nV; u++){
					if(adjacent(g,v,u) && adjacent(g,w,u)){
						printf("%d-%d-%d\n",v,w,u);
					}
				}
			}
		}
	}
}




int main(void){
	int nV;
	printf("Enter the number of vertices: " );
	scanf("%d",&nV);
	
	Edge e;
	Graph g = newGraph(nV);

	printf("Enter an edge (from): ");
	while(scanf("%d",&e.v)){
		printf("Enter an edge (to): ");
		scanf("%d",&e.w);
		insertEdge(g,e);
		printf("Enter an edge (from): ");
	}
	printf("Finished\n");
	MinMaxDegree(g,nV);
	show3Cliques(g,nV);
	freeGraph(g);
	return 0;
}













