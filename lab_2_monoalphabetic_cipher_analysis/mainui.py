import streamlit as st
from collections import Counter, defaultdict
import matplotlib.pyplot as plt
import pandas as pd


english_frequency = {
    'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75,
    'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78,
    'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97,
    'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15,
    'Q': 0.10, 'Z': 0.07
}


def plot_frequencies(english_freq, cipher_freq):
    fig, axs = plt.subplots(1, 2, figsize=(14, 6))

    axs[0].bar(english_freq.keys(), english_freq.values(), color='blue', alpha=0.7)
    axs[0].set_title("English Letter Frequencies")
    axs[0].set_xlabel("Letters")
    axs[0].set_ylabel("Frequency (%)")

    axs[1].bar(cipher_freq.keys(), cipher_freq.values(), color='red', alpha=0.7)
    axs[1].set_title("Cipher Text Letter Frequencies")
    axs[1].set_xlabel("Letters")
    axs[1].set_ylabel("Frequency (%)")

    plt.tight_layout()
    return fig



def substitution_cipher_interface(cipher_frequency, initial_decrypted_text):
    if 'substitution_dict' not in st.session_state:
        st.session_state.substitution_dict = {}
    if 'decrypted_text' not in st.session_state:
        st.session_state.decrypted_text = initial_decrypted_text

    while True:
        char_to_change = st.text_input("Enter the letter you want to change (or leave blank to finalize):").strip()

        if char_to_change == "":
            break  

        char_substitute = st.text_input(f"Substitute '{char_to_change}' with:", key=f"sub_{char_to_change}").strip()
        
        if char_substitute:
            st.session_state.substitution_dict[char_to_change] = char_substitute

            updated_text = st.session_state.decrypted_text.replace(char_to_change, char_substitute)
            st.session_state.decrypted_text = updated_text

            st.subheader("Updated Decrypted Text")
            st.write(st.session_state.decrypted_text)

            words = st.session_state.decrypted_text.split()
            length_groups = defaultdict(list)
            for word in words:
                length_groups[len(word)].append(word)

            st.subheader("Words Sorted by Length")
            for length in sorted(length_groups):
                st.write(f"{length}-letter words: " + ", ".join(length_groups[length]))

            words_with_sub = [word for word in words if char_substitute in word]
            words_with_sub_sorted = sorted(words_with_sub, key=len)
            st.subheader(f"Words Containing '{char_substitute}'")
            st.write(", ".join(words_with_sub_sorted))
        else:
            st.warning("Please enter a substitute letter.")

    st.success("Substitution finalized. You can start over by refreshing the page.")

st.title("Character Frequency Analysis and Substitution Tool")


encrypted_text = st.text_area("Enter the encrypted text here:")


if encrypted_text:

    filtered_text = ''.join([char for char in encrypted_text if char.isalpha()]).upper()
    text_length = len(filtered_text)


    frequency_counter = Counter(filtered_text)
    cipher_frequency = {char: (count / text_length) * 100 for char, count in frequency_counter.items()}


    sorted_english_freq = dict(sorted(english_frequency.items(), key=lambda item: item[1], reverse=True))
    sorted_cipher_freq = dict(sorted(cipher_frequency.items(), key=lambda item: item[1], reverse=True))

    
    st.subheader("Character Frequencies in Encrypted Text")
    st.write("English Frequency vs. Cipher Frequency")
    fig = plot_frequencies(english_frequency, sorted_cipher_freq)
    st.pyplot(fig)
    
    st.subheader("Character Substitution")
    decrypted_text = encrypted_text.upper()
    substitution_dict = {}

    substitution_cipher_interface(cipher_frequency, decrypted_text)
