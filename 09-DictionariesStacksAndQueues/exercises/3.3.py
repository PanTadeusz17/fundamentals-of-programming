import queue

def brackets_ok(expression):
    stack = queue.LifoQueue()
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in '([{':
            stack.put(char)
        elif char in ')]}':
            if stack.empty():
                return False
            if stack.get() != pairs[char]:
                return False

    return stack.empty()

def main():
    expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"
    expression2 = "[(2+3]/4)"
    expression3 = "(2-3*4+(5/6)"

    for idx, expr in enumerate([expression1, expression2, expression3], start=1):
        if brackets_ok(expr):
            print(f"Expression {idx}: brackets OK")
        else:
            print(f"Expression {idx}: brackets NOT correct")

if __name__ == "__main__":
    main()