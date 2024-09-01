# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

import random
from typing import List, Tuple

def make_desk(size: int) -> List[List[int]]:
    EMPTY = 0
    return [[EMPTY for _ in range(size)] for _ in range(size)]

def show_desk(desk: List[List[int]]) -> None:
    print()
    print(*desk, sep='\n')

def feel_desk(desk: List[List[int]], queens: List[Tuple[int, int]]) -> List[List[int]]:
    '''
    Функция заполняет доску ферзями.
    1 - ферзь на поле, 0 - поле пустое
    Возвращает доску в виде списка с расставленными фигурами
    '''
    BUSY = 1
    for q in queens:
        desk[q[0]][q[1]] = BUSY
    return desk

def _check_turns(desk: List[List[int]]) -> bool:
    for row in desk:
        if row.count(1) > 1:
            return False
    return True

def _transparent(desk: List[List[int]]) -> List[List[int]]:
    return [list(row) for row in zip(*desk)]

def _make_all_diagonal(desk: List[List[int]]) -> List[List[int]]:
    n = len(desk)
    all_diags = []

    main, second = _check_main_diagonal(desk)
    all_diags.append(main)
    all_diags.append(second)

    for distance in range(1, n):
        sum_tl = n - 1 - distance
        sum_br = n - 1 + distance

        all_diags.append([desk[i][sum_tl - i] for i in range(n - distance)])
        all_diags.append([desk[i][sum_br - i] for i in range(distance, n)])

    return all_diags

def _check_main_diagonal(desk: List[List[int]]) -> Tuple[List[int], List[int]]:
    main_diag = [desk[i][i] for i in range(len(desk))]
    secondary_diagonal = [desk[i][len(desk) - i - 1] for i in range(len(desk))]
    return main_diag, secondary_diagonal

def _check_diagonals(desk: List[List[int]]) -> bool:
    all_diags = _make_all_diagonal(desk)
    for diag in all_diags:
        if diag.count(1) > 1:
            return False
    return True

def is_beat(size: int, queens: List[Tuple[int, int]]) -> bool:
    desk = make_desk(size)
    desk_with_queens = feel_desk(desk, queens)
    if _check_turns(desk_with_queens):
        rotate_desk = _transparent(desk_with_queens)
        if _check_turns(rotate_desk):
            if _check_diagonals(desk_with_queens):
                return True
    return False

def generate_queens_coordinates(size: int) -> List[Tuple[int, int]]:
    coordinates = []
    while len(coordinates) < size:
        x, y = random.randint(0, size - 1), random.randint(0, size - 1)
        if (x, y) not in coordinates:
            coordinates.append((x, y))
    return coordinates

def show_success(size: int, num_successes: int) -> None:
    count = num_successes
    while count > 0:
        coord_queens = generate_queens_coordinates(size)
        result = is_beat(size, coord_queens)
        if result:
            desk_with_queens = feel_desk(make_desk(size), coord_queens)
            show_desk(desk_with_queens)
            print(f"Success: {coord_queens}")
            count -= 1

if __name__ == "__main__":
    SIZE = 8
    show_success(SIZE, 4)
