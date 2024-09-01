# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
from sys import argv

def is_leap(year :int) -> bool:
    return not (year % 4 != 0 or year % 100 == 0 and year % 400 != 0)

def valid(full_date: str) -> bool:
    date, month, year = (int(item) for item in full_date.split('.'))
    if year < 1 or year > 9999 or month < 1 or month > 12 or date < 1 or date > 31:
        return False
    if month in (4, 6, 9, 11) and date > 30:
        return False
    if month == 2 and is_leap(year) and date > 29:
        return False
    if month == 2 and not is_leap(year) and date > 28:
        return False
    return True

if __name__ == "__main__":
    if len(argv) != 2:
        print("Использование: python date_validator.py <дата в формате DD.MM.YYYY>")
    else:
        input_date = argv[1]
        if valid(input_date):
            print("Дата существует.")
        else:
            print("Дата невозможна.")