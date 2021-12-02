def part_one():
        f = open('two.txt')
        lines = f.readlines()
        casted = [str(i) for i in lines]
        horizontal = 0
        depth = 0
        for _ in casted:
                if 'forward' in _: horizontal += int(_[8:])
                elif 'down' in _: depth += int(_[5:])
                elif 'up' in _: depth -= int(_[3:])
        print(horizontal * depth)

def part_two():
        f = open('two.txt')
        lines = f.readlines()
        casted = [str(i) for i in lines]
        horizontal = 0
        depth = 0
        aim = 0
        for _ in casted:
                if 'forward' in _:
                        horizontal += int(_[8:])
                        depth += (aim * int(_[8:]))
                elif 'down' in _:
                        aim += int(_[5:])
                elif 'up' in _:
                        aim -= int(_[3:])
        print(horizontal * depth)
