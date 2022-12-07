from read_input import get_input_data
from collections import defaultdict

input_data = get_input_data(day=7)

SZ = defaultdict(int)

def solve_puzzle_one() -> int:
    path = []
    for line in input_data.splitlines():
        words = line.strip().split()
        if words[1] == 'cd':
            if words[2] == '..':
                path.pop()
            else:
                path.append(words[2])
        if words[1] == 'ls':
            continue
        else:
            try:
                sz = int(words[0])
                for i in range(len(path)+1):
                    SZ['/'.join(path[:i])] += sz
            except:
                pass
    
    ans = 0
    for k, v in SZ.items():
        if v <= 100000:
            ans += v
    return ans

def solve_puzzle_two():
    max_used = 70000000 - 30000000
    total_size = SZ['/']
    need_to_free = total_size - max_used

    ans = 1e9
    for k, v in SZ.items():
        if v >= need_to_free:
            ans = min(ans, v)
    return ans

print(solve_puzzle_one())
print(solve_puzzle_two())