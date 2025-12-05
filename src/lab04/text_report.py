import csv
import sys
from pathlib import Path
import re
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "lib"))
sys.path.append(os.path.dirname(__file__))
from text_stats import *
from io_txt_csv import *


def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    input_file = os.path.join(base_dir, "data", "lab04", "input.txt")
    output_file = os.path.join(base_dir, "data", "lab04", "report.csv")
    try:
        text = read_text(input_file)
        tokens = tokenize(normalize(text))
        freq = count_freq(tokens)
        sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
        write_csv(sorted_freq, output_file, header=("word", "count"))
        print(f"Всего слов: {sum(freq.values())}")
        print(f"Уникальных слов: {len(freq)}")
        print("Топ-5:", *[f"{w}:{c}" for w, c in top_n(freq, 5)])
    except FileNotFoundError:
        print(f"Файл не найден: {input_file}")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
