import unittest
from caesar_cipher_with_two_keys import generate_permuted_alphabet, caesar_cipher_with_two_keys



class TestCaesarCipherWithTwoKeys(unittest.TestCase):

    def test_generate_permuted_alphabet(self):
        self.assertEqual(generate_permuted_alphabet("KEYBOARD"), "KEYBOARDCFGHIJLMNPQSTUVWXZ")
        self.assertEqual(generate_permuted_alphabet("abcdefg"), "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(generate_permuted_alphabet("AAABBBCCC"), "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    
    def test_caesar_cipher_with_two_keys_encrypt(self):
        # Test simple encryption case
        result = caesar_cipher_with_two_keys("HELLO", 3, "KEYBOARD", "encrypt")
        self.assertEqual(result, "LOPPD")  # Expected encrypted result
        
        result = caesar_cipher_with_two_keys("WORLD", 4, "SECURITY", "encrypt")
        self.assertEqual(result, "EWAPJ")  # Expected encrypted result
    
    def test_caesar_cipher_with_two_keys_decrypt(self):
        # Test simple decryption case
        result = caesar_cipher_with_two_keys("LOPPD", 3, "KEYBOARD", "decrypt")
        self.assertEqual(result, "HELLO")  # Expected decrypted result
        
        result = caesar_cipher_with_two_keys("EWAPJ", 4, "SECURITY", "decrypt")
        self.assertEqual(result, "WORLD")  # Expected decrypted result

    def test_invalid_key1(self):
        # Test for invalid key1 values outside the range of 1-25
        with self.assertRaises(ValueError):
            caesar_cipher_with_two_keys("HELLO", 0, "KEYBOARD", "encrypt")
        
        with self.assertRaises(ValueError):
            caesar_cipher_with_two_keys("HELLO", 26, "KEYBOARD", "encrypt")
    
    def test_invalid_character_in_text(self):
        # Test to raise error when text contains invalid characters (not A-Z)
        with self.assertRaises(ValueError):
            caesar_cipher_with_two_keys("HELLO1", 3, "KEYBOARD", "encrypt")
        
        with self.assertRaises(ValueError):
            caesar_cipher_with_two_keys("HELLO!", 3, "KEYBOARD", "encrypt")
    
    def test_invalid_operation(self):
        # Test to raise error for invalid operation
        with self.assertRaises(ValueError):
            caesar_cipher_with_two_keys("HELLO", 3, "KEYBOARD", "invalid_op")


