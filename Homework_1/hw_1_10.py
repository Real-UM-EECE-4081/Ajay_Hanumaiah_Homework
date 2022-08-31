from collections import Counter
def word_freq (file):
    with open(file) as f:
        return Counter (f.read().split())

print('Number of words in file: ',word_freq('sample3.txt'))
