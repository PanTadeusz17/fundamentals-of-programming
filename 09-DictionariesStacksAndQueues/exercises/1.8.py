def main():
    price_list = {
        'T-shirt': 19.99,
        'Jeans': 49.99,
        'Jacket': 89.99,
        'Sneakers': 59.99,
        'Hat': 15.99
    }

    print("Prices before discount:")
    for item, price in price_list.items():
        print(f"{item}: {price:.2f}")
    print(f"Total before discount: {sum(price_list.values()):.2f}\n")

    for item in price_list:
        price_list[item] = round(price_list[item] * 0.9, 2)

    print("Prices after 10% discount:")
    for item, price in price_list.items():
        print(f"{item}: {price:.2f}")
    print(f"Total after discount: {sum(price_list.values()):.2f}")

if __name__ == "__main__":
    main()