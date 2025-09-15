# Cho k= 27 , và Plaintext = TranHoangBaoKhanh. Hãy mã hóa theo thuật toán Ceasar. 
# Bằng ngôn ngữ Python và đưa lên Github. 

def caesar_cipher(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr(((ord(char) - 65 + shift_amount) % 26) + 65)
            ciphertext += new_char
        else:
            ciphertext += char
    return ciphertext

k = 27
plaintext = "TranHoangBaoKhanh"
ciphertext = caesar_cipher(plaintext, k)
print("Ciphertext:", ciphertext)