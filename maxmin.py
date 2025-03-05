def find_maxmin(num_list: list[int]) -> list[int] | None:
    '''
    Return a list containing the minimum and maximum values amongst an input which is a list of numbers.
    '''
    if len(num_list) == 0:
        return None

    minimum, maximum = num_list[0], num_list[0]

    for num in num_list[1:]:
        if num < minimum:
            minimum = num
        elif num > maximum:
            maximum = num

    return [minimum, maximum]


example1 = [2, 4, 1, 0, 2, -1]
example2 = [20, 50, 12, 6, 14, 8]
example3 = [100, -100]

if __name__ == '__main__':
    result1 = find_maxmin(example1)
    result2 = find_maxmin(example2)
    result3 = find_maxmin(example3)

    print(f'Example1 min and max: {result1}')
    print(f'Example2 min and max: {result2}')
    print(f'Example3 min and max: {result3}')
