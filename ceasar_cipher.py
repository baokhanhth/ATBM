# Cho k= 27 , và Plaintext = TranHoangBaoKhanh. Hãy mã hóa theo thuật toán Ceasar. 
# Bằng ngôn ngữ Python và đưa lên Github. 

def caesar_cipher(plaintext, shift):
    ciphertext = ""
    shift_amount = shift % 26  

    for char in plaintext:
        if char.isupper(): 
            new_char = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
            ciphertext += new_char
        elif char.islower():  
            new_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            ciphertext += new_char
        else:  
            ciphertext += char

    return ciphertext

k = 27
plaintext = "TranHoangBaoKhanh"
ciphertext = caesar_cipher(plaintext, k)
print("Ciphertext:", ciphertext)
