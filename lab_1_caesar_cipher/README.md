# Laboratory 1: Caesar Cipher Implementation

## Objective
The objective of this laboratory is to implement the **Caesar cipher**, a simple encryption technique where each letter in the plaintext is shifted by a fixed number of places in the alphabet. This laboratory aims to explore the mechanics of the Caesar cipher, its vulnerabilities, and the concept of enhancing its security through keyword-based permutations.

## Key Concepts

### Encryption and Decryption
The formulas for encryption and decryption are defined as follows:

- **Encryption**: 
  \[
  c = e_k(x) = (x + k) \mod n
  \]
  
- **Decryption**: 
  \[
  m = d_k(y) = (y - k) \mod n
  \]

  Where:
  - \( k \) is the shift key.
  - \( n \) is the number of letters in the alphabet.

### Character Mapping
Each letter is represented by a numeric value:
- 'A' = 0
- 'B' = 1
- ...
- 'Z' = 25

### Keyspace
The keyspace for the standard Caesar cipher consists of 25 possible keys (1-25).

### Brute Force Attack
The weakness of the Caesar cipher lies in its limited keyspace, making it susceptible to brute force attacks where all possible keys are tested until meaningful text is found.

## Tasks

### Task 1.1
Implement the basic Caesar cipher for the English alphabet. The program should:
- Accept a key between 1 and 25.
- Only allow characters between 'A' and 'Z', converting all input to uppercase and removing spaces.
- Provide options for encryption and decryption.

### Task 1.2
Extend the implementation to incorporate a second key, allowing for a permutation of the alphabet based on a keyword. The program should:
- Accept a keyword with a minimum length of 7 letters.
- Ensure the keyword only contains unique letters of the Latin alphabet.
- Apply the Caesar cipher using both the shift key and the permuted alphabet.

