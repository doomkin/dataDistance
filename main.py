"""Поиск подходящих фрагментов паззла"""
from scipy.spatial import distance
from scipy.stats import spearmanr, kendalltau, pearsonr

"""Список задач, состоящих из пазла и набора фрагментов для поиска подходящего"""
tasks = [
    # 1.1
    [[[0, 0, 1,  0, 1, 0,  0, 1, 0,  1], [0, 0, 1,  0, 0, 0,  0, 0, 0,  2], [0, 0, 0,  0, 1, 0,  0, 1, 0,  3],
      [0, 2, 0,  2, 0, 0,  0, 2, 0,  2], [0, 0, 2,  0, 2, 0,  0, 2, 0,  1], [0, 2, 2,  2, 2, 0,  0, 0, 0,  1],
      [0, 0, 0,  0, 0, 1,  1, 0, 1,  3], [0, 0, 1,  0, 0, 1,  0, 0, 0,  3]],

     [[0, 0, 2,  0, 0, 0,  2, 0, 2,  2], [0, 0, 2,  0, 0, 0,  2, 0, 2,  3], [0, 0, 1,  0, 0, 0,  1, 0, 1,  1],
      [0, 2, 0,  0, 2, 2,  0, 0, 0,  1],
      [0, 0, 2,  0, 0, 0,  0, 2, 0,  2], [2, 0, 0,  0, 0, 2,  0, 0, 0,  2], [0, 0, 0,  2, 0, 0,  0, 0, 0,  1],
      [0, 0, 2,  0, 0, 0,  2, 0, 2,  2]]],

    # 1.2
    [[[1, 0, 0,  0, 0, 0,  0, 0, 0,  1], [0, 0, 0,  0, 0, 0,  3, 0, 0,  1], [0, 0, 0,  0, 0, 3,  0, 3, 0,  1],
      [0, 0, 0,  0, 0, 0,  2, 0, 0,  1], [4, 0, 0,  0, 0, 0,  0, 4, 0,  1], [0, 0, 0,  0, 4, 0,  0, 0, 0,  1],
      [0, 0, 0,  0, 0, 0,  0, 3, 0,  1], [5, 0, 0,  5, 0, 0,  0, 0, 0,  1]],

     [[0, 0, 0,  0, 0, 3,  0, 0, 0,  1], [0, 0, 5,  0, 0, 0,  0, 0, 5,  1], [0, 5, 0,  0, 0, 0,  0, 0, 0,  1],
      [0, 5, 0,  0, 0, 0,  0, 0, 0,  1],
      [0, 0, 0,  0, 0, 5,  0, 0, 0,  1], [0, 0, 0,  0, 0, 0,  0, 4, 0,  1], [3, 0, 0,  3, 0, 0,  0, 0, 0,  1],
      [0, 0, 5,  0, 0, 0,  0, 0, 0,  1]]],
]


def correlation(function, fragment, puzzle):
    """Корреляция фрагмента с паззлом"""
    summa = 0
    for puzzle_fragment in puzzle:
        result = function(fragment, puzzle_fragment)
        if isinstance(result, (list, tuple)):
            summa += result[0]
        else:
            summa += result
    return summa


def optimum(min_max, function, puzzle, fragments):
    """Номер оптимального фрагмента паззла"""
    correlations = [correlation(function, fragment, puzzle) for fragment in fragments]
    print([round(corr, 2) for corr in correlations])
    return correlations.index(min_max(correlations)) + 1


def solve(task):
    """Решение паззла"""
    page_num, task_num = task_number(tasks.index(task))
    puzzle, fragments = task
    print(page_num, task_num, sep=".")
    print()
    print_task(puzzle, 3, 3, False)
    print_task(fragments, 2, 4, True)
    print(optimum(max, spearmanr, puzzle, fragments), 'по сумме ранговых корреляций Спирмена\n')
    print(optimum(max, kendalltau, puzzle, fragments), 'по сумме ранговых корреляций Кендалла\n')
    print(optimum(max, pearsonr, puzzle, fragments), 'по сумме корреляций Пирсона\n')
    print(optimum(min, distance.euclidean, puzzle, fragments), 'по сумме евклидовых расстояний\n')


def print_task(task, rows, cols, show_number):
    for row in range(rows):
        for col in range(cols):
            index = cols * row + col
            if index < len(task):
                if show_number:
                    print(index + 1, "=", end=' ')
                print(task[index], end='  ')
        print()
    print()


def task_number(index):
    number = index + 1
    page_num, task_num = number // 10 + 1, number % 10
    if task_num == 0:
        task_num = 10
    return page_num, task_num


if __name__ == '__main__':
    for t in tasks:
        solve(t)
