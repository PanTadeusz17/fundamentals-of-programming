print("SURVEY")

# Wymuszamy zwrócenie wartości logicznej (True/False)
q1 = input("Are you interested in computer science? (y/n): ").lower() == 'y'
q2 = input("Do you like playing computer games? (y/n): ").lower() == 'y'
q3 = input("Do you have an Instagram account? (y/n): ").lower() == 'y'

# Nasz tłumacz z wyników logicznych na słowa z zadania
answers = {True: 'Yes', False: 'No'}

print("\nSURVEY RESULTS")
# q1, q2 i q3 muszą teraz być True albo False, inaczej słownik zwróci KeyError
print(f"Interested in computer science: {answers[q1]}")
print(f"Playing computer games: {answers[q2]}")
print(f"Has an Instagram account: {answers[q3]}")