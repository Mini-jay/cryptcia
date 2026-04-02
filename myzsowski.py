def myszowski_encrypt(plaintext, keyword):
    plaintext = plaintext.replace(" ", "").upper()
    keyword = keyword.upper()
    ranks = []
    sorted_key = sorted(list(keyword))
    for char in keyword:
        ranks.append(sorted_key.index(char))
    width = len(keyword)
    grid = [plaintext[i:i + width] for i in range(0, len(plaintext), width)]
    ciphertext = ""
    unique_ranks = sorted(list(set(ranks)))
    for r in unique_ranks:
        indices = [i for i, val in enumerate(ranks) if val == r]
        if len(indices) == 1:
            col_idx = indices[0]
            for row in grid:
                if col_idx < len(row):
                    ciphertext += row[col_idx]
        else:
            for row in grid:
                for col_idx in indices:
                    if col_idx < len(row):
                        ciphertext += row[col_idx]
    return ciphertext

def myszowski_decrypt(ciphertext, keyword):
    keyword = keyword.upper()
    num_cols = len(keyword)
    num_rows = (len(ciphertext) + num_cols - 1) // num_cols
    ranks = []
    sorted_key = sorted(list(keyword))
    for char in keyword:
        ranks.append(sorted_key.index(char))
    unique_ranks = sorted(list(set(ranks)))
    grid = [['' for _ in range(num_cols)] for _ in range(num_rows)]
    current_pos = 0
    for r in unique_ranks:
        indices = [i for i, val in enumerate(ranks) if val == r]
        if len(indices) == 1:
            col_idx = indices[0]
            for row_idx in range(num_rows):
                if row_idx * num_cols + col_idx < len(ciphertext):
                    grid[row_idx][col_idx] = ciphertext[current_pos]
                    current_pos += 1
        else:
            for row_idx in range(num_rows):
                for col_idx in indices:
                    if row_idx * num_cols + col_idx < len(ciphertext):
                        grid[row_idx][col_idx] = ciphertext[current_pos]
                        current_pos += 1
    plaintext = ""
    for row in grid:
        plaintext += "".join(row)
    return plaintext