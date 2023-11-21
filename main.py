from zadanie1 import scene_1
from zadanie2 import scene_2
from zadanie3 import scene_3
from zadanie4 import scene_4


if __name__ == '__main__':
    """Основная функция"""
    # Выбор сценария
    res = int(input('Выберете сценарий 1-4: '))
    # Запуск выбранного сценария
    match res:
        case 1: scene_1()
        case 2: scene_2()
        case 3: scene_3()
        case 4: scene_4()
        # Вызов ошибки если сценарий не в диапазоне 1-4
        case _: raise Exception('Недопустимый сценарий')
