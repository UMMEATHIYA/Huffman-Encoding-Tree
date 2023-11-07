import heapq

class Node:
    def __init__(self, freq, char=None):
        self.freq = freq
        self.char = char
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_dict):
    priority_queue = [Node(freq, char) for char, freq in freq_dict.items()]
    heapq.heapify(priority_queue)
    
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        parent = Node(left.freq + right.freq)
        parent.left = left
        parent.right = right
        heapq.heappush(priority_queue, parent)
    
    return priority_queue[0]

def generate_huffman_codes(node, code="", code_dict={}):
    if node is not None:
        if node.char is not None:
            code_dict[node.char] = code
        generate_huffman_codes(node.left, code + "0", code_dict)
        generate_huffman_codes(node.right, code + "1", code_dict)
    return code_dict

# Input frequencies
freq_dict = {
    'a': 20,
    'b': 35,
    'c': 12,
    'd': 30,
    'e': 55,
    'f': 25,
    'g': 5,
    'h': 21
}

# Build Huffman tree
root = build_huffman_tree(freq_dict)

# Generate Huffman codes
huffman_codes = generate_huffman_codes(root)

# Print Huffman codes
for char, code in huffman_codes.items():
    print(f"{char}: {code}")
