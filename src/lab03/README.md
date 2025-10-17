# Лабораторная работа №2

## Задание normalize
```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    text = text.casefold() if casefold else text
    text = text.replace('ё', 'е').replace('Ё', 'е') if yo2e else text
    return re.sub(r'\s+', ' ', text).strip()
```
![47](/images/lab3/img01.png)
## Задание tokenize
```python
def tokenize(text: str) -> list[str]:
    text = normalize(re.sub(r'[^\w-]', ' ', text).strip())
    return text.split()
```
![47](/images/lab3/img02.png)
## Задание count_freq+top_n
```python
def count_freq(tokens: list[str]) -> dict[str, int]:
    fr = dict()
    for token in tokens:
        if token in fr:
            fr[token] += 1
        else:
            fr[token] = 1
    return dict(sorted(fr.items(), key=lambda item: (-item[1], item[0])))

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    a = []
    k = 0
    for token in freq.items():
        a.append(token)
        k += 1
        if k == n:  
            break
    return a
```
![47](/images/lab3/img03.png)

## Задание B
```python
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
```
![47](/images/lab3/img04.png)
