from collections import Counter
import heapq
import docx2txt
import math

# Node class for the Huffman tree
class Node:
    def __init__(self, char=None, frequency=0, left=None, right=None):
        self.char = char
        self.frequency = frequency
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.frequency < other.frequency

# Step 1: Load the .docx file.
def load_docx(file_path):
    """Read content from a .docx file using docx2txt."""
    try:
        return docx2txt.process(file_path)
    except Exception as e:
        print(f"Error loading file: {e}")
        return ""

# Step 2: Preprocess the text.
def preprocess_text(text):
    """
    Convert text to lowercase and remove newline characters.
    All other symbols and characters are allowed.
    """
    # Convert to lowercase.
    text = text.lower()
    # Remove newline characters.
    text = text.replace("\n", "") 
    return text

# Step 3: Analyze character frequencies.
def calculate_frequencies(text):
    """Count the frequency of each character in the text."""
    return Counter(text)

# Step 4: Calculate probabilities.
def calculate_probabilities(frequencies):
    """Calculate the probability of each character."""
    total_characters = sum(frequencies.values())
    probabilities = {char: freq / total_characters for char, freq in frequencies.items()}
    return probabilities

# Step 5: Calculate entropy.
def calculate_entropy(probabilities):
    """Calculate the entropy of the alphabet."""
    entropy = -sum(p * math.log2(p) for p in probabilities.values() if p > 0)
    return entropy

# Step 6: Build Huffman tree.
def build_huffman_tree(frequencies):
    """Build the Huffman tree using a priority queue."""
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(frequency=left.frequency + right.frequency, left=left, right=right)
        heapq.heappush(heap, merged)

    return heap[0]

# Step 7: Generate Huffman codes.
def generate_huffman_codes(node, code="", codes=None):
    """Generate Huffman codes by traversing the tree."""
    if codes is None:
        codes = {}
    if node.char is not None:
        codes[node.char] = code
    if node.left:
        generate_huffman_codes(node.left, code + "0", codes)
    if node.right:
        generate_huffman_codes(node.right, code + "1", codes)
    return codes

# Step 8: Calculate NASCII.
def calculate_nascii(total_characters):
    """Calculate the number of bits needed to encode the text using ASCII."""
    return total_characters * 8

# Step 9: Calculate the average number of bits (bits/character).
def calculate_average_bits(probabilities, huffman_codes):
    """Calculate the average number of bits per character using Huffman code."""
    return sum(probabilities[char] * len(code) for char, code in huffman_codes.items())

# Step 10: Calculate NHUFFMAN. 
def calculate_nhuffman(frequencies, huffman_codes):
    """Calculate the total number of bits needed to encode the text using Huffman code."""
    return sum(frequencies[char] * len(code) for char, code in huffman_codes.items())

# Step 11: Calculate compression percentage.
def calculate_compression_percentage(nascii, nhuffman):
    """Calculate the percentage of compression accomplished by Huffman encoding."""
    return ((nascii - nhuffman) / nascii) * 100

# Print the frequency in tabular format.
def print_results(frequencies, probabilities, huffman_codes):
    """Print the frequencies, probabilities, and Huffman codes in alphabetical order."""
    print("------------------------------------------------------------------------")
    print("|   Symbol  |  Frequency | Probability |  Huffman Code   | Code Length |")
    print("------------------------------------------------------------------------")
    # Sort characters alphabetically.
    for char in sorted(frequencies.keys()):  
        freq = frequencies[char]
        prob = probabilities[char]
        code = huffman_codes[char]
        print(f"| {repr(char):^9} | {freq:^9}  | {prob:^11.5f} | {code:^15} | {len(code):^11} |")

    print("------------------------------------------------------------------------")

# Subset analysis for Selected Characters.
def print_subset_analysis(frequencies, probabilities, huffman_codes, subset):
    """Print analysis for selected characters in alphabetical order."""
    print("\nSubset Analysis (Selected Characters):")
    print("--------------------------------------------------------")
    print("|   Symbol  | Probability |   Codeword   | Code length |")
    print("--------------------------------------------------------")
    for char in (subset): 
        if char in frequencies:
            prob = probabilities[char]
            code = huffman_codes[char]
        print(f"| {repr(char):^9} | {prob:^11.5f} | {code:^12} | {len(code):^11} |")

    print("--------------------------------------------------------")

# Display menu for the user.
def display_menu():
    """Display the menu options for the program."""
    print("\nChoose a step to calculate.")
    print("a. Display number of characters, their frequencies and probabilities, and codewords using Huffman in the story.")
    print("b. Calculate and display Entropy.")
    print("1. Calculate number of Bits using ASCII (NASCII).")
    print("2. Calculate average number of Bits/Character using Huffman.")
    print("3. Calculate total bits using Huffman (Nhuffman).")
    print("4. Display compression percentage.")
    print("5. Show subset analysis.")
    print("6. Exit.")

# Main execution.
def main():
    # File path to the text file.
    file_path = "To_Build_A_Fire_by_Jack_London.docx"

    # Load and preprocess the text.
    text = preprocess_text(load_docx(file_path))
    frequencies = calculate_frequencies(text)
    probabilities = calculate_probabilities(frequencies)
    entropy = calculate_entropy(probabilities)
    
    # Build the Huffman tree and generate codes.
    huffman_tree = build_huffman_tree(frequencies)
    huffman_codes = generate_huffman_codes(huffman_tree)

    total_characters = sum(frequencies.values())
    nascii = calculate_nascii(total_characters)
    average_bits = calculate_average_bits(probabilities, huffman_codes)
    nhuffman = calculate_nhuffman(frequencies, huffman_codes)
    compression_percentage = calculate_compression_percentage(nascii, nhuffman)

    # Menu loop.
    while True:
        display_menu()
        choice = input("\nEnter your choice: ").strip().lower()

        if choice == "a":
            print('-------------------------------------------------------')
            print("Total number of characters in the story is:", total_characters)
            print('-------------------------------------------------------')
            print('\n')
            print_results(frequencies, probabilities, huffman_codes)

        elif choice == "b":
            print('-------------------------------------------------------')
            print("Entropy of the alphabet:", round(entropy, 6), "bits/character")
            print('-------------------------------------------------------')

        elif choice == "1":
            print('-------------------------------------------------------')
            print("Number of bits needed using ASCII (NASCII):", nascii, "bits")
            print('-------------------------------------------------------')

        elif choice == "2": 
            print('--------------------------------------------------------------------------------')
            print("Entropy of the alphabet:", round(entropy, 6), "bits/character")
            print("Average number of bits/character using Huffman code:", round(average_bits, 6), "bits/character")
            print("Comparison: Huffman Avg Bits vs Entropy ->", round(average_bits, 6), "vs", round(entropy, 6))
            print('--------------------------------------------------------------------------------')

        elif choice == "3":
            print('----------------------------------------------------------------')
            print("Total number of bits using Huffman code (Nhuffman):", nhuffman , "bits")
            print('----------------------------------------------------------------')

        elif choice == "4":
            print('------------------------------------')
            print(f"Compression Percentage: {compression_percentage:.4f}%")
            print('------------------------------------')

        elif choice == "5":
            subset = ['a', 'b', 'c', 'd', 'e', 'f', 'm', 'z', ' ', '.']
            print_subset_analysis(frequencies, probabilities, huffman_codes, subset)

        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
