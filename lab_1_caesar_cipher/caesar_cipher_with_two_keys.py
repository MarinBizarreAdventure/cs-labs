from caesar_cipher import get_valid_key, get_valid_text


def generate_permuted_alphabet(key2):
    key2 = ''.join(dict.fromkeys(key2.upper()))
    standard_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    remaining_letters = ''.join([char for char in standard_alphabet if char not in key2])
    return key2 + remaining_letters



def caesar_cipher_with_two_keys(text, key1, key2, operation):
    permuted_alphabet = generate_permuted_alphabet(key2)
    standard_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    text = text.upper().replace(" ", "")
    
    if not (0 < key1 < 26):
        raise ValueError("Key 1 must be between 1 and 25.")
    
    result = ''

    for char in text:
        if char not in standard_alphabet:
            raise ValueError(f"Invalid character '{char}' in text. Only letters A-Z are allowed.")

        char_index = permuted_alphabet.index(char)

        if operation == 'encrypt':
            new_index = (char_index + key1) % 26
        elif operation == 'decrypt':
            new_index = (char_index - key1) % 26
        else:
            raise ValueError("Invalid operation. Use 'encrypt' or 'decrypt'.")
        
        result += permuted_alphabet[new_index]

    return result

def get_valid_key2():
    while True:
        key2 = input("Enter key 2 (Latin letters, at least 7 characters): ")
        if key2.isalpha() and len(key2) >= 7:
            return key2
        else:
            print("Key 2 must contain only Latin letters and have a minimum length of 7.")

def caesar_cipher_problem_two_keys():
    print("Caesar Cipher with Two Keys")

    while True:
        operation = input("Choose operation ('encrypt' or 'decrypt'): ").lower()
        if operation in ['encrypt', 'decrypt']:
            break
        else:
            print("Invalid operation. Please enter 'encrypt' or 'decrypt'.")
    
    key1 = get_valid_key()
    key2 = get_valid_key2().upper()
    text = get_valid_text()

    result = caesar_cipher_with_two_keys(text, key1, key2, operation)

    if operation == 'encrypt':
        print("Encrypted text:", result)
    else:
        print("Decrypted text:", result)


