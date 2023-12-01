import sys


with open("inputs/day1.txt") as file:
    puzzle = file.read().strip()

# Part one
result = 0
for l in puzzle.split("\n"):
    digits = ""
    for c in l:
        if 48 <= ord(c) <= 59:
            digits += c
    if digits:
        result += int("".join([digits[0],digits[-1]]))

print("Part 1:", result)



# Part two
letters = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
result = 0

for l in puzzle.split("\n"):
    digits = []
    c = 0
    for _ in range(len(l)):
        if c < len(l) and 48 <= ord(l[c]) <= 59:
            digits.append(int(l[c]))
            c += 1
            continue
        string = ""
        for j in range(c,len(l)):
            string += l[j]
            if string in letters:
                digits.append(letters.index(string)+1)
                break
        c += 1
    if digits:
        result += int(f"{digits[0]}{digits[-1]}")


print("Part 2:", result)

