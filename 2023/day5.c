#include <stdio.h>
#include <ctype.h>
#include <string.h>

#define MAX_LINE 250
#define MAX_SEEDS 20


long int maps[7][50][3];


long int get_correspond(int mapid, long int number){
	long int source, dest, length;
	for (int j = 0; j < 50 && (maps[mapid][j][0] || maps[mapid][j][1] || maps[mapid][j][2]); j++) {
		dest = maps[mapid][j][0];
		source = maps[mapid][j][1];
		length = maps[mapid][j][2];
		if (number >= source && ((number-source)+dest) < dest+length) {
			return (number-source)+dest;
		}
	}
	return number;
}


int main() {
	FILE *fp;
	char line[MAX_LINE];
	char firstline[MAX_LINE];
	long int number = 0;
	long int seeds[MAX_SEEDS];

	memset(seeds, 0, sizeof(seeds));
	memset(maps, 0, sizeof(maps));

	fp = fopen("inputs/day5.txt", "r");

	fgets(firstline, MAX_LINE, fp); // seeds
	int j = 0;
	for (int i=0; i < MAX_LINE && firstline[i] != '\0'; i++) {
		if (isdigit(firstline[i])) {
			number = firstline[i]-'0' + number * (number!=0?10:1); 
		} else if (firstline[i] == ' ' && number) {
			seeds[j++] = number;
			number = 0;
		}
	}
	if (number) {
		seeds[j++] = number;
		number = 0;
	}

	int k = -1, i = 0;
	long int dest_start = 0, source_start = 0, range_length = 0;
	while ((fgets(line, MAX_LINE, fp)) != NULL) {
		if (strcmp(line, "\n") == 0) {
			k++;
			i = 0;
			fgets(line, MAX_LINE, fp);
			continue;
		}
		sscanf(line, "%ld %ld %ld", &dest_start, &source_start, &range_length);
		maps[k][i][0] = dest_start;
		maps[k][i][1] = source_start;
		maps[k][i][2] = range_length;
		i++;
	}

	// Part one
	long int tmp;
	long int lowest_direction = 1e10;
	for (int i = 0; i < MAX_SEEDS && seeds[i] != 0; i++) {
		tmp = get_correspond(0, seeds[i]); // seed-to-soil
		tmp = get_correspond(1, tmp); // soil-to-fertilizer
		tmp = get_correspond(2, tmp); // fertilizer-to-water
		tmp = get_correspond(3, tmp); // water-to-light
		tmp = get_correspond(4, tmp); // light-to-temperature
		tmp = get_correspond(5, tmp); // temperature-to-humidity
		tmp = get_correspond(6, tmp); // humidity-to-location
		lowest_direction = (tmp<lowest_direction?tmp:lowest_direction);
	}
	printf("Part one: %ld\n", lowest_direction);
	fclose(fp);
}