import sys
sys.path.append('./src/lib')
from text_stats import * 
string = sys.stdin.readline()
tokenize = tokenize(string)
unique_words = count_freq(tokenize)
print(f"Всего слов: {len(tokenize)}")
print(f"Уникальных слов: {len(unique_words)}")
n = 5
print(f"Топ-{n}:")
k = top_n(unique_words)
for token in k:
    print(token[0] + ":" + str(token[1]))
