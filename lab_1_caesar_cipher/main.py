from caesar_cipher import get_valid_key, get_valid_text, caesar_ciper, caesar_chipher_problem 
from test_caesar_cipher import TestCaesarCipher
from caesar_cipher_with_two_keys import caesar_cipher_problem_two_keys,get_valid_key2




def main():
    print("Welcome to the Caesar Cipher Program!")
    while True:
        print("\nChoose the type of Caesar Cipher:")
        print("1. Caesar Cipher with One Key")
        print("2. Caesar Cipher with Two Keys")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            caesar_chipher_problem()
        elif choice == '2':
            caesar_cipher_problem_two_keys()

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")



if __name__ == "__main__":
    main()