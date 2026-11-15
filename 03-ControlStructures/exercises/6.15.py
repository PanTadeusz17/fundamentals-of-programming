ean = input("Enter EAN-13 article number: ")

# Sprawdzamy czy ma 13 znaków i czy to tylko cyfry
if len(ean) == 13 and ean.isdigit():
    print("Article number is correct")
    
   
    # Można też if ean.startswith('590'):
    if ean[:3] == '590':
        print("Article manufactured in Poland")