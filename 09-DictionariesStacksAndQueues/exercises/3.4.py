import queue

def main():
    number = int(input("Natural number: "))
    stack = queue.LifoQueue()

    if number == 0:
        stack.put(0)
    else:
        n = number
        while n > 0:
            stack.put(n % 2)
            n //= 2

    print("Binary number: ", end="")
    while not stack.empty():
        print(stack.get(), end="")
    print()

if __name__ == "__main__":
    main()