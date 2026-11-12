

dog_age = float(input("Enter your dog's age: "))
dog_years_age = 0

if dog_age <= 2:
    dog_years_age = dog_age * 10.5
else:
    dog_years_age = 21 + (dog_age - 2) * 4

print(f"Dog's age in dog's years is {dog_years_age} years old.")