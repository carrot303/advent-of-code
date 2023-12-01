#include <stdio.h>
#include <string.h>


int main() {
    char c;
    char line[100];
    FILE *fptr;
    char* letters[9] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    int result = 0;

    fptr = fopen("./inputs/day1.txt", "r");
    if (fptr == NULL) {
        perror("Error in opening file day1.txt\n");
        return 1;
    }
    while ((fgets(line, 100, fptr)) != NULL) {
        int first = -1;
        int last = -1;
        for (int i = 0; i < 100 && line[i] != '\0';i++) {
            if (line[i] >= 47 && line[i] <= 59) {
                if (first == -1) {
                    first = line[i] - '0';
                }
                last = line[i] - '0';
            }
        }
        if (first != -1 && last != -1) {
            result += first * 10 + last;
        }
    }
    printf("Part one: %d\n", result);
    fseek(fptr,0, SEEK_SET);


    // Part two
    result = 0;
    while ((fgets(line, 100, fptr)) != NULL) {
        int first = -1;
        int last = -1;
        for (int i = 0; i < 100 && line[i] != '\0';i++) {
            if (line[i] >= 47 && line[i] <= 59) {
                if (first == -1) {
                    first = line[i] - '0';
                }
                last = line[i] - '0';
                continue;
            }
            char string[100];
            for (int k = 0, j = i; j < sizeof(line) && line[j] != '\0'; j++){
                string[k++] = line[j];
                string[k+1] = '\0';
                for (int q=0; q < 9; q++){
                    if (strcmp(letters[q], string) == 0){
                        if (first == -1) {
                            first = q+1;
                        }
                        last = q+1;
                        break;
                    }
                }
            }
        }
        if (first != -1 && last != -1) {
            result += first * 10 + last;
        }
    }
    fclose(fptr);
    printf("Part two: %d\n", result);
}
