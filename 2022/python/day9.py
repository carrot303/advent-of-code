from read_input import get_input_data

input_data = get_input_data(day=9)
lines = input_data.splitlines()


class Point:
    def __init__(self, id: int | str, x: int, y: int) -> None:
        self.id = id
        self.x = x
        self.y = y
        self.pathes = [str(self)]

    def move(self, direction: str, step: int = 1) -> None:
        """Move specific steps toward given direction"""
        match direction:
            case 'R':
                self.x += step
            case 'L':
                self.x -= step
            case 'U':
                self.y += step
            case 'D':
                self.y -= step
        if str(self) not in self.pathes:
            self.pathes.append(str(self))
    
    def dispatch(self, direction: str, point: 'Point') -> None:
        """Dispath the way"""
        if not self.is_touching(point):
            match direction:
                case 'R':
                    self.x = point.x-1
                    self.y = point.y
                case 'L':
                    self.x = point.x+1 
                    self.y = point.y
                case 'U':
                    self.y = point.y-1 
                    self.x = point.x
                case 'D':
                    self.y = point.y+1 
                    self.x = point.x
                    
            if str(self) not in self.pathes:
                self.pathes.append(str(self))
    
    def is_touching(self, point: 'Point') -> bool:
        """Check the self point is touching the other point
        diagonally, adjacent and even overlapping count as touching
        """
        is_touching = False
        if self.x == point.x and self.y == point.y:
            # overlapping
            is_touching = True
        
        if abs(self.x-point.x) == 1 and self.y == point.y:
            # adjacent -> next to the point [RIGHT or LEFT]
            is_touching = True

        if abs(self.y-point.y) == 1 and self.x == point.x:
            # adjacent -> next to the point [DOWN or UP]
            is_touching = True

        if abs(self.x-point.x) == 1 and abs(self.y-point.y) == 1:
            # diagonally
            is_touching = True
        return is_touching        
    
    def __str__(self) -> str:
        return f'Point(id={self.id}, x={self.x}, y={self.y})'
    
    def __repr__(self) -> str:
        return f'Point(id={self.id}, x={self.x}, y={self.y})'



def solve_puzzle_one() -> int:
    head = Point('H', 0, 0)
    tail = Point('T', 0, 0)
    for line in lines:
        dir_, step = line.split()
        for _ in range(int(step)):
            head.move(dir_)
            tail.dispatch(dir_, head)
    return len(tail.pathes)


if __name__ == '__main__':
    print(f"Result for puzzle one: {solve_puzzle_one()}")