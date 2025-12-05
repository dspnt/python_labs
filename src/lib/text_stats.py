import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    text = text.casefold() if casefold else text
    text = text.replace("ё", "е").replace("Ё", "е") if yo2e else text
    return re.sub(r"\s+", " ", text).strip()


def tokenize(text: str) -> list[str]:
    text = normalize(re.sub(r"[^\w-]", " ", text).strip())
    return text.split()


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
