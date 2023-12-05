#include <stdio.h>
#include <string.h>

#define MAX 10000
#define ADJACENT(row1, row2) (row1+1 == row2)||(row1-1 == row2)||(row1 == row2)
#define SAME_RANGE(s1,s2,e1,e2) s1 >= s2-1 && e1 <= e2

struct Part {
	int row;
	int start;
	int end;
	int number;
	char type;
};

struct Symbol {
	int number;
	int row;
	int col;
};


int digit_number(int number) {
	int d = 1;
	while ((number/=10)>0) {
		d++;
	}
	return d;
}

int main(int argc, char const *argv[])
{
	FILE *fp;
	char line[MAX];
	struct Part numlocs[MAX];
	int result = 0;

	fp = fopen("inputs/day3.txt", "r");
	if (fp == NULL) {
		perror("Error in opening file day3.txt");
		return 1;
	}

	int number = 0;
	int i = 0;
	int k = 0;
	int j = 0;
	while ((fgets(line, MAX, fp)) != NULL) {
		for (j = 0; line[j] != '\0'; j++) {
			if ((line[j] < '0' || line[j] > '9') && line[j] != '.' && line[j] != '\n') {
				struct Part n =  {i, j, j, line[j], 's'};
				numlocs[k++] = n;
			}
			if (line[j] >= '0' && line[j] <= '9') {
				number = (line[j]-'0') + number * (number>0?10:1);
			}
			if ((line[j] < '0' || line[j] > '9') && number > 0) {
				struct Part n =  {i, j-digit_number(number), j, number, 'n'};
				numlocs[k++] = n;
				number = 0;
			}
		}
		i++;
	}
	if (number) {
		struct Part n =  {i-1, j-digit_number(number), j, number, 'n'};
		numlocs[k++] = n;
		number = 0;
	}
	fclose(fp);


	int symbol_numbers[150][150];
	int count_symbol_numbers[150][150];
	for (int i = 0; i < k; i++) {
		if (numlocs[i].type == 'n'){
			for (int j = 0; j < k; j++) {
				if ((numlocs[j].type == 's') &&
					(ADJACENT(numlocs[i].row, numlocs[j].row)) &&
					(SAME_RANGE(numlocs[j].start, numlocs[i].start, numlocs[j].end, numlocs[i].end))) {
					if (symbol_numbers[numlocs[j].row][numlocs[j].start] == 0) {
						symbol_numbers[numlocs[j].row][numlocs[j].start] = 1;
					}
					symbol_numbers[numlocs[j].row][numlocs[j].start] *= numlocs[i].number;
					count_symbol_numbers[numlocs[j].row][numlocs[j].start] += 1;
					result += numlocs[i].number;
					break;
				}
			}
		}
	}
	printf("Part one: %d\n", result);
	result = 0;
	for (int i=0; i < 150;i++){
		for (int j =0; j < 150;j++) {
			if (count_symbol_numbers[i][j] == 2) {
				result += symbol_numbers[i][j];
			}
		}
	}
	printf("Part two: %d\n", result);
	return 0;
}