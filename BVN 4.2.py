#Mã hóa thay thế bằng phép toán cộng với k=27 theo danh sách. 
# Plaintext là P=TranHoangBaoKhanh. Theo Z26. 
def encode(plaintext, k):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():  
            shift = k % 26 
            base = ord('A') if char.isupper() else ord('a')
            encoded_char = chr((ord(char) - base + shift) % 26 + base)
            ciphertext += encoded_char
        else:
            ciphertext += char 
    return ciphertext

k=27
plaintext="Tran Hoang Bao Khanh"
print(encode(plaintext, k))