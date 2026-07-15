MIN_LENGTH = 5

WORDS = ["кот", "автоматизация", "тест", "программирование", "код", "Python"]


def filter_long_strings(strings):
    result = []
    for s in strings:
        if len(s) > MIN_LENGTH:
            result.append(s)
    return result


if __name__ == "__main__":
    print("Исходный список:", WORDS)
    print("Длинные строки:", filter_long_strings(WORDS))
