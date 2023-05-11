input_data = [-75, -72, -70, -69, -66, -65,
                 -63, -62, -60, -58, -56, -55,
                 -52, -51, -48, -46, -43, -42,
                 -41, -39, -37, -34, -33]


def solution(args):
    if not args:
        return ''
    ranges = []
    start, end = args[0], args[0]
    for i in range(1, len(args)):
        if args[i] == end + 1:
            end = args[i]
        else:
            if end - start >= 2:
                ranges.append(f'{start}-{end}')
            else:
                ranges.extend(str(j) for j in range(start, end+1))
            start, end = args[i], args[i]
    if end - start >= 2:
        ranges.append(f'{start}-{end}')
    else:
        ranges.extend(str(j) for j in range(start, end+1))
    return ','.join(ranges)


print(solution(input_data))


def find_ranges(start, end):
    ranges = []
    if end - start >= 2:
        ranges.append(f'{start}-{end}')
    else:
        ranges.extend(str(j) for j in range(start, end+1))
    return ranges


def solution2(args):
    ranges = []
    start, end = args[0], args[0]
    for i in range(1, len(args)):
        if args[i] == end + 1:
            end = args[i]
        else:
            ranges.extend(find_ranges(start, end))
            start, end = args[i], args[i]
    ranges.extend(find_ranges(start, end))
    return ','.join(ranges)


print(solution2(input_data))


def solution3(args):
    output = ''
    # In comments: 'group' = any individual integer, pair, or range of 3+
    for n in args:
        # At the end of the list, there's no extra punctuation
        if n == max(args): output += str(n)
        # You get a comma at the end of a group, or in the middle of a pair
        elif n+1 not in args or (n-1 not in args and n+2 not in args): output += str(n) + ','
        # You get a dash if you're at the start of a group and didn't get a comma
        elif n-1 not in args: output += str(n) + '-'
    return output


print(solution3(input_data))
