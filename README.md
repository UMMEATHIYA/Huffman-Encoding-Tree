# Huffman Encoding Tree

This repository contains a Python implementation of the Huffman Encoding algorithm. Huffman Encoding is a widely used algorithm for lossless data compression. It works by creating a variable-length encoding scheme for characters based on their frequencies.

## Table of Contents
- [Introduction](#introduction)
- [Usage](#usage)
- [Implementation Details](#implementation-details)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Huffman Encoding is a technique used for data compression. It creates a variable-length encoding scheme for characters based on their frequencies. This allows more frequent characters to have shorter codes, resulting in a more efficient encoding.

## Usage

To use this implementation, simply clone the repository and run the Python code provided. You can modify the input frequencies and customize the code as needed for your specific use case.

## Implementation Details

The implementation includes the following components:
- `Node`: A class representing nodes in the Huffman tree.
- `build_huffman_tree`: Function to build the Huffman tree from given character frequencies.
- `generate_huffman_codes`: Function to generate Huffman codes for each character.

## Example

```python
# Example usage
freq_dict = {
    'm': 32,
    'n': 76,
    'o': 45,
    'p': 56,
    'r': 28,
    's': 40,
    't': 30,
    'u': 18
}

root = build_huffman_tree(freq_dict)
huffman_codes = generate_huffman_codes(root)

for char, code in huffman_codes.items():
    print(f"{char}: {code}")
