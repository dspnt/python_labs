# Лабораторная работа №7

## A
```python
import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../src")
from lib.io_helpers import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
        ("   ", ""),
    ],
)
def test_normalize(source, expected):
    assert normalize(source) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("машина скорость", ["машина", "скорость"]),
        ("авто дорога город", ["авто", "дорога", "город"]),
        ("", []),
        ("       ", []),
        ("быстрая, машина! скорость.", ["быстрая", "машина", "скорость"]),
    ],
)
def test_tokenize(text, expected):
    assert tokenize(text) == expected


def test_count_freq_basic():
    tokens = ["авто", "мото", "авто", "вело", "мото", "авто"]
    result = count_freq(tokens)
    expected = {"авто": 3, "мото": 2, "вело": 1}
    assert result == expected


def test_count_freq_empty():
    assert count_freq([]) == {}


def test_top_n_basic():
    freq = {"авто": 8, "мото": 5, "велосипед": 12, "самокат": 2}
    result = top_n(freq, 2)
    expected = [("велосипед", 12), ("авто", 8)]
    assert result == expected


def test_top_n_tie_breaker():
    freq = {"ролики": 4, "скейт": 4, "сноуборд": 4}
    result = top_n(freq, 3)
    expected = [("ролики", 4), ("скейт", 4), ("сноуборд", 4)]
    assert result == expected


def test_top_n_empty():
    assert top_n({}, 3) == []


def test_full_pipeline():
    text = "Спорт интересный! Спорт важен. Бег полезен."
    normalized = normalize(text)
    tokens = tokenize(normalized)
    freq = count_freq(tokens)
    top_words = top_n(freq, 5)

    assert normalized == "спорт интересный! спорт важен. бег полезен."
    assert tokens == [
        "спорт",
        "интересный",
        "спорт",
        "важен",
        "бег",
        "полезен",
    ]
    assert freq == {"спорт": 2, "интересный": 1, "важен": 1, "бег": 1, "полезен": 1}

    assert set(top_words) == {
        ("спорт", 2),
        ("интересный", 1),
        ("важен", 1),
        ("бег", 1),
        ("полезен", 1),
    }
    assert len(top_words) == 5
```

## B

```python
mport pytest
import json
import csv
from lab05.json_csv import json_to_csv, csv_to_json


class TestJsonToCsv:
    def test_json_to_csv_basic(self, tmp_path):
        json_data = [
            {"name": "Alice", "age": 25, "city": "Moscow"},
            {"name": "Bob", "age": 30, "city": "SPb"},
        ]

        json_file = tmp_path / "test.json"
        csv_file = tmp_path / "output.csv"

        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(json_data, f)

        json_to_csv(str(json_file), str(csv_file))

        assert csv_file.exists()

        with open(csv_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        assert len(rows) == 2
        assert set(rows[0].keys()) == {"age", "city", "name"}
        assert rows[0]["name"] == "Alice"
        assert rows[0]["age"] == "25"
        assert rows[0]["city"] == "Moscow"

    def test_json_to_csv_different_keys(self, tmp_path):
        json_data = [
            {"name": "Alice", "city": "Moscow"},
            {"name": "Bob", "country": "Russia", "age": 30},
        ]

        json_file = tmp_path / "test.json"
        csv_file = tmp_path / "output.csv"

        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(json_data, f)

        json_to_csv(str(json_file), str(csv_file))

        with open(csv_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        expected_keys = {"name", "city", "country", "age"}
        assert set(rows[0].keys()) | set(rows[1].keys()) == expected_keys

    def test_json_to_csv_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            json_to_csv("nonexistent.json", "output.csv")

    def test_json_to_csv_invalid_json(self, tmp_path):
        invalid_json_file = tmp_path / "invalid.json"
        output_file = tmp_path / "output.csv"

        with open(invalid_json_file, "w", encoding="utf-8") as f:
            f.write("{invalid json content")

        with pytest.raises(ValueError):
            json_to_csv(str(invalid_json_file), str(output_file))

    def test_json_to_csv_empty_json(self, tmp_path):
        empty_file = tmp_path / "empty.json"
        output_file = tmp_path / "output.csv"

        empty_file.write_text("")

        with pytest.raises(ValueError):
            json_to_csv(str(empty_file), str(output_file))


class TestCsvToJson:
    def test_csv_to_json_basic(self, tmp_path):
        csv_data = """name,age,city
Alice,25,Moscow
Bob,30,SPb"""

        csv_file = tmp_path / "test.csv"
        json_file = tmp_path / "output.json"

        with open(csv_file, "w", encoding="utf-8") as f:
            f.write(csv_data)

        csv_to_json(str(csv_file), str(json_file))

        assert json_file.exists()

        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        assert len(data) == 2
        assert set(data[0].keys()) == {"name", "age", "city"}
        assert data[0] == {"name": "Alice", "age": "25", "city": "Moscow"}
        assert data[1] == {"name": "Bob", "age": "30", "city": "SPb"}

    def test_csv_to_json_empty_cells(self, tmp_path):
        csv_data = """name,age,city
Alice,25,
Bob,,SPb"""

        csv_file = tmp_path / "test.csv"
        json_file = tmp_path / "output.json"

        with open(csv_file, "w", encoding="utf-8") as f:
            f.write(csv_data)

        csv_to_json(str(csv_file), str(json_file))

        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        assert data[0]["city"] in [None, ""]
        assert data[1]["age"] in [None, ""]

    def test_csv_to_json_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            csv_to_json("nonexistent.csv", "output.json")

    def test_csv_to_json_empty_file(self, tmp_path):
        empty_file = tmp_path / "empty.csv"
        output_file = tmp_path / "output.json"

        empty_file.write_text("")

        with pytest.raises(ValueError):
            csv_to_json(str(empty_file), str(output_file))


class TestIntegration:
    def test_json_csv_json_roundtrip(self, tmp_path):
        original_data = [
            {"name": "Alice", "age": 25, "city": "Moscow"},
            {"name": "Bob", "age": 30, "city": "SPb"},
        ]

        json_file1 = tmp_path / "test1.json"
        csv_file = tmp_path / "test.csv"
        json_file2 = tmp_path / "test2.json"

        with open(json_file1, "w", encoding="utf-8") as f:
            json.dump(original_data, f)

        json_to_csv(str(json_file1), str(csv_file))
        csv_to_json(str(csv_file), str(json_file2))

        with open(json_file2, "r", encoding="utf-8") as f:
            final_data = json.load(f)

        assert len(final_data) == len(original_data)
```
## Result

![47](/images/lab7/img01.png)
![47](/images/lab7/img02.png)
![47](/images/lab7/img03.png)