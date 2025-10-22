
SYMBOLS ='ABCDEFGHIJKLMNOPRSTUVWXYZ'

while True:
    print("Do you want to (e)ncrypt or (d)ecrypt your text?")
    response = input("> ").lower()
    if response.startswith("e"):
        mode = 'encrypt'
        break
    elif response.startswith("d"):
        mode = 'decrypt'
        break
    print("Please provide 'e' to encrypt or 'd' to decrypt.")

while True:
    print("Enter the encryption key – a number from 1 to 26.")
    key_user = input("> ")
    if 0 < int(key_user) <= 26:
        key = int(key_user)
        break

print(f"Enter the message to {mode}.")
message = input("> ").upper()

translated = ''

for letter in message:
    if letter in SYMBOLS:
        num = SYMBOLS.find(letter)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        translated = translated + SYMBOLS[num]

    else:
        translated = translated + letter

print(translated)

