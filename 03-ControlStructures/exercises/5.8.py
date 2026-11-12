

balance = 1000
PIN = 1111

while True:
    print()
    print('ATM menu:')
    print('1. Check balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Check PIN')
    print('5. Change PIN')
    print('6. Exit')

    choice = input('What do you want to do? (1-6): ')
    print()

    if choice == '1':
        print(f'Your balance is: {balance}zl')
    elif choice == '2':
        amount = float(input('Enter amount to deposit: '))
        balance += amount
        print(f'Amount has been deposited. New balance: {balance}')
    elif choice == '3':
        amount = float(input('Enter amount to withdraw: '))
        if amount <= balance:
            balance -= amount
            print(f'Amount has been withdrawn. New balance: {balance}')
        else:
            print('Insufficient balance.')
    elif choice == '4':
        print(f'Your PIN is {PIN}')
    elif choice == '5':
        new_pin = input('Enter a new 4-digit PIN: ')
        if len(new_pin) == 4 and new_pin.isdigit():
            PIN = new_pin
            print('PIN has been successfully changed.')
        else:
            print('Invalid PIN. It must consist of exactly 4 digits.')
    elif choice == '6':
        print('Exiting... Thank you for using the ATM!')
        break
    else:
        print('Invalid option. Please try again.')
