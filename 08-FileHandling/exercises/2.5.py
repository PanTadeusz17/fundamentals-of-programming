def add_product(file_name, product_name):
    with open(file_name, 'a') as file:
        file.write(product_name + "\n")

def main():
    shopping_list = 'shopping_list.txt'
    product = ""
    while product != "0":
        product = input('Enter product name (0 stops): ')
        if product == '0':
            break
        else:
            add_product(shopping_list, product)

if __name__ == "__main__":
    main()