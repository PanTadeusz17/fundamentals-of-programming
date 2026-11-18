def main():
    t = (10, 20, 30, 40, 50)
    print("Tuple:", ",".join(map(str, t)))
    print("Reverse order:", ",".join(map(str, t[::-1])))

if __name__ == "__main__":
    main()