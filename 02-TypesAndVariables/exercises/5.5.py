Price = float(input("Enter price: "))
Discount = float(input("Enter discount (in %): "))
PriceWithDiscount = Price * ((100 - Discount) / 100)
Reduction = Price - PriceWithDiscount
print(f"You got {Reduction} off! Your price is now {PriceWithDiscount}")