a = 0
b = 1

for i in range(20):
    print(a, end=" ")
    # Magia Pythona: jednoczesna aktualizacja obu zmiennych
    a, b = b, a + b
    
print()