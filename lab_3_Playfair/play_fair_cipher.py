class PlayfairCipher:
    def __init__(self, key, additional_letter='X'):
        self.key = self.process_key(key)
        self.matrix = self.create_matrix(self.key)
        
        self.additional_letter = additional_letter

    alphabet = "AĂÂBCDDEFGHHIÎJKLMNOPQRSȘTTUVWXYZ"

    def process_key(self, key):
        key = ''.join(sorted(set(key), key=key.index)).replace(" ",'')  
        key = key.replace('J', 'I')
        key = key.upper()
        return key

    def create_matrix(self, key):
        matrix = list(key)
        for char in self.alphabet:
            if char not in matrix:
                matrix.append(char)

        return [matrix[i:i + 6] for i in range(0, len(matrix), 6)]


    def print_matrix(self):
        text = ''
        for row in self.matrix:
            text += ' '.join(row) + '\n'
        return text

    def prepare_text(self, text):
        text = text.replace('J', 'I').upper()
        prepared_text = ''.join(filter(lambda char: char in self.alphabet, text))
        pairs = []
        i = 0

        while i < len(prepared_text):
            if i + 1 < len(prepared_text):  
                pair = prepared_text[i:i + 2] 
                
                if pair[0] == pair[1]: 
                    pairs.append(pair[0] + self.additional_letter)  
                    i += 1
                else:
                    pairs.append(pair)  
                    i += 2  
            else:  
                pairs.append(prepared_text[i] + self.additional_letter)  
                break

        final_text = ' '.join(pairs).replace(" ", "")
        return final_text


    def encrypt(self, plaintext):
        plaintext = self.prepare_text(plaintext)
        print(plaintext)
        ciphertext = ''
        i = 0
        while i < len(plaintext):
            a = plaintext[i]
            if i + 1 < len(plaintext):
                b = plaintext[i + 1]
            else:
                b = 'X'  
            
            if a == b:
                b = 'X'  
                i += 1
            else:
                i += 2

            a_row, a_col = self.find_position(a)
            b_row, b_col = self.find_position(b)

            if a_row == b_row: 
                ciphertext += self.matrix[a_row][(a_col + 1) % 6]
                ciphertext += self.matrix[b_row][(b_col + 1) % 6]
            elif a_col == b_col: 
                ciphertext += self.matrix[(a_row + 1) % 5][a_col]
                ciphertext += self.matrix[(b_row + 1) % 5][b_col]
            else:  
                ciphertext += self.matrix[a_row][b_col]
                ciphertext += self.matrix[b_row][a_col]
        
        return ciphertext

    def decrypt(self, ciphertext):
        ciphertext = ciphertext.replace(' ', '').upper()
        print(ciphertext)
    
        plaintext = ''
        i = 0
        while i < len(ciphertext):
            a = ciphertext[i]
            if i + 1 < len(ciphertext):
               b = ciphertext[i + 1]
            else:
                b = 'X' 

            a_row, a_col = self.find_position(a)
            b_row, b_col = self.find_position(b)

            if a_row == b_row:  
                plaintext += self.matrix[a_row][(a_col - 1) % 6] 
                plaintext += self.matrix[b_row][(b_col - 1) % 6] 
            elif a_col == b_col: 
                plaintext += self.matrix[(a_row - 1) % 5][a_col]  
                plaintext += self.matrix[(b_row - 1) % 5][b_col]  
            else:  
                plaintext += self.matrix[a_row][b_col]
                plaintext += self.matrix[b_row][a_col]

            i += 2  

        return plaintext

    def find_position(self, char):
        for i, row in enumerate(self.matrix):
            for j, c in enumerate(row):
                if c == char:
                    return i, j
        return -1, -1