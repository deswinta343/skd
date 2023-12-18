import string

# Fungsi untuk melakukan enkripsi teks input
def encrypt(input):
    res = ""
    key = 24

    # Loop melalui setiap karakter dalam teks input
    for x in range(len(input)):
        char = input[x]

        # Periksa apakah karakter adalah huruf abjad
        if char.isalpha():
            # Jika itu huruf kapital, lakukan enkripsi untuk huruf kapital
            if char.isupper():
                hasil = string.ascii_uppercase.index(char) + key
                hasil = hasil % 26
                res += string.ascii_uppercase[hasil]
            # Jika itu huruf kecil, lakukan enkripsi untuk huruf kecil
            else:
                hasil = string.ascii_lowercase.index(char) + key
                hasil = hasil % 26
                res += string.ascii_lowercase[hasil]
        else:
            # Jika bukan huruf abjad, lakukan enkripsi untuk karakter non-abjad
            ascii_code = ord(char) + key
            if ascii_code > 127:
                ascii_code = ascii_code - 127 + 32
            res += chr(ascii_code)

    return res

# Fungsi untuk melakukan dekripsi teks input
def decrypt(input):
    res = ""
    key = 24

    # Loop melalui setiap karakter dalam teks input
    for x in range(len(input)):
        char = input[x]

        # Periksa apakah karakter adalah huruf abjad
        if char.isalpha():
            # Jika itu huruf kapital, lakukan dekripsi untuk huruf kapital
            if char.isupper():
                hasil = string.ascii_uppercase.index(char) - key
                hasil = hasil % 26
                res += string.ascii_uppercase[hasil]
            # Jika itu huruf kecil, lakukan dekripsi untuk huruf kecil
            else:
                hasil = string.ascii_lowercase.index(char) - key
                hasil = hasil % 26
                res += string.ascii_lowercase[hasil]
        else:
            # Jika bukan huruf abjad, lakukan dekripsi untuk karakter non-abjad
            ascii_code = ord(char) - key
            if ascii_code < 32:
                ascii_code = ascii_code + 127 - 32
            res += chr(ascii_code)

    return res

# Loop program utama
while True:
    print("Pilih operasi:")
    print("1. Enkripsi")
    print("2. Dekripsi")

    # Dapatkan pilihan pengguna
    choice = input("Masukkan pilihan (1/2): ")

    if choice == '1':
        # Enkripsi
        plaintext = input("Masukkan teks yang akan dienkripsi: ")
        encrypted_text = encrypt(plaintext)
        print("Teks terenkripsi:", encrypted_text)
    elif choice == '2':
        # Dekripsi
        encrypted_text = input("Masukkan teks yang akan didekripsi: ")
        decrypted_text = decrypt(encrypted_text)
        print("Teks terdekripsi:", decrypted_text)
    else:
        # Pilihan tidak valid
        print("Pilihan tidak valid.")
