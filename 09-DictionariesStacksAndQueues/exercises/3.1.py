import queue

def main():
    stack = queue.LifoQueue()
    for num in [2, 3, 7, 4, 1, 9, 8]:
        stack.put(num)

    # Suma dwóch ostatnich liczb zdjętych z wierzchu (8 + 9)
    last_two_sum = stack.get() + stack.get()
    print("Sum of last two numbers:", last_two_sum)

    # Suma pozostałych elementów za pomocą pętli while
    remaining_sum = 0
    while not stack.empty():
        remaining_sum += stack.get()
    print("Sum of remaining elements:", remaining_sum)

if __name__ == "__main__":
    main()