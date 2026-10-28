"""
ДЗ презентации 2, повышенный уровень, задача 1.
Время: 20–30 минут.

Тема: арифметические операторы, // и %.

Условие:
    Дано целое число секунд. Переведите его в формат ЧЧ:ММ:СС.
    Используйте только // и %.

Пример:
    In: 3661
    Out: 01:01:01
"""

def seconds_to_hms(seconds: int) -> str:
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    res = []
    for i in [hours, minutes, secs]:
        if i < 10:
            i = f'0{i}'
            res.append(i)
        else:
            res.append(i)
    return f'{res[0]}:{res[1]}:{res[2]}'


if __name__ == "__main__":
    assert seconds_to_hms(3661) == "01:01:01"
    assert seconds_to_hms(0) == "00:00:00"
    assert seconds_to_hms(59) == "00:00:59"
    assert seconds_to_hms(3600) == "01:00:00"
    print("task_01 (p2 advanced): тесты пройдены")
