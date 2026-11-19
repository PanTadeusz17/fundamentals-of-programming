def hotel_list(hotels):
    return ",".join(hotel["name"] for hotel in hotels)

def avg_price(hotels):
    total = sum(hotel["price"] for hotel in hotels)
    return round(total / len(hotels))

def main():
    hotels_in_Krakow = [
        {"name": "Sky", "price": 320.00},
        {"name": "Metropol", "price": 480.00},
        {"name": "New Port", "price": 420.00},
        {"name": "Aparthotel", "price": 390.00}
    ]
    hotels_in_Sopot = [
        {"name": "Focus", "price": 510.00},
        {"name": "Aqua", "price": 345.00},
        {"name": "La Boutique", "price": 390.00},
        {"name": "Marina", "price": 410.00}
    ]

    krakow_avg = avg_price(hotels_in_Krakow)
    sopot_avg = avg_price(hotels_in_Sopot)
    cheaper = "Krakow" if krakow_avg < sopot_avg else "Sopot"

    print("Hotels in Krakow:", hotel_list(hotels_in_Krakow))
    print("Average hotel price in Krakow:", krakow_avg)
    print("Hotels in Sopot:", hotel_list(hotels_in_Sopot))
    print("Average hotel price in Sopot:", sopot_avg)
    print("Cheaper hotels in:", cheaper)

if __name__ == "__main__":
    main()