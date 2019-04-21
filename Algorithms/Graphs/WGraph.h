// Weighted Graph ADT interface.....  COMP9024 18x1 UNSW

typedef struct GraphRep *Graph;

// vertices are ints
typedef int Vertex;

// edges are pairs of vertices (end-points)
typedef struct Edge {
	Vertex v;
	Vertex w;
	int weight;
} Edge;

Graph newGraph(int);
void insertEdge(Graph, Edge);
void removeEdge(Graph, Edge);
int adjacent(Graph, Vertex, Vertex); // returns weight or 0 if not adjacent.
void showGraph(Graph);
void freeGraph(Graph);


