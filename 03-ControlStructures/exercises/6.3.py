###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
light_switch1 = input('Switch 1 (on/off): ') # False - switch off, True - switch on
light_switch2 = input('Switch 2 (on/off): ')
bulbs_on = 0
if light_switch1 == 'on':
    bulbs_on += 1
elif light_switch1 == 'off':
    bulbs_on = 0
if light_switch2 == 'on':
    bulbs_on += 2
elif light_switch2 == 'off':
    bulbs_on = 0

print(f'Number of bulbs on: {bulbs_on}')