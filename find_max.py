NUMBERS = [4, 17, 2, 9, 25, 6, 11, 30, 8]


def find_max(numbers):
    biggest = numbers[0]
    for n in numbers:
        if n > biggest:
            biggest = n
    return biggest


if __name__ == "__main__":
    print("Список:", NUMBERS)
    print("Максимум:", find_max(NUMBERS))
