input = "233313312141413140216898416549879"

with open("input_day9.txt") as file: input = file.read()

disk = []
last_checked_block_index = None
checks = []

for i in range(len(input)):
	if i % 2 == 0:
		disk += [(i//2)] * int(input[i])
	else:
		disk += [None] * int(input[i])


def last_block():
	if last_checked_block_index is not None:
		start = last_checked_block_index-1
	else:
		start = len(disk)-1
	for i in range(start, -1, -1):
		if disk[i] and disk[i] not in checks:
			return i, disk[i]

def last_all_block():
	r = last_block()
	if r is None:
		return None
	last_block_index, last_block_id = r
	return disk.index(last_block_id), last_block_id, disk.count(last_block_id)


def get_required_space(count, disk, until_id):
	first_sector = None
	last_sector = None
	sectore_count = 0
	for i in range(0, until_id+1):
		if sectore_count == count:
			last_sector = i
			break

		if disk[i] == None:
			sectore_count += 1
			first_sector = first_sector or i
		else:
			first_sector = None
			sectore_count = 0
	else:
		return None, None

	return first_sector, last_sector



def defrag_any():
	temp_disk = disk
	while True:
		last_block_index, _ = last_block()
		first_space = temp_disk.index(None)
		if last_block_index < first_space:
			break
		temp_disk[first_space] = temp_disk[last_block_index]
		temp_disk[last_block_index] = None

	result = 0
	for i in range(temp_disk.index(None)):
		result += i * temp_disk[i]
	return result


def defrag_all():
	global last_checked_block_index
	temp_disk = disk
	while last_all_block():
		index, id, count = last_all_block()
		last_checked_block_index = index
		first, last = get_required_space(count, temp_disk, index)
		checks.append(id)
		if first and last:
			temp_disk[first:last] = [id] * count
			temp_disk[index:index+count] = [None] * count
		elif count == 1:
			break

	result = 0
	for i in range(len(temp_disk)):
		if temp_disk[i] == None: continue
		result += i * temp_disk[i]
	return result


print("Part 1:", defrag_any())
print("Part 2:", defrag_all())