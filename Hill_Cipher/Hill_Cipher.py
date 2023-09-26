'''
Nama : Dimas Falah Arianto Wibisono
NPM	 : 140810210064
'''

import numpy as np

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def matrix_inverse(matrix, mod):
    det = int(np.linalg.det(matrix))
    det_inv = mod_inverse(det, mod)
    
    if det_inv is None:
        raise ValueError("Matrix is not invertible")
    
    adj_matrix = np.round(det_inv * np.linalg.inv(matrix)).astype(int)
    return adj_matrix % mod

def hill_encrypt(plain_text, key_matrix, mod):
    plain_text = plain_text.replace(' ', '').upper()
    n = len(key_matrix)
    encrypted_text = ""
    
    if len(plain_text) % n != 0:
        plain_text += 'X' * (n - len(plain_text) % n)
    
    for i in range(0, len(plain_text), n):
        block = [ord(char) - ord('A') for char in plain_text[i:i+n]]
        result = np.dot(key_matrix, block) % 26
        encrypted_text += ''.join([chr(char + ord('A')) for char in result])
    
    return encrypted_text

def hill_decrypt(cipher_text, key_matrix, mod):
    n = len(key_matrix)
    key_matrix_inv = matrix_inverse(key_matrix, mod)
    decrypted_text = ""
    
    for i in range(0, len(cipher_text), n):
        block = [ord(char) - ord('A') for char in cipher_text[i:i+n]]
        result = np.dot(key_matrix_inv, block)
        decrypted_text += ''.join([chr((char % 26) + ord('A')) for char in result])
    
    return decrypted_text

def generate_key(n):
    key = np.random.randint(0, 26, size=(n, n))
    while True:
        if gcd(int(np.linalg.det(key)), 26) == 1:
            return key

if __name__ == "__main__":
    mod = 26
    n = 3  # Anda dapat mengganti nilai n sesuai dengan ukuran matriks kunci yang Anda inginkan
    
    key = generate_key(n)
    print("Matriks Kunci:")
    print(key)

    plain_text = input("Masukkan teks yang akan dienkripsi: ")
    encrypted_text = hill_encrypt(plain_text, key, mod)
    
    print("Teks Terenkripsi: " + encrypted_text)

    decrypted_text = hill_decrypt(encrypted_text, key, mod)
    print("Teks Terdekripsi: " + decrypted_text)
