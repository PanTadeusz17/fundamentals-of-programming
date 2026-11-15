correct_pin = "0805"
attempts = 3

while attempts > 0:
    pin = input("Enter the PIN code: ")
    if pin == correct_pin:
        print("Access granted!")
        break
    else:
        print("Incorrect...")
        attempts -= 1

# Poza pętlą sprawdzamy, czy skończyły się próby
if attempts == 0:
    print("Sorry, your payment card has been blocked.")