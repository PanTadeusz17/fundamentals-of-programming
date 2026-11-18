#Czy przynajmniej jedna z trzech liczb jest ujemna
def f(n1, n2, n3):
    return n1 < 0 or n2 < 0 or n3 < 0

def main():
    print(f(11, 6, -4))
    print(f(5, 4, 14))

if __name__ == "__main__":
    main()