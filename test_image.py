# Импорт функции check_color
from zadanie1 import check_color


def test_check_color():
    """Тест для check_color"""
    # Проверка ответов
    assert check_color([255, 0, 0]) == 'B'
    assert check_color([0, 255, 0]) == 'G'
    assert check_color([0, 0, 255]) == 'R'
    # Пример неправильного ввода
    try:
        check_color([255, 255, 0])
    # Вызов ошибки если ввод неправильный
    except Exception as e:
        assert str(e) == 'Не допустимый цвет'