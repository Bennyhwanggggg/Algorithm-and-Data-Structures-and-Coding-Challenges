// Graph Adjacency Matrix Interface 	COMP9024 18x1 UNSW
#include <stdbool.h>
typedef struct GraphRep *Graph;
// vertices are ints
typedef int Vertex;
// edges are pairs of vertices (end-points)
typedef struct Edge {
	Vertex v;
	Vertex w;
} Edge;

Graph newGraph(int);
void insertEdge(Graph, Edge);
void removeEdge(Graph, Edge);
bool adjacent(Graph, Vertex, Vertex);
void showGraph(Graph);
void freeGraph(Graph);




