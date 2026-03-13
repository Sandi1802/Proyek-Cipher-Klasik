"""
Hello World - Demonstrasi Cipher Klasik
Menunjukkan enkripsi pesan "HALLO" menggunakan berbagai cipher klasik.
"""

from caesar import caesar_encrypt
from AffineCipher import affine_encrypt
from tugaspertemuan2 import vigenere_encrypt, vigenere_decrypt


def demo():
    message = "HALLO"
    print("=" * 40)
    print("  Demonstrasi Cipher Klasik")
    print("=" * 40)
    print(f"\nPesan asli: {message}\n")

    # Caesar Cipher
    caesar_result = caesar_encrypt(message, 3)
    print(f"Caesar Cipher (shift=3)  : {caesar_result}")

    # Affine Cipher
    affine_result = affine_encrypt(message, 5, 8)
    print(f"Affine Cipher (a=5, b=8) : {affine_result}")

    # Vigenere Cipher
    key = "KUNCI"
    vigenere_enc = vigenere_encrypt(message, key)
    vigenere_dec = vigenere_decrypt(vigenere_enc, key)
    print(f"Vigenere Cipher (key={key}): {vigenere_enc}")
    print(f"  Dekripsi               : {vigenere_dec}")

    print("\n" + "=" * 40)


if __name__ == "__main__":
    demo()
