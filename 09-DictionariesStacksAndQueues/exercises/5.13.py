import queue

def main():
    stack = queue.LifoQueue()

    while True:
        token = input("Enter number, operator (+ - * /) or = : ").strip()
        if token == '=':
            if not stack.empty():
                print("Result:", stack.get())
            break
        elif token in ['+', '-', '*', '/']:
            b = stack.get()  # drugi argument (zdjęty jako pierwszy)
            a = stack.get()  # pierwszy argument (zdjęty jako drugi)
            if token == '+':
                stack.put(a + b)
            elif token == '-':
                stack.put(a - b)
            elif token == '*':
                stack.put(a * b)
            elif token == '/':
                stack.put(a / b)
        else:
            stack.put(float(token))

if __name__ == "__main__":
    main()