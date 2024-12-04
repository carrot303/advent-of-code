
input = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

with open("input_day4.txt") as file: input = file.read()

letters = [list(line) for line in input.strip().split("\n")]

possible_X = ["MAS MAS","MAS SAM", "SAM SAM", "SAM MAS"]


def part1():
	result = 0
	for x in range(len(letters)):
		for y in range(len(letters[x])):
			hor = [l[y] for l in letters[x:x+4]]
			diagonals = [
				[letters[x+i][y+i] for i in range(4) if x+i < len(letters) and y+i < len(letters)], # DIAGONALS TOP-RIGHT-DOWN
				[letters[x+i][y-i] for i in range(4) if x+i < len(letters) and y-i >= 0], 			# DIAGONALS TOP-LEFT-DOWN
				[letters[x-i][y+i] for i in range(4) if x-i >= 0 and y+i < len(letters)], 			# DIAGONALS DOWN-RIGHT-TOP
				[letters[x-i][y-i] for i in range(4) if x-i >= 0 and y-i >= 0], 					# DIAGONALS DOWN-LEFT-TOP
			]
			if "".join(letters[x][y:y+4]) in ["XMAS", "SAMX"]: result += 1
			if "".join(hor) in ["XMAS", "SAMX"]: result += 1
			for diagonal in diagonals:
				if "".join(diagonal) == "XMAS": result += 1
	return result


def part2():
	result = 0
	for x in range(len(letters)-2):
		for y in range(len(letters[x])-2):
			cube3x3 = [l[y:y+3] for l in letters[x:x+3]]
			patt_x1 = "".join([cube3x3[i][i] for i in range(3)])
			patt_x2 = "".join([cube3x3[i][j] for i,j in zip(range(3),range(2,-1,-1))])
			if f"{patt_x1} {patt_x2}" in possible_X:
				result += 1
	return result


print("Part 1:" ,part1())
print("Part 2:" ,part2())