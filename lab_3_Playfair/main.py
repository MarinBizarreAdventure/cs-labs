import streamlit as st
from play_fair_cipher import PlayfairCipher

def main():
    st.title("Playfair Cipher for Romanian Alphabet (31 Letters)")

    key = st.text_input("Enter a key (minimum length 7):")

    if len(key) < 7 and key:
        st.warning("Key length must be at least 7 characters.")
        return

    cipher = PlayfairCipher(key, additional_letter='X')

    st.subheader("Cipher Matrix:")
    cipher_matrix = cipher.print_matrix()  
    st.text(cipher_matrix)

    operation = st.selectbox("Choose operation - Encrypt (E) or Decrypt (D):", ['E', 'D'])

    text = st.text_area("Enter the text (letters A-Z only):")

    if st.button("Process"):
        if operation == 'E':
            encrypted_text = cipher.encrypt(text)
            st.success(f"Encrypted Text: {encrypted_text}")
        else:
            decrypted_text = cipher.decrypt(text)
            st.success(f"Decrypted Text: {decrypted_text}")

    if st.button("Reset"):
        st.experimental_rerun()



if __name__ == "__main__":
    main()
