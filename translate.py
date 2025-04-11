#!/usr/bin/env python3 


def subsitution_cipher():

    #get user input 
    plaintext = input("Plain alphabet? ").lower()
    print()
    ciphertext = input("Cipher alphabet? ").lower()
    print()
    message = input("Message? ").lower()
    print()

    # Initialize results
    encrypted_msg = ""
    encrypted_cnt = 0
    total_cnt = 0

    # Loop through the message 
    for char in message: 
        total_cnt += 1
        if char in plaintext:
            index = plaintext.index(char)
            cipher_char = ciphertext[index]
            encrypted_msg += cipher_char
            encrypted_cnt += 1
        else:
            encrypted_msg += char

    # Output the results
    print(encrypted_msg)
    print(f"Encrypted {encrypted_cnt} characters out of {total_cnt} characters")

# Run the function 
subsitution_cipher()