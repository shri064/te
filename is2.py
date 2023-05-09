def encrypt_transposition(plaintext, key):
    num_cols = len(key)
    num_rows = (len(plaintext) + num_cols - 1) // num_cols
    
    plaintext += ' ' * (num_rows * num_cols - len(plaintext))
    
    matrix = [[''] * num_cols for i in range(num_rows)]
    
    row = 0
    col = 0
    for char in plaintext:
        matrix[row][col] = char
        col += 1
        if col == num_cols:
            col = 0
            row += 1
    
    ciphertext = ''
    for col in key:
        for row in range(num_rows):
            ciphertext += matrix[row][col]
    
    return ciphertext


def decrypt_transposition(ciphertext, key):
    num_cols = len(key)
    num_rows = (len(ciphertext) + num_cols - 1) // num_cols
    
    matrix = [[''] * num_cols for i in range(num_rows)]
    
    num_empty = num_rows * num_cols - len(ciphertext)
    
    empty_positions = [(num_rows-1, col) for col in range(num_cols-1, num_cols-1-num_empty, -1)]
    
    pos = 0
    for col in key:
        for row in range(num_rows):
            if (row, col) not in empty_positions:
                matrix[row][col] = ciphertext[pos]
                pos += 1
    
    plaintext = ''
    for row in range(num_rows):
        for col in range(num_cols):
            if (row, col) not in empty_positions:
                plaintext += matrix[row][col]
    
    return plaintext

plaintext = "Shrihari"
key = [0, 1, 2, 3]
enc = encrypt_transposition(plaintext, key)
dec = decrypt_transposition(enc, key)
print("The cipher text is : ",enc)
# print("\n")
print("The plaintext is : ",dec)
