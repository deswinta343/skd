from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def encrypt_AES(key, plaintext):
    # Inisialisasi objek AES dengan mode ECB (untuk demonstrasi)
    cipher = AES.new(key.encode(), AES.MODE_ECB)

    # Padding plaintext agar panjangnya menjadi kelipatan 16
    padded_plaintext = pad(plaintext.encode(), AES.block_size)

    # Melakukan enkripsi plaintext
    ciphertext = cipher.encrypt(padded_plaintext)

    # Mengembalikan hasil enkripsi dalam bentuk base64
    return base64.b64encode(ciphertext).decode()

def decrypt_AES(key, ciphertext):
    # Inisialisasi objek AES dengan mode ECB (untuk demonstrasi)
    cipher = AES.new(key.encode(), AES.MODE_ECB)

    # Melakukan dekripsi ciphertext yang telah dienkripsi
    decrypted_text = cipher.decrypt(base64.b64decode(ciphertext))

    # Menghapus padding dari decrypted text
    unpadded_text = unpad(decrypted_text, AES.block_size)

    # Mengembalikan plaintext yang sudah didekripsi
    return unpadded_text.decode()

# Kunci dan plaintext
key = 'silaturahmi'
plaintext = 'kelompokenam'

# Melakukan enkripsi
encrypted_text = encrypt_AES(key, plaintext)
print(f"Hasil Enkripsi: {encrypted_text}")

# Melakukan dekripsi
decrypted_text = decrypt_AES(key, encrypted_text)
print(f"Hasil Dekripsi: {decrypted_text}")
