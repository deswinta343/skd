def generate_playfair_matrix(key):
  # Membuat tabel Playfair berdasarkan kunci
  alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Tanpa J untuk Playfair
  key = key.upper().replace("J", "I")  # Mengganti J dengan I dan ubah menjadi huruf kapital
  key_set = set()
  matrix = []

  for char in key:
      if char not in key_set and char in alphabet:
          key_set.add(char)
          alphabet = alphabet.replace(char, "")
          matrix.append(char)

  for char in alphabet:
      matrix.append(char)

  return matrix

def prepare_text(text):
  # Ubah teks menjadi bigram
  text = text.upper().replace("J", "I")
  text = text.replace(" ", "")
  # Memisahkan bigram yang sama dengan X
  i = 0
  while i < len(text) - 1:
      if text[i] == text[i + 1]:
          text = text[:i + 1] + 'X' + text[i + 1:]
      i += 2
  # Jika panjangnya ganjil, tambahkan 'X' di akhir
  if len(text) % 2 == 1:
      text += 'X'

  return [text[i:i+2] for i in range(0, len(text), 2)]

def playfair_encrypt(text, key):
  matrix = generate_playfair_matrix(key)
  bigrams = prepare_text(text)
  encrypted_text = ""

  for bigram in bigrams:
      row1, col1 = divmod(matrix.index(bigram[0]), 5)
      row2, col2 = divmod(matrix.index(bigram[1]), 5)

      if row1 == row2:
          encrypted_text += matrix[row1 * 5 + (col1 + 1) % 5]
          encrypted_text += matrix[row2 * 5 + (col2 + 1) % 5]
      elif col1 == col2:
          encrypted_text += matrix[((row1 + 1) % 5) * 5 + col1]
          encrypted_text += matrix[((row2 + 1) % 5) * 5 + col2]
      else:
          encrypted_text += matrix[row1 * 5 + col2]
          encrypted_text += matrix[row2 * 5 + col1]

  return encrypted_text

# Teks asli dan kunci
plaintext = "Hari kamis libur nasional"
key = "kuliah libur"

# Enkripsi pesan dengan menggunakan metode Playfair cipher
encrypted_text = playfair_encrypt(plaintext, key)
print("Pesan Terenkripsi:", encrypted_text)
