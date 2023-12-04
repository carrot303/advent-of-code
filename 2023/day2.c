#include <stdio.h>
#include <string.h>

#define MAX_LINE 1000

int main() {
	FILE *fptr;
	char line[MAX_LINE];
	int result = 0;
	fptr = fopen("inputs/day2.txt", "r");
	if (fptr == NULL) {
		perror("Error in opening file day2.txt");
		return 1;
	}

	while ((fgets(line, MAX_LINE, fptr)) != NULL) {
		int number = 0;
		int blue = 0, red = 0, green = 0;
		int id = 0;
		int possible = 1;
		for (int i = 0; i < MAX_LINE && line[i] != '\0'; i++) {
			if (line[i] >= '0' && line[i] <= '9') {
				number = (line[i] - '0') + number * ((number!=0)?10:1);
				continue;
			} else if (line[i] == ':') {
				id = number;
				number = 0;
			} else if (line[i] == 'b') {
				blue = number;
				number = 0;
			} else if (line[i] == 'r') {
				red = number;
				number = 0;
			} else if (line[i] == 'g') {
				green = number;
				number = 0;
			} 
			if (red > 12 || green > 13 || blue > 14) {
				possible = 0;
				break;
			}
		}
		result += possible ? id : 0;
	}
	printf("Part one: %d\n", result);
    fseek(fptr, 0, SEEK_SET);

	// Part two
	result = 0;
	while ((fgets(line, MAX_LINE, fptr)) != NULL) {
		int number = 0;
		int blue = 0, red = 0, green = 0;
		int possible = 1;
		for (int i = 0; i < MAX_LINE && line[i] != '\0'; i++) {
			if (line[i] >= '0' && line[i] <= '9') {
				number = (line[i] - '0') + number * ((number!=0)?10:1);
				continue;
			} else if (line[i] == ':') {
				number = 0;
			} else if (line[i] == 'b') {
				blue = (number>blue)?number:blue;
				number = 0;
			} else if (line[i] == 'r') {
				red = (number>red)?number:red;
				number = 0;
			} else if (line[i] == 'g') {
				green = (number>green)?number:green;
				number = 0;
			}
		}
		result += red*blue*green;
	}
	printf("Part two: %d\n", result);
	fclose(fptr);
}