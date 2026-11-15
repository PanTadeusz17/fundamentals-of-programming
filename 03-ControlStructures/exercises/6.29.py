n = int(input("How many prime numbers do you want to find? "))
print("Prime numbers:", end=" ")

count = 0      # Ile liczb pierwszych już znaleźliśmy
num = 2        # Zaczynamy sprawdzanie od liczby 2

while count < n:
    is_prime = True
    
    # Sprawdzamy, czy num dzieli się przez cokolwiek od 2 do num-1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break   # Znaleźliśmy dzielnik, nie ma sensu sprawdzać dalej
            
    if is_prime:
        print(num, end=" ")
        count += 1  
        
    num += 1        
    
print()