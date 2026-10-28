"""
ДЗ презентации 5, повышенный уровень, задача 1.
Время: 25–35 минут.

Тема: дробный рюкзак.

Условие:
    items — список кортежей (weight, value).
    Верните максимальную суммарную стоимость.

Пример:
    capacity = 50
    items = [(10, 60), (20, 100), (30, 120)]
    Ответ: 240.0
"""

def fractional_knapsack(capacity: float, items: list) -> float:
    items = sorted(items, key=lambda item: item[1] / item[0], reverse=True)

    remaining_capacity = capacity
    total_value = 0

    for item in items:
        weight = item[0]
        value = item[1]
        if weight <= remaining_capacity:
            total_value += value
            remaining_capacity -= weight
        else:
            fraction = remaining_capacity / weight
            total_value += value * fraction
            remaining_capacity = 0
            break
    
    return total_value


if __name__ == "__main__":
    items = [(10, 60), (20, 100), (30, 120)]
    assert abs(fractional_knapsack(50, items) - 240.0) < 1e-9
    assert fractional_knapsack(0, items) == 0.0
    print("task_01 (p5 advanced): тесты пройдены")
