#!/usr/bin/env python3
# Soubor:  caesar.py
# Datum:   02.10.2018 00:36
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
############################################################################


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 

def decrypt():
    
    print("Welcome to Caesar Cipher Decryption.\n")
    encrypted_message = input("Enter the message you would like to decrypt: ").strip()
    print()
    key = int(input("Enter key to decrypt: "))
    
    decrypted_message = ""

    for c in encrypted_message:

        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - key) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c

    print("\nDecrypting your message...\n") 
    print("Your decrypted message is:\n")
    print(decrypted_message)

decrypt()