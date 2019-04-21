/* Insertion Sort	

   by Benny Hwang 29/12/2017
*/

#include <stdio.h>

#define MAXSIZE 100 // set maximum array size to 100 elements

// insertion sort function
// input: array of numbers - A[0...n-1], size of array - n
void insertionSort(int array[], int n){
	int element, i, j;	
	for(i=0; i<n; i++){
		element = array[i];
		j = i-1;
		while(j>=0 && array[j] > element){
			array[j+1] = array[j];
			j --;
		}
		array[j+1] = element;
	}
}

int main(void){
	int n;
	printf("Enter array size (Maximum is 100):");
	scanf("%d",&n);
	while(n>MAXSIZE){
		printf("Enter array size (Maximum is 100):");
		scanf("%d",&n);
	}
	int array[n];
	for(int i=0; i<n; i++){
		printf("Input data into array:");
		scanf("%d", &array[i]);
	}
	
	printf("The entered array is:\n");
	for(int i=0; i<n; i++){
		printf("%d ", array[i]);
	}
	putchar('\n');
	insertionSort(array, n);
	printf("The sorted array is:\n");
	for(int i=0; i<n; i++){
		printf("%d ", array[i]);
	}
	putchar('\n');
	return 0;
}
	
	
