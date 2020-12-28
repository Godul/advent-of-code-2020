from abc import (
    ABC,
    abstractmethod,
)


class Expr(ABC):
    @abstractmethod
    def eval(self):
        pass


class BinExpr(Expr, ABC):
    def __init__(self, left: Expr, right: Expr = None):
        super().__init__()
        self.left = left
        self.right = right


class AddExpr(BinExpr):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def eval(self):
        return self.left.eval() + self.right.eval()


class MulExpr(BinExpr):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def eval(self):
        return self.left.eval() * self.right.eval()


class IntExpr(Expr):
    def __init__(self, val: int):
        super().__init__()
        self.val = val

    def eval(self):
        return self.val


def load_data():
    with open('input.txt') as file:
        return [line[:-1] for line in file]


def tokenize(line: str):
    res = []
    i = 0
    while i < len(line):
        if line[i] in {'(', ')', '+', '*'}:
            res.append(line[i])
            i += 1
        elif line[i].isdigit():
            j = i + 1
            while j < len(line) and line[j].isdigit():
                j += 1
            res.append(int(line[i:j]))
            i = j
        else:
            i += 1
    return res


def parse(tokens: list) -> Expr:
    stack = []

    for token in tokens:
        if isinstance(token, int):
            int_expr = IntExpr(token)
            if stack and isinstance(stack[-1], BinExpr):
                stack[-1].right = int_expr
            else:
                stack.append(int_expr)
        elif token == '+':
            stack.append(AddExpr(left=stack.pop()))
        elif token == '*':
            stack.append(MulExpr(left=stack.pop()))
        elif token == '(':
            stack.append(token)
        elif token == ')':
            expr = stack.pop()
            stack.pop()
            if stack and isinstance(stack[-1], BinExpr):
                stack[-1].right = expr
            else:
                stack.append(expr)

    if len(stack) != 1:
        raise RuntimeError('Parse error')
    return stack[0]


def insert_left_bracket(tokens: list, add_idx: int):
    idx = add_idx - 1
    if tokens[idx] == ')':
        opened_num = 1
        while opened_num > 0:
            idx -= 1
            if tokens[idx] == ')':
                opened_num += 1
            elif tokens[idx] == '(':
                opened_num -= 1
    tokens.insert(idx, '(')


def insert_right_bracket(tokens: list, add_idx: int):
    idx = add_idx + 1
    if tokens[idx] == '(':
        opened_num = 1
        while opened_num > 0:
            idx += 1
            if tokens[idx] == '(':
                opened_num += 1
            elif tokens[idx] == ')':
                opened_num -= 1
    tokens.insert(idx + 1, ')')


def insert_addition_brackets(tokens: list):
    i = 0
    while i < len(tokens):
        if tokens[i] == '+':
            insert_left_bracket(tokens, i)
            i += 1
            insert_right_bracket(tokens, i)
        i += 1


def part_one():
    result = 0
    for line in load_data():
        tokens = tokenize(line)
        expr = parse(tokens)
        result += expr.eval()
    print(result)


def part_two():
    result = 0
    for line in load_data():
        tokens = tokenize(line)
        insert_addition_brackets(tokens)
        expr = parse(tokens)
        result += expr.eval()
    print(result)


if __name__ == '__main__':
    part_one()
    part_two()
