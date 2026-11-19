import json

def load_reservations(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data["reservations"] if isinstance(data, dict) else data

def count_rooms(reservations):
    return len(reservations)

def count_paid(reservations, paid_status):
    return sum(1 for r in reservations if r["paid"] == paid_status)

def total_value(reservations, paid_status):
    return sum(r["nights"] * r["price_per_night"] for r in reservations if r["paid"] == paid_status)

def main():
    reservations = load_reservations('reservations.json')
    print("Number of rooms:", count_rooms(reservations))
    print("Number of paid reservations:", count_paid(reservations, True))
    print("Number of unpaid reservations:", count_paid(reservations, False))
    print(f"Total value of paid reservations: {total_value(reservations, True):.2f}")
    print(f"Total value of unpaid reservations: {total_value(reservations, False):.2f}")

if __name__ == "__main__":
    main()