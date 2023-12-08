#include <stdio.h>
#include <math.h>

int beat(long int time, long int distance) {
	int j = 1, q = time-1;
	for (;j < time; j++)
		if (j*(time-j) > distance)
			break;
	for (; q > j; q--)
		if (q*(time-q) > distance)
			break;
	return (j>q?j-q:q-j)+1;
}


int digit_number(int number) {
	int d = 1;
	while ((number/=10)>0) {
		d++;
	}
	return d;
}

long int numjoin(int numbers[], int buffer) {
	long int result = 0;
	for (int i = 0; i < buffer; ++i){
		result = numbers[i] + result * ((int)pow(10, digit_number(numbers[i])));
	}
	return result;
}

int main() {
	FILE *fp;
	int times[4];
	int distances[4];
	char line[50];
	int result = 1;

	fp = fopen("inputs/day6.txt", "r");
	if (fp == NULL) {
		perror("Error in opening file day6.txt");
		return 1;
	}


	int number = 0, j = 0;
	// Times
	fgets(line, 50, fp);
	for (int i = 0; i < 50 || line[i] != '\0'; i++) {
		if (line[i] >= '0' && line[i] <= '9') {
			number = line[i]-'0' + number * (number!=0?10:1);
		} else if (line[i] == ' ' && number) {
			times[j++] = number;
			number = 0;
		} 
	}
	if (number) {
		times[j] = number;
		number = 0;
	}

	// Distances
	fgets(line, 50, fp);
	j = 0;
	for (int i = 0; i < 50 || line[i] != '\0'; i++) {
		if (line[i] >= '0' && line[i] <= '9') {
			number = line[i]-'0' + number * (number!=0?10:1);
		} else if (line[i] == ' ' && number) {
			distances[j++] = number;
			number = 0;
		} 
	}
	if (number) {
		distances[j] = number;
		number = 0;
	}

	for (int i = 0; i < 4; ++i)	{
		result *= beat(times[i], distances[i]);
	}

	printf("Part one: %d\n", result);


	// Part two
	long int time = numjoin(times, 4);
	long int distance = numjoin(distances, 4);
	printf("Part two: %d\n", beat(time, distance));

	fclose(fp);
	return 0;
}