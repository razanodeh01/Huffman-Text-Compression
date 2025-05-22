# 📚 Huffman Text Compression

## 📄 About the Project

A Python-based project that applies Huffman coding to compress the short story *"To Build A Fire"* by Jack London. The system calculates character frequencies, builds a Huffman tree, encodes the text, and evaluates the compression rate against standard ASCII encoding. The project demonstrates the efficiency of Huffman coding in reducing data size for storage and transmission.


## 🧠 Key Concepts

- **Huffman Coding**: A variable-length prefix coding technique used for lossless compression.
- **Entropy**: The theoretical lower bound on average bits/character.
- **ASCII vs. Huffman**: Comparison of bit usage and efficiency.
- **Prefix Property**: Ensures no code is the prefix of another.


## ⚙️ Functional Overview

- Loads and cleans a `.docx` text file.
- Calculates:
  - Character frequencies and probabilities.
  - Entropy of the character distribution.
  - Average bits per character with Huffman.
  - Total bits needed for ASCII vs. Huffman.
  - Compression percentage.
- Builds a Huffman tree and generates codes.
- Provides analysis for selected characters.
- Includes a user-friendly CLI menu to display results interactively.

## 🎥 Demo

Here’s a quick preview of how the program runs in the terminal:[Run the script](https://github.com/user-attachments/assets/e34fd1c2-4a38-44ce-8fdc-2c8f8fedfd14)


## 👥 Contributors:
- [**Razan Abdalrahman**](https://github.com/razanodeh01)  
- [**Maisam Alaa**](https://github.com/maisamjuma)

