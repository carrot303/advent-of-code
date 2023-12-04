from collections import defaultdict

with open("inputs/day3.txt") as file:
	puzzle = file.read().strip()

lines = puzzle.split("\n")
not_symbols = "0123456789."
digits = "0123456789"
result = 0
positions = []
for i in range(len(lines)):
	number = ""
	for j in range(len(lines[i])):
		if lines[i][j] not in digits and number != "":
			positions.append((i, int(number), j-len(number), j))
			number = ""
			continue

		if lines[i][j].isdigit():
			number += lines[i][j]

	if number:
		positions.append((i,int(number), j-len(number)+1, j))

# Part one
for p in positions:
	i, n, j, k = p
	if j > 0 and lines[i][j-1] not in not_symbols:
		result += n
		continue
	if lines[i][k] not in not_symbols:
		result += n
		continue
	for ii in range(max(j-1,0), k+1):	
		if i > 0 and lines[i-1][ii] not in not_symbols:
			break
		if i < len(lines)-1 and lines[i+1][ii] not in not_symbols: 
			break
	else:
		continue
	result += n
	
print(result)


# Part Two
symbol_positions = defaultdict(list)

for p in positions:
	i, n, j, k = p
	if j > 0 and lines[i][j-1] not in not_symbols:
		symbol_positions[(i,j-1)].append(n)
	if lines[i][k] not in not_symbols:
		symbol_positions[(i,k)].append(n)
		result += n
	for ii in range(max(j-1,0), k+1):	
		if i > 0 and lines[i-1][ii] not in not_symbols:
			symbol_positions[(i-1,ii)].append(n)
		if i < len(lines)-1 and lines[i+1][ii] not in not_symbols: 
			symbol_positions[(i+1,ii)].append(n)

result = 0
for s, nums in symbol_positions.items():
	if len(nums) == 2:
		result += nums[0] * nums[1]

print(result)