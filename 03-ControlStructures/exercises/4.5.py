###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    code = ord(char)
    code = code + 1 
    encrypted_char = chr(code)
    encrypted_text = encrypted_text + encrypted_char
print(f'plain_text: {plain_text}')
print(f'encrypted_text: {encrypted_text}')