# Gwiazdki oddzielone ukośnikiem
def f(n):
    return "/".join(["*"] * n)

def main():
    print(f(4))
    print(f(1))

if __name__ == "__main__":
    main()