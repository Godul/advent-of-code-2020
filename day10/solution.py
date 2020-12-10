from collections import defaultdict


def get_sorted_jolts():
    with open('input.txt') as file:
        return list(sorted(map(int, file)))


def count_diffs(jolts: list):
    count_dict = defaultdict(int)
    for i in range(1, len(jolts)):
        count_dict[jolts[i] - jolts[i - 1]] += 1
    return count_dict


def count_arrangements(jolts: list):
    # Dynamic solution with s[i] meaning: number of arrangements containing i-th adapter
    s = [0] * len(jolts)
    s[0] = 1  # Empty arrangement
    s[1] = 1  # 0-th adapter is always there
    s[2] = 2 if jolts[2] <= 3 else 1  # Two solutions if can skip first adapter

    for i in range(3, len(s)):
        s[i] = s[i - 1]  # We can simply add i-th adapter to the arrangement
        if jolts[i] - jolts[i - 2] <= 3:  # If we can skip (i-1)-th
            s[i] += s[i - 2]
        if jolts[i] - jolts[i - 3] <= 3:  # If we can skip (i-1)-th and (i-2)-th
            s[i] += s[i - 3]
    return s[-1]


def both_parts():
    jolts = get_sorted_jolts()
    jolts.insert(0, 0)  # We start with zero joltage
    jolts.append(jolts[-1] + 3)  # Last joltage is equal to largest + 3

    count_dict = count_diffs(jolts)
    print(count_dict[1] * count_dict[3])

    num_arrangements = count_arrangements(jolts)
    print(num_arrangements)


if __name__ == '__main__':
    both_parts()
