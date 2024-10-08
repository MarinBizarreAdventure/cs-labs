
def caesar_ciper(text, key, operation):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    text = text.upper().replace(" ","")

    if not (0 < key < 26):
        raise ValueError("key must between 1 and 25")
    
    result = ''

    for char in text:
        if char not in alphabet:
            raise ValueError(f"Invalid character '{char}' in text. only capital letters are allowed A - Z")
        
        char_index = alphabet.index(char)

        if operation == "encrypt":
            new_index = (char_index + key)%26
        elif operation == "decrypt":
            new_index = (char_index - key)%26
        else:
            raise ValueError("Invalid operation. Use 'encrypt' or 'decrypt'.")
        

        result += alphabet[new_index]

    return result


def get_valid_key():
    while True:
        try:
            key = int(input("Enter a key (1-25):"))
            if 0 < key < 26:
                return key
            else:
                print("key must be between 1-25")
        except ValueError:
            print("Invalid Input, enter a number between 1-25")



def get_valid_text():
    while True:
        text = input("Enter the message or cryptogram (A-z and spaces):")
        if all(c.isalpha() or c.isspace() for c in text):
            return text
        else:
            print("Text can only contain letters A-Z or a-z and spaces.")


def caesar_chipher_problem():
    print("Caesar chipher")

    while True:
        operation = input("Choose operation ('encrypt' or 'decrypt'): ").lower()
        if operation in ['encrypt', 'decrypt']:
            break
        else:
            print("Invalid operation. Please enter 'encrypt' or 'decrypt'.")
    
    key = get_valid_key()
    text = get_valid_text()
    result = caesar_ciper(text, key, operation)

    if operation == 'encrypt':
        print("Encrypted text:", result)
    else:
        print("Decrypted text:", result)

