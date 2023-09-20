def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Hanya enkripsi huruf
            # Tentukan apakah huruf adalah huruf besar atau huruf kecil
            is_upper = char.isupper()
            
            # Ubah huruf menjadi indeks dalam alfabet (0-25)
            if is_upper:
                offset = ord('A')
            else:
                offset = ord('a')
            
            # Enkripsi dengan menggeser huruf
            char_code = ord(char) - offset
            encrypted_char = chr((char_code + shift) % 26 + offset)
            
            result += encrypted_char
        else:
            # Jika bukan huruf, biarkan tidak berubah
            result += char
    
    return result

def decrypt(text, shift):
    # Dekripsi adalah enkripsi dengan geseran negatif
    return encrypt(text, -shift)

# Contoh penggunaan
text = "Dimas Falah"
shift = 20
encrypted_text = encrypt(text, shift)
print("Pesan terenkripsi:", encrypted_text)

decrypted_text = decrypt(encrypted_text, shift)
print("Pesan terdekripsi:", decrypted_text)
