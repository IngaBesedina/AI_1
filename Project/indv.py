#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from itertools import permutations


graph = {
    "Тамбов": {"Мичуринск": 67.8, "Моршанск": 83.8},
    "Мичуринск": {"Тамбов": 67.8, "Сараи": 99.2, "Лебедянь": 92.9},
    "Лебедянь": {"Мичуринск": 92.9, "Скопин": 94.3},
    "Скопин": {"Лебедянь": 94.3, "Шилово": 104},
    "Шилово": {"Сараи": 65.9, "Скопин": 104, "Рязань": 82.5},
    "Сараи": {"Моршанск": 61.3, "Мичуринск": 99.2, "Шилово": 65.9},
    "Моршанск": {"Тамбов": 83.8, "Сараи": 61.3, "Сасово": 73.8},
    "Сасово": {"Моршанск": 73.8, "Касимов": 73.8},
    "Касимов": {"Сасово": 73.8, "Спас-Клепеки": 80.6},
    "Спас-Клепеки": {"Касимов": 80.6, "Рязань": 62.2},
    "Рязань": {"Спас-Клепеки": 62.2, "Шилово": 82.5}
}


def calc_distance(route):
    """Функция для вычисления расстояния маршрута."""
    distance = 0
    for i in range(len(route) - 1):
        distance += graph[route[i]].get(route[i + 1], float("inf"))
    return distance


def find_min_route(start, end):
    """Функция для нахождения минимального маршрута
    с использованием полного перебора."""
    nodes = list(graph.keys())
    nodes.remove(start)
    nodes.remove(end)

    min_distance = float("inf")
    best_route = None

    # Перебор всех возможных маршрутов
    for r in range(len(nodes) + 1):
        for perm in permutations(nodes, r):
            route = [start] + list(perm) + [end]
            distance = calc_distance(route)

            if distance < min_distance:
                min_distance = distance
                best_route = route

    return best_route, min_distance


def main():
    start_point = "Тамбов"
    end_point = "Рязань"

    best_route, min_distance = find_min_route(start_point, end_point)

    print(
        f"Лучший маршрут от {start_point} до {end_point}:"
        f" {' -> '.join(best_route)}"
    )
    print(f"Минимальное расстояние: {min_distance}")


if __name__ == "__main__":
    main()
