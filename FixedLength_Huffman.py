def huffman_fixed_length_size(text, encoding_dict):
    total_bits = 0

    for char in text:
        total_bits += len(encoding_dict[char])

    return total_bits

# Example usage
text = "tmnsourp"
bits_per_character = 3

# Replace the dictionary below with the actual Huffman encoding you have
# For this example, we assume a fixed-length encoding
encoding_dict = {
    't': '000',
    'm': '001',
    'n': '01',
    's': '100',
    'o': '101',
    'u': '1100',
    'r': '1101',
    'p': '111'
}

total_bits = huffman_fixed_length_size(text, encoding_dict)

print(f"The total size using fixed-length Huffman encoding is: {total_bits} bits")
