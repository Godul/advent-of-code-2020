def load_numbers():
    with open('input.txt') as file:
        return list(map(int, file))


def is_sum_of_two(n: int, q: list):
    for i in range(len(q)):
        for j in range(i):
            if q[i] + q[j] == n:
                return True
    return False


def find_invalid(numbers: list):
    # We use list as a queue for convenience. It's always short, so there's no need for deque.
    queue = numbers[:25]

    for n in numbers[25:]:
        if not is_sum_of_two(n, queue):
            return n
        queue.pop(0)
        queue.append(n)


def calc_partial_sums(numbers: list):
    s = [0] * (len(numbers) + 1)
    for i in range(1, len(numbers) + 1):
        s[i] = s[i - 1] + numbers[i - 1]
    return s


def find_subarray_with_sum(numbers: list, n: int):
    s = calc_partial_sums(numbers)

    for idx_r in range(len(s)):
        for idx_l in range(idx_r - 1):
            if s[idx_r] - s[idx_l] == n:
                return numbers[idx_l:idx_r]


def both_parts():
    numbers = load_numbers()
    invalid_n = find_invalid(numbers)
    print(invalid_n)
    subarray = find_subarray_with_sum(numbers, invalid_n)
    print(max(subarray) + min(subarray))


if __name__ == '__main__':
    both_parts()
