import cv2
import pathlib
import numpy


def check_color(pixel) -> str:
    """Распознаём цвет по первому пикселю"""
    # Если 1 пиксель голубой писать 'B'
    if pixel[0] == 255 and pixel[1] == 0 and pixel[2] == 0:
        return 'B'
    # Если 1 пиксель зелёный писать 'G'
    if pixel[0] == 0 and pixel[1] == 255 and pixel[2] == 0:
        return 'G'
    # Если 1 пиксель красный писать 'R'
    if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 255:
        return 'R'
    # Вызов ошибки если цвет не из списка ['Красный', 'Синий', 'Зелёный']
    raise Exception('Не допустимый цвет')


def get_image(image_path: pathlib.Path):
    """Cчитывает изображения с диска"""
    stream = open(image_path, "rb")
    # Преобразование изображения в массив байт
    bytes = bytearray(stream.read())
    numpyarray = numpy.asarray(bytes, dtype=numpy.uint8)
    # Возврат картинки без изменений
    return cv2.imdecode(numpyarray, cv2.IMREAD_UNCHANGED)


def scene_1():
    """Сценарий 1"""
    # Ввод пути к папке с картинками
    path = input('Введите путь к файлам: ')
    p = pathlib.Path(path)
    # Если путь существует и это папка выполнять следующие действия
    if p.exists() and p.is_dir():
        res = ''
        # Считывание всех файлов из папки, стандартная сортировка
        for image_path in sorted(list(p.iterdir())):
            # Если это файл и его расширение '.png' выполнять следующие действия
            if image_path.is_file() and image_path.suffix == '.png':
                image = get_image(image_path.resolve())
                res += check_color(image[0][0])
        # Вывод результата
        print(res)
    else:
        # Вызов ошибки если путь не существует или это не папка
        raise Exception('Путь не существует или это не папка')


if __name__ == '__main__':
    scene_1()
