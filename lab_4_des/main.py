import random

from constants import EXPANSION_TABLE, PERMUTATION_TABLE, S_BOXES


def binary_to_decimal(binary):
    return int("".join(map(str, binary)), 2)

def decimal_to_binary(value, bits):
    return [int(x) for x in format(value, f'0{bits}b')]

def expand(bits):
    return [bits[i] for i in EXPANSION_TABLE]

def apply_s_boxes(bits):
    output = []
    for i in range(8):  # DES uses 8 S-boxes
        chunk = bits[i * 6:(i + 1) * 6]
        row = (chunk[0] << 1) | chunk[5]
        col = binary_to_decimal(chunk[1:5])
        s_box_value = S_BOXES[i][row][col]
        output.extend(decimal_to_binary(s_box_value, 4))
    return output

def permute(bits):
    return [bits[i] for i in PERMUTATION_TABLE]

def xor(bits1, bits2):
    return [b1 ^ b2 for b1, b2 in zip(bits1, bits2)]

def calculate_rk(L_prev, R_prev, K):
    # Step 1: Expand R_prev
    expanded_r = expand(R_prev)
    print("Expanded R_prev:", expanded_r)
    
    # Step 2: XOR with the key
    xored = xor(expanded_r, K)
    print("XOR with Key:", xored)
    
    # Step 3: Apply S-boxes
    s_box_output = apply_s_boxes(xored)
    print("S-box Output:", s_box_output)
    
    # Step 4: Permute
    permuted = permute(s_box_output)
    print("Permuted Output:", permuted)
    
    # Step 5: Calculate Rk
    Rk = xor(L_prev, permuted)
    return Rk

def get_user_or_random_input(prompt, length):
    choice = input(f"{prompt} (enter manually or type 'random' to generate randomly): ").strip().lower()
    if choice == "random":
        return [random.randint(0, 1) for _ in range(length)]
    else:
        user_input = input(f"Enter {length} bits as a space-separated list (e.g., 1 0 1 ...): ").strip()
        return list(map(int, user_input.split()))

# Main program
if __name__ == "__main__":
    print("DES Round Calculation")
    print("=====================")
    
    # Get inputs for L_prev, R_prev, and K
    L_prev = get_user_or_random_input("Provide L_prev (32 bits)", 32)
    R_prev = get_user_or_random_input("Provide R_prev (32 bits)", 32)
    K = get_user_or_random_input("Provide K (48 bits)", 48)
    
    print("\nInputs:")
    print("L_prev:", L_prev)
    print("R_prev:", R_prev)
    print("Key (K):", K)
    
    # Calculate Rk
    Rk = calculate_rk(L_prev, R_prev, K)
    
    print("\nResult:")
    print("Rk:", Rk)
