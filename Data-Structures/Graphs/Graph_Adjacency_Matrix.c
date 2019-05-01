/*
Graph - Adjacency Matrix Implementation COMP9024 UNSW

*/

#include "Graph_Adjacency_Matrix.h"
#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

typedef struct GraphRep{
	int **edges;
	int nV;
	int nE;	
} GraphRep;

// set up new graph
Graph newGraph(int V){
	assert(V>=0);
	
	Graph g = malloc(sizeof(GraphRep));
	g->nV = V;
	g->nE = 0;

	// allocate memory for each row
	g->edges = malloc(V*sizeof(int *));
	assert(g->edges != NULL);

	// allocate memory for each column
	for(int i=0; i<V; i++){
		g->edges[i] = calloc(V, sizeof(int));	// calloc syntax calloc(number of element, size of each element)
		assert(g->edges[i]!=NULL);
	}

	return g;
}

// check if a vertex is valid in a graph
bool validV(Graph g, Vertex v){
	return (g!=NULL && v>=0 && v<g->nV);
}

// insert new edge
void insertEdge(Graph g, Edge e){
	assert(g!=NULL && validV(g, e.v) && validV(g, e.w));

	// if edge doesn't exist yet
	if(!g->edges[e.v][e.w]){
		g->edges[e.v][e.w] = 1;
		g->edges[e.w][e.v] = 1;
		g->nE ++;
	}
}

// remove edge
void removeEdge(Graph g, Edge e){
	assert(g!=NULL && validV(g, e.v) && validV(g, e.w));

	// if edge exist
	if(g->edges[e.v][e.w]){
		g->edges[e.v][e.w] = 0;
		g->edges[e.w][e.v] = 0;
		g->nE --;
	}
}

// check if two vertices are connected by an edge
bool adjacent(Graph g, Vertex v, Vertex w){
	assert(g!=NULL && validV(g, v) && validV(g, w));
	return (g->edges[v][w] !=0);
}

// show graph
void showGraph(Graph g){
	assert(g!=NULL);
	int i, j;
	printf("Number of vertices: %d\n", g->nV);
	printf("Number of edges: %d\n", g->nE);
	for(i=0; i<g->nV; i++){
		for(j=i+1; j<g->nV; j++){
			if(g->edges[i][j]){
				printf("Edge %d - %d\n", i, j );
			}
		}
	}
}

// free graph
void freeGraph(Graph g){
	assert(g!=NULL);
	for(int i=0; i<g->nV; i++){
		free(g->edges[i]);
	}
	free(g->edges);
	free(g);
}