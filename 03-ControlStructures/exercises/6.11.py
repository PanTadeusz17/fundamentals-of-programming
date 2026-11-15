current_price = float(input('Enter current price: '))
previous_price = float(input('Enter previous price: '))

reduction = ((previous_price - current_price) / previous_price) * 100

if reduction >= 10:
    print("Buy the product!")
    print(f'Product is reduced by {reduction:.0f}%')