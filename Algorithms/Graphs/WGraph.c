// Weighted Graph Adjacency Matrix Representation COMP9024 18x1 UNSW

#include "WGraph.h"
#include <stdio.h>
#include <assert.h>
#include <stdlib.h>

typedef struct GraphRep{
	int **edges; // adjacency matrix storing positive weights, // 0 if nodes not adjacent
	int nV;
	int nE;
} GraphRep;

Graph newGraph(int V){
	assert(V >= 0);
	int i;
	
	Graph g = malloc(sizeof(GraphRep));
	assert(g!= NULL);
	g->nV = V;
	g->nE = 0;

	// allocate memory for each row
	g->edges = malloc(V*sizeof(int *));
	assert(g->edges != NULL);
	for (i=0; i<V; i++){
		g->edges[i] = calloc(V, sizeof(int));
		assert(g->edges[i] != NULL);
	}
	return g;
}

// check if a vertex is valid in a graph
int validV(Graph g, Vertex v){
	return(g != NULL && v >= 0 && v < g->nV);
}

void insertEdge(Graph g, Edge e){
	assert(g != NULL && validV(g,e.v) && validV(g,e.w));
	if(g->edges[e.v][e.w] == 0){
		g->edges[e.v][e.w] = e.weight;
		g->edges[e.w][e.v] = e.weight;
		g->nE ++;
	}
}

void removeEdge(Graph g, Edge e){
	assert(g != NULL && validV(g,e.v) && validV(g,e.w));
	if(g->edges[e.v][e.w] != 0){
		g->edges[e.v][e.w] = 0;
		g->edges[e.w][e.v] = 0;
		g->nE --;
	}
}

int adjacent(Graph g, Vertex v, Vertex w){
	assert(g != NULL && validV(g,v) && validV(g,w));
	return(g->edges[v][w]);
}

void showGraph(Graph g){
	assert(g != NULL);
	int i, j;
	printf("Number of vertices: %d\n", g->nV);
	printf("Number of edges: %d\n", g->nE);
	for(i=0; i < g->nV; i++){
		for(j=0; j <g->nV; j++){
			if(g->edges[i][j] != 0){
				printf("Edge %d - %d: %d\n", i, j , g->edges[i][j]);
			}
		}
	}
}

void freeGraph(Graph g){
	assert(g != NULL);
	int i;
	for(i=0; i < g->nV; i++){
		free(g->edges[i]);
	}
	free(g->edges);
	free(g);
}


