def caesar_encrypt(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

# Contoh penggunaan:
if __name__ == "__main__":
    print(caesar_encrypt('HELLO', 3))  # Output: KHOOR
