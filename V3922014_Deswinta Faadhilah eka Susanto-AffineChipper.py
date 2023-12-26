# Fungsi untuk mengenkripsi menggunakan Affine Cipher
def affine_encrypt(text, a, b):
    result = ""
    for char in text:
        if char.isalpha():  # Hanya proses huruf alfabet
            if char.isupper():
                result += chr(((a * (ord(char) - 65) + b) % 26) + 65)
            else:
                result += chr(((a * (ord(char) - 97) + b) % 26) + 97)
        else:
            result += char
    return result

# Fungsi untuk mendekripsi menggunakan Affine Cipher
def affine_decrypt(text, a, b):
    result = ""
    # Menghitung invers modular dari a
    m_inv = 0
    for i in range(26):
        if (a * i) % 26 == 1:
            m_inv = i
            break
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr(((m_inv * (ord(char) - 65 - b)) % 26) + 65)
            else:
                result += chr(((m_inv * (ord(char) - 97 - b)) % 26) + 97)
        else:
            result += char
    return result

# Plaintext yang akan dienkripsi
plaintext = "deswinta"

# Kunci A dan B
A = 3
B = 5

# Enkripsi plaintext
encrypted_text = affine_encrypt(plaintext, A, B)
print("Plaintext setelah dienkripsi:", encrypted_text)

# Dekripsi ciphertext
decrypted_text = affine_decrypt(encrypted_text, A, B)
print("Ciphertext setelah didekripsi:", decrypted_text)
