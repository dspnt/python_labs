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
    top_words = top_n(freq, 5)  # изменили на 5

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

    # Для ТОП-5 проверяем все слова (порядок может быть разный)
    assert set(top_words) == {
        ("спорт", 2),
        ("интересный", 1),
        ("важен", 1),
        ("бег", 1),
        ("полезен", 1),
    }
    assert len(top_words) == 5
