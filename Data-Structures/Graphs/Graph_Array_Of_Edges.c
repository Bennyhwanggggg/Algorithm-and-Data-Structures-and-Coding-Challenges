/*
Graph - Array of Edges ADT

COMP9024 UNSW
*/

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "Graph_Array_Of_Edges.h"

#define MAXEDGES 1000000


typedef struct GraphRep{
	int nV;			// number of vertices
	int nE;			// number of edges
	Edge *edges;	// Array of edges
	int n;			// size of edge array
} GraphRep;


// initialise new graph
Graph newGraph(int v){
	Graph g = malloc(sizeof(GraphRep));
	assert(g!=NULL);
	g->nV = v;
	g->nE = 0;
	g->n = MAXEDGES;
	g->edges = malloc(g->n * sizeof(Edge));
	assert(g->edges != NULL);
	return g;
}

// check if two edges are equal
bool edgeEq(Edge e1, Edge e2){
	return((e1.v == e2.v && e1.w == e2.w) || (e1.v == e2.w && e1.w == e2.v ));
}

// insert new edge
void insertEdge(Graph g, Edge e){
	assert(g!=NULL && g->nE < g->n);
	int i = 0;
	while(i<g->nE && !edgeEq(e,g->edges[i])){
		i++;
	}
	// if edge e not found, we can insert it (avoid duplicated edges)
	if(i==g->nE){
		g->edges[i] = e;
		g->nE ++;
	}
}

// remove edge
void removeEdge(Graph g, Edge e){
	assert(g!=NULL);

	int i=0;
	// Go through all the edges until the edge we want to delete is found
	while(i<g->nE && !edgeEq(e, g->edges[i])){
		i++;
	}
	// if edge found, delete it by replacing it with the last edge in the current array
	if(i<g->nE){
		g->edges[i] = g->edges[--g->nE];
	}	
}

bool adjacent(Graph g, Vertex a, Vertex b){
	assert(g!=NULL);

	Edge e;
	e.v = a;
	e.w = b;

	int i = 0;
	while(i<g->nE){
		if(edgeEq(e, g->edges[i])){
			return true;
		}
		i++;
	}
	return false;
}

// show the whole graph structure
void showGraph(Graph g){
	assert(g!=NULL);

	printf("Number of edges: %d\n", g->nE);
	printf("Number of vertices: %d\n", g->nV);
	int i;
	for(i=0; i<g->nE; i++){
		printf("Edge %d - %d\n", g->edges[i].v, g->edges[i].w);
	}
}

// free the graph
void freeGraph(Graph g){
	assert(g!=NULL);
	free(g->edges);
	free(g);
}



