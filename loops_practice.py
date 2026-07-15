"""Практика по циклам: решения оформлены методами одного класса."""
import random
import time
NUMBERS_START = 1
NUMBERS_END = 8
BREAK_AT = 5

WORDS_COUNT = 10
WORD_PREFIX = "str"

ITERATIONS_COUNT = 10
LOAD_MIN = 0
LOAD_MAX = 100
LOAD_WARNING_THRESHOLD = 85
PAUSE_SECONDS = 0.2

class LoopsPractice:
    """Решения задач по циклам."""

    def print_numbers_until_break(self):
        """Печатает числа и останавливается на BREAK_AT."""
        numbers = list(range(NUMBERS_START, NUMBERS_END))
        for n in numbers:
            print(n)
            if n == BREAK_AT:
                break

    def print_words(self):
        """Печатает сгенерированный список строк."""
        words = [f"{WORD_PREFIX}{i}" for i in range(WORDS_COUNT)]
        for word in words:
            print(word)

    
    def monitor_rostics_load(self):
        """Имитирует мониторинг нагрузки Rostics: 10 итераций со случайной нагрузкой."""
        iteration = 0
        while iteration < ITERATIONS_COUNT:
            load = random.randint(LOAD_MIN, LOAD_MAX)
            print(f"Итерация {iteration}: нагрузка {load}%")
            if load > LOAD_WARNING_THRESHOLD:
                print("ПРЕДУПРЕЖДЕНИЕ: нагрузка превышает порог!")
            time.sleep(PAUSE_SECONDS)
            iteration += 1
if __name__ == "__main__":
    practice = LoopsPractice()
    practice.print_numbers_until_break()
    practice.print_words()
    practice.monitor_rostics_load()