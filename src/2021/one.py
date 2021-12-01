def part_one():
    f = open('one.txt', 'r')
    lines = f.readlines()
    nums = [int(i) for i in lines]
    total = 0
    for _ in range(1, len(nums), 1):
        if nums[_] > nums[_-1]:
            total += 1
    print(total)

def part_two():
    f = open('one.txt', 'r')
    lines = f.readlines()
    nums = [int(i) for i in lines]
    summed_nums = []
    for _ in range(2, len(nums), 1):
        summed_nums.append(nums[_] + nums[_-1] + nums[_-2])
    total = 0
    for _ in range(1, len(summed_nums), 1):
        if summed_nums[_] > summed_nums[_-1]:
            total += 1
    print(total)

part_two()
