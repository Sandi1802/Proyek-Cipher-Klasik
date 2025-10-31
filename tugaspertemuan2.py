# Vigenere Cipher Implementation
from collections import Counter

# Fungsi enkripsi
def vigenere_encrypt(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")
    key = key.upper()
    ciphertext = ""
    for i in range(len(plaintext)):
        letter = plaintext[i]
        shift = ord(key[i % len(key)]) - 65
        encrypted_char = chr((ord(letter) - 65 + shift) % 26 + 65)
        ciphertext += encrypted_char
    return ciphertext

# Fungsi dekripsi
def vigenere_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper().replace(" ", "")
    key = key.upper()
    plaintext = ""
    for i in range(len(ciphertext)):
        letter = ciphertext[i]
        shift = ord(key[i % len(key)]) - 65
        decrypted_char = chr((ord(letter) - 65 - shift) % 26 + 65)
        plaintext += decrypted_char
    return plaintext

# Analisis frekuensi
def frequency_analysis(text):
    text = text.upper().replace(" ", "")
    freq = Counter(text)
    total = sum(freq.values())
    print("Analisis Frekuensi:")
    for char, count in sorted(freq.items()):
        print(f"{char}: {count} ({count/total:.2%})")

# Contoh penggunaan
plaintext = "KRIPTOGRAFI ADALAH ILMU KEAMANAN INFORMASI"
key = "RAHASIA"

ciphertext = vigenere_encrypt(plaintext, key)
decrypted = vigenere_decrypt(ciphertext, key)

print("Plaintext :", plaintext)
print("Kunci     :", key)
print("Ciphertext:", ciphertext)
print("Dekripsi  :", decrypted)
print()
frequency_analysis(ciphertext)
