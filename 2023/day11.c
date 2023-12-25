#include <stdio.h>
#include <string.h>
#include <stdlib.h> 


#define LEN 200
#define GAL 500


typedef struct {
	int i;
	int j;
} Coord;

char buffer[LEN][LEN];
Coord galaxies[GAL];
int g = 0;


int is_row_empty(int i) {
	for (int j = 0; j < g; j++) {
		if (galaxies[j].i == i) {
			return 0;
		}
	}
	return 1;
}

int is_column_empty(int i) {
	for (int j = 0; j < g; j++) {
		if (galaxies[j].j == i) {
			return 0;
		}
	}
	return 1;
}

int main() {

	FILE *fp;
	char line[LEN];
	Coord coord = {};
	int result = 0;

	fp = fopen("inputs/day11.txt", "r");
	if (fp == NULL) {
		perror("Error in opening day11.txt");
		return 1;
	}
	memset(buffer, '.', sizeof(buffer));

	int i = 0;
	while (fgets(line, LEN, fp) != NULL) {
		for (int j=0; j < strlen(line) && line[j] != '\n'; j++) {
			buffer[i][j] = line[j];
			if (line[j] == '#') {
				coord.i = i;
				coord.j = j;
				galaxies[g++] = coord;
			}
		}
		i++;
	}
	for (int i = 0; i < g; i++) {
		for (int j = i+1; j < g; j++) {
			int r = 0;
			int min_x = (galaxies[i].j<galaxies[j].j) ? galaxies[i].j : galaxies[j].j;
			int max_x = (galaxies[i].j>galaxies[j].j) ? galaxies[i].j : galaxies[j].j;

			for (int x = min_x; x < max_x; x++, r++)
				if (is_column_empty(x)) r++;

			int min_y = (galaxies[i].i<galaxies[j].i) ? galaxies[i].i : galaxies[j].i;
			int max_y = (galaxies[i].i>galaxies[j].i) ? galaxies[i].i : galaxies[j].i;
			
			for (int y = min_y; y < max_y; y++, r++)
				if (is_row_empty(y)) r++;
			
			result += r;
		}
	}
	printf("Part one: %d\n", result);


	// Part two
	long long int result2 = 0;
	for (int i = 0; i < g; i++) {
		for (int j = i+1; j < g; j++) {
			int r = 0;
			int min_x = (galaxies[i].j<galaxies[j].j) ? galaxies[i].j : galaxies[j].j;
			int max_x = (galaxies[i].j>galaxies[j].j) ? galaxies[i].j : galaxies[j].j;

			for (int x = min_x; x < max_x; x++, r++)
				if (is_column_empty(x)) r += 1000000-1;

			int min_y = (galaxies[i].i<galaxies[j].i) ? galaxies[i].i : galaxies[j].i;
			int max_y = (galaxies[i].i>galaxies[j].i) ? galaxies[i].i : galaxies[j].i;
			
			for (int y = min_y; y < max_y; y++, r++)
				if (is_row_empty(y)) r += 1000000-1;
			
			result2 += r;
		}
	}
	printf("Part two: %lld\n", result2);

}