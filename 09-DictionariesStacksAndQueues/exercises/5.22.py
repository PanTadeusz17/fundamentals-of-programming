import json

def main():
    product = {}
    product["name"] = input("Product name: ")
    product["price"] = round(float(input("Product price: ")), 2)
    paid_input = input("Paid (yes/no): ").strip().lower()
    product["paid"] = True if paid_input == "yes" else False

    with open('product.json', 'w', encoding='utf-8') as file:
        json.dump(product, file, indent=4)

if __name__ == "__main__":
    main()