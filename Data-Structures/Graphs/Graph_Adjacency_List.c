/*
Graph - Adjacency List Implementation

From COMP9024 UNSW
*/

#include "Graph_Adjacency_List.h"
#include "llist.h"
#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

typedef struct GraphRep{
	List *edges;	// array of linked lists
	int nV;			// number of vertices
	int nE;			// number of edges
} GraphRep;

Graph newGraph(int nV){
	assert(nV>=0);
	
	Graph g = malloc(sizeof(GraphRep));
	assert(g!=NULL);
	g->nV = nV;
	g->nE = 0;

	g->edges = malloc(nV * sizeof(List));
	assert(g->edges!=NULL);
	for(int i=0; i<g->nV; i++){
		g->edges[i] = NULL;
	}

	return g;
}

// check if vertex is valid in a graph
bool validV(Graph g, Vertex v){
	return (g!=NULL && v>= 0 && v<g->nV);
}

// insert an edge
void insertEdge(Graph g, Edge e){
	assert(g!=NULL && validV(g,e.v) && validV(g,e.w));

	// check if the edge is already in a graph or not. Insert if not.
	if(!inLL(g->edges[e.v], e.w)){
		g->edges[e.v] = insertLL(g->edges[e.v], e.w);
		g->edges[e.w] = insertLL(g->edges[e.w], e.v);
		g->nE ++;
	}
}

// remove an edge
void removeEdge(Graph g, Edge e){
	assert(g!=NULL && validV(g,e.v) && validV(g,e.w));

	// check if the edge is already in a graph or not. Remove if its is there.
	if(inLL(g->edges[e.v], e.w)){
		g->edges[e.v] = deleteLL(g->edges[e.v], e.w);
		g->edges[e.w] = deleteLL(g->edges[e.w], e.v);
		g->nE --;
	}
}

// check if two vertices are connected by an edge
bool adjacent(Graph g, Vertex a, Vertex b){
	assert(g!=NULL && validV(g,a) && validV(g,b));

	return (inLL(g->edges[a], b));
}

// show a graph
void showGraph(Graph g){
	assert(g!=NULL);

	printf("Number of vertices: %d\n", g->nV);
	printf("Number of edges: %d\n", g->nE);
	for(int i=0; i<g->nV; i++){
		printf("%d - ", i);
		showLL(g->edges[i]);
	}
}

// free the graph
void freeGraph(Graph g){
	assert(g!=NULL);

	for(int i=0; i<g->nV; i++){
		free(g->edges[i]);
	}

	free(g);
}

