#include <stdio.h>

#define MAX_LINE 200


int power(int i, int b) {
	int r = 1;
	while (b-- > 0) {
		r *= i;
	}
	return r;
}

int main() {
	FILE *fp;
	char line[MAX_LINE];
	int winnumbers[10];
	int own_numbers[25];
	int scrathcards[250] = {0};
	int card_id = 0;
	int number = 0;
	int result = 0;
	int result2 = 0;

	fp = fopen("inputs/day4.txt", "r");
	if (fp == NULL) {
		perror("Error in opening file day4.txt");
		return 1;
	}

	while ((fgets(line, MAX_LINE, fp)) != NULL) {
		int k = 0;
		for (int side=0, i=0; line[i] != '\0'; i++) {
			if (line[i] >= '0' && line[i] <= '9') {
				number = (line[i] - '0') + number * ((number!=0)?10:1);
			} else if (line[i] == ':') {
				card_id = number;
				number = 0;
			} else if (line[i] == ' ' && number > 0) {
				if (side == 0) {
					winnumbers[k++] = number;
					number = 0;
				} else if (side == 1) {
					own_numbers[k++] = number;
					number = 0;
				}
			} else if (line[i] == '|') {
				side = 1;
				k = 0;
			}
		}
		if (number > 0) {
			own_numbers[k] = number;
			number =0 ;
		}
		
		// Part one
		int same_cards = 0;
		for (int i = 0; i < 25; i++) {
			for (int j = 0; j < 10; j++) {
				if (own_numbers[i] == winnumbers[j]) {
					same_cards++;
				}
			}
		}
		scrathcards[card_id]++;
		result2++;
		if (same_cards) {
			result += power(2, same_cards-1);
		}
		for (int i = 0; i < scrathcards[card_id]; i++) {
			for (int j = card_id+1; j < card_id+same_cards+1; j++) {
				scrathcards[j]++;
				result2++;
			}
		}
	}
	printf("Part one: %d\n", result);
	printf("Part two: %d\n", result2);

	fclose(fp);
	return 0;
}
