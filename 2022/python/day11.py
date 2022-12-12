from read_input import get_input_data


input_data = get_input_data(day=11)

class Monkey:
    monkeys: dict[int, 'Monkey'] = {}

    def __init__(self, data: list[str]) -> None:
        self.number = int(data[0].strip()[-2])
        self.starting_items = list(map(int, data[1].strip().split(':')[1].strip().split(',')))
        self.operation = data[2].strip().split(':')[-1].strip()
        self.divisible_by = int(data[3].strip().split()[-1])
        self.throw_to_monkey = {
            True: int(data[4].strip().split()[-1]),
            False: int(data[5].strip().split()[-1])
        }
        self.count = 0
    
    def start_round(self) -> None:
        """Starting round for this monkey"""
        removal_items = []
        
        for item in self.starting_items:
            operation = self.operation.replace('old', str(item)).split('=')[1]
            result_operation = eval(operation)
            divided = result_operation//3
            is_divisible = divided % self.divisible_by == 0
            throw_to_monkey = self.throw_to_monkey[is_divisible]
            self.throw(throw_to_monkey, divided)
            removal_items.append(item)
            
        self.count += len(self.starting_items)

        for removal_item in removal_items:
            self.starting_items.remove(removal_item)
        
    def throw(self, to_monkey: int, new_level_worry: int) -> None:
        """Throw the level to monkey items"""
        Monkey.monkeys[to_monkey].starting_items.append(new_level_worry)
        
    @classmethod
    def add_monkey(cls, monkey: 'Monkey'):
        cls.monkeys[monkey.number] = monkey
    

def solve_puzzle_one() -> int:
    monkeys = input_data.split('\n\n')
    for m in monkeys:
        monkey = Monkey(m.splitlines())
        Monkey.add_monkey(monkey)
    
    for _ in range(20):
        for _, monkey in Monkey.monkeys.items():
            monkey.start_round()
    monkey_one, monkey_two, *rest = sorted(Monkey.monkeys.items(), key=lambda m: m[1].count, reverse=True)
    return monkey_one[1].count * monkey_two[1].count


if __name__ == '__main__':
    print(f'Result puzzle one: {solve_puzzle_one()}')
