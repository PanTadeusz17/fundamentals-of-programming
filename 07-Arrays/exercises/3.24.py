import random

def rand_elem(array):
    return array[random.randint(0, len(array) - 1)]

def main():
    arr = [10, 20, 30, 40, 50]
    for _ in range(3):
        print(rand_elem(arr))

if __name__ == "__main__":
    main()