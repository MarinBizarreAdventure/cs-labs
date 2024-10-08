import unittest
from caesar_cipher import caesar_ciper

class TestCaesarCipher(unittest.TestCase):

    def test_encrypt(self):
        # Test case for encryption
        text = "HELLO"
        key = 3
        result = caesar_ciper(text, key, "encrypt")
        expected = "KHOOR"
        self.assertEqual(result, expected)

    def test_decrypt(self):
        # Test case for decryption
        text = "KHOOR"
        key = 3
        result = caesar_ciper(text, key, "decrypt")
        expected = "HELLO"
        self.assertEqual(result, expected)

    def test_encrypt_with_spaces(self):
        # Test case for encryption with spaces
        text = "HELLO WORLD"
        key = 5
        result = caesar_ciper(text, key, "encrypt")
        expected = "MJQQTBTWQI"
        self.assertEqual(result, expected)

    def test_decrypt_with_spaces(self):
        # Test case for decryption with spaces
        text = "MJQQT BTWQI"
        key = 5
        result = caesar_ciper(text, key, "decrypt")
        expected = "HELLOWORLD"
        self.assertEqual(result, expected)

    def test_invalid_character(self):
        # Test case for invalid character in the text
        with self.assertRaises(ValueError):
            caesar_ciper("HELLO123", 3, "encrypt")

    def test_invalid_key(self):
        # Test case for invalid key
        with self.assertRaises(ValueError):
            caesar_ciper("HELLO", 30, "encrypt")

    def test_invalid_operation(self):
        # Test case for invalid operation
        with self.assertRaises(ValueError):
            caesar_ciper("HELLO", 3, "invalid_operation")