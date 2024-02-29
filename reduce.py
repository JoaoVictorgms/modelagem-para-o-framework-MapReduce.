import random
import string

class FileGenerator:
    def __init__(self, split, n, alphabet, min_size, max_size):
        self.split = split
        self.n = n
        self.alphabet = alphabet
        self.min_size = min_size
        self.max_size = max_size

    def generate_word(self):
        word_size = random.randint(self.min_size, self.max_size)
        return ''.join(random.choices(self.alphabet, k=word_size))

    def generate_file(self):
        words = [self.generate_word() for _ in range(self.n)]
        chunks = [words[i:i + self.n // self.split] for i in range(0, self.n, self.n // self.split)]
        return chunks

split = 3
n = 100
alphabet = string.ascii_lowercase
min_size = 3
max_size = 8


generator = FileGenerator(split, n, alphabet, min_size, max_size)
file_chunks = generator.generate_file()



for i, chunk in enumerate(file_chunks):
    with open(f'chunk_{i+1}.txt', 'w') as f:
        f.write('\n'.join(chunk))
