import queue

def main():
    customers = queue.Queue()
    ticket_number = 1

    while True:
        print("\n1. New customer (issue ticket)")
        print("2. Serve next customer")
        print("0. Quit")
        choice = input("Select option: ")

        if choice == '1':
            customers.put(ticket_number)
            print(f"Customer with ticket #{ticket_number} added to the queue.")
            ticket_number += 1
        elif choice == '2':
            if not customers.empty():
                served = customers.get()
                print(f"Now serving customer with ticket #{served}.")
            else:
                print("No customers in the queue.")
        elif choice == '0':
            break

if __name__ == "__main__":
    main()