###
# String manipulation
#
e = 0
movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print('Capitalized title: ', movie.upper())

# print title in small letters
print('Small letters title: ', movie.lower())

# print how many times the vowel "e" appears in the title
ilosc_e = movie.count('e')
print('e in the title: ', ilosc_e)

# print where in the text is the word "Lord"
Lord = movie.find('Lord')
print('Lord is at index: ', Lord)

# print where in the text is the word "dragon"
dragon = movie.find('dragon')
print('dragon is at index: ', dragon)