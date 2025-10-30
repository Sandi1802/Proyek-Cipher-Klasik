def affine_encrypt(text, a, b):
    result = ''
    for char in text.upper():
        if char.isalpha():
            result += chr(((a * (ord(char) - 65) + b) % 26) + 65)
        else:
            result += char
    return result

# Contoh penggunaan:
print(affine_encrypt('HELLO', 5, 8))  # Output: RCLLA
