def generate_table(key):
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # tanpa J
    table = ''
    for c in key.upper() + alphabet:
        if c not in table:
            table += c
    return [table[i:i+5] for i in range(0, 25, 5)]

# Contoh pembuatan tabel:
table = generate_table('KEYWORD')
for row in table:
    print(row)
