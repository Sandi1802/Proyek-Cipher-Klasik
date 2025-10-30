import numpy as np

def hill_encrypt(text, key):
    text = text.upper().replace(" ", "")
    if len(text) % 2 != 0:  # Tambah X kalau ganjil
        text += "X"
    result = ""
    for i in range(0, len(text), 2):
        pair = np.array([ord(text[i]) - 65, ord(text[i+1]) - 65])
        enc = np.dot(key, pair) % 26
        result += chr(enc[0] + 65) + chr(enc[1] + 65)
    return result

key = np.array([[3, 3], [2, 5]])  # Matriks kunci
print(hill_encrypt("HELLO", key))
