// booyer moore text search algorithm. Written by Benny Hwang Feb 2018


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#define ASCII_SIZE 128
#define MAX_CHARACTERS 127
#define MAX_TEXT 1023
#define TEXT_FORMAT_STRING "%[^\n]%*c"

int *lastOccurence(char *pattern, char *alphabet){
	int *L = malloc(ASCII_SIZE * sizeof(int));
	assert(L != NULL);

	int i, s = strlen(alphabet);
	for(i=0; i<s; i++){
		L[(int)alphabet[i]] = -1;
	}
	
	int m = strlen(pattern);
	for(i=0; i<m; i++){
		L[(int)pattern[i]] = i;
	}

	return L;
}

int BoyerMooreMatch(char *text, char *pattern, char *alphabet){
	
	int *last = lastOccurence(pattern, alphabet);
	int i, a = strlen(alphabet);	// assume alphabets are given in alphabetical order
	printf("Last occurence array:\n");
	for (i=0; i<a; i++){
		printf("L[%c] = %d\n", alphabet[i], last[(int)alphabet[i]]);
	}
	putchar('\n');
	
	int m = strlen(pattern);
	int n = strlen(text);
	i = m-1;
	int j = m-1;
	
	while(i<n){
		if(text[i] == pattern[j]){
			if(j==0){
				return i;
			} else {
				i--;
				j--;
			}
		} else {
			int min = j < (1 + last[(int)text[i]]) ? j : 1 + last[(int)text[i]];
			i = i + m - min;
			j = m - 1;
		}
	}
	free(last);
	return -1;
}

int main(void){
	char alphabet[MAX_CHARACTERS], pattern[MAX_CHARACTERS], text[MAX_TEXT];
	/* Non space and newline character read version	
	printf("Enter alphabet: ");
	scanf("%s", &alphabet[0]);
	printf("Enter text: ");
	scanf("%s", &text[0]);
	printf("Enter pattern: ");
	scanf("%s", &pattern[0]);
	*/

	// This method can read every character as long as its not a new line.
	printf("Enter alphabet: ");
	scanf(TEXT_FORMAT_STRING, alphabet);
	printf("Enter text: ");
	scanf(TEXT_FORMAT_STRING, text);
	printf("Enter pattern: ");
	scanf(TEXT_FORMAT_STRING, pattern);
	
	int match = BoyerMooreMatch(text, pattern, alphabet);
	if (match != -1){
		printf("Pattern found at %d\n", match);
	} else {
		printf("Pattern not found!\n");
	}

	return 0;
}
