from itertools import chain


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


def prepare_cycle(data: list, node_dict: dict, n: int):
    start = Node(data[0])
    node_dict[data[0]] = start

    prev = start
    for number in chain(data[1:], range(10, n + 1)):
        current = Node(number)
        node_dict[number] = current
        prev.next = current
        prev = current
    prev.next = start

    return start


def cut_next_three(current: Node):
    selected = []
    to_add = current

    for _ in range(3):
        to_add = to_add.next
        selected.append(to_add)

    current.next = selected[-1].next
    return selected


def insert_selected(current: Node, selected: list, node_dict: dict, n: int):
    dest_val = (current.value - 2 + n) % n + 1
    while dest_val in {node.value for node in selected}:
        dest_val = (dest_val - 2 + n) % n + 1
    dest_node = node_dict[dest_val]

    right = dest_node.next
    dest_node.next = selected[0]
    selected[-1].next = right


def simulate(start_seq: str, n: int, num_iters: int):
    data = [int(d) for d in start_seq]
    node_dict = {}
    current = prepare_cycle(data, node_dict, n)

    for _ in range(num_iters):
        selected = cut_next_three(current)
        insert_selected(current, selected, node_dict, n)
        current = current.next

    return node_dict


def part_one():
    start_seq = '716892543'
    d = simulate(start_seq=start_seq, n=len(start_seq), num_iters=100)
    result = []
    node = d[1]
    for _ in range(len(start_seq) - 1):
        node = node.next
        result.append(str(node.value))
    print(''.join(result))


def part_two():
    start_seq = '716892543'
    d = simulate(start_seq=start_seq, n=10**6, num_iters=10**7)
    first = d[1].next
    second = first.next
    print(first.value * second.value)


if __name__ == '__main__':
    part_one()
    part_two()
