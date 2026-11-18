import math
import matplotlib.pyplot as plt

def main():
    x = list(range(0, 361))
    y = [math.sin(math.radians(deg)) for deg in x]
    plt.plot(x, y)
    plt.show()

if __name__ == "__main__":
    main()