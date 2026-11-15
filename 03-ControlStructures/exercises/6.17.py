time_24 = input("Enter time (24-hour format): ")
hours_str, minutes_str = time_24.split(':')
hours = int(hours_str)

period = "am"
if hours >= 12:
    period = "pm"

# Konwersja z formatu 24h na 12h
if hours > 12:
    hours -= 12
elif hours == 0:
    hours = 12

print(f"Time in 12-hour format: {hours}:{minutes_str}{period}")