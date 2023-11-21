import cv2
import numpy as np
import pathlib
from zadanie1 import get_image


def draw_contours(img, contours, contours_color=(0, 0, 255), text="Red Color"):
    """Отрисовка контуров на изображении"""
    for contour in contours:
        # Расчёт площади контура
        area = cv2.contourArea(contour)
        # Не рисуем контуры с площадью < 300
        if area > 300:
            # Получаем параметры контура
            x, y, w, h = cv2.boundingRect(contour)
            # Добавляем контур к картинке
            img = cv2.rectangle(img, (x, y),
                                (x + w, y + h),
                                contours_color, 2)
            # Создание текста, в котором будет написан цвет контура
            cv2.putText(img, text, (x, y - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.4,
                        contours_color, 2)
    return img


def draw_centers(img, contours):
    """Добавляем центр метки"""
    # Поиск центров и координат
    h, w = img.shape[0:2]
    frame_center_x, frame_center_y = int(w/2), int(h/2)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 300:
            x, y, w, h = cv2.boundingRect(contour)
            center_x = int(x + w / 2)
            center_y = int(y + h / 2)
            relative_x = center_x - frame_center_x
            relative_y = center_y - frame_center_y
            text = str(relative_x) + ' ' + str(relative_y)
            # Печать центров и написание координат
            img = cv2.circle(img, (center_x, center_y), 5, (0, 0, 0), 3)
            cv2.putText(img, text, (center_x - 85, center_y - 25),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2,
                        (0, 0, 0), 2)


def read_image(name_img):
    """Считавание картинки с диска"""
    img = cv2.imread(name_img)
    # Преобразование изображения в палитру HSV
    hsv_frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    return hsv_frame, img


def get_mask(img, color):
    """Создаёт маску для синего и красного"""
    # Проверка цвета
    # Если цвет красный создаём маску для него
    if color == 'red':
        lower = np.array([0, 50, 50])
        upper = np.array([10, 255, 255])
        mask0 = cv2.inRange(img, lower, upper)

        lower = np.array([170, 50, 50])
        upper = np.array([180, 255, 255])
        mask1 = cv2.inRange(img, lower, upper)

        return mask0 + mask1

    # Если цвет синий создаём маску для него
    if color == 'blue':
        lower = np.array([94, 80, 2])
        upper = np.array([126, 255, 255])

        return cv2.inRange(img, lower, upper)


def scene_2():
    """Сценарий 2"""
    # Путь к файлам
    path = input('Введите путь к файлам: ')
    p = pathlib.Path(path)
    i = 0
    # Если путь существует и это папка выполнять следующие действия
    if p.exists() and p.is_dir():
        # Сортировка изображений
        for image_path in sorted(list(p.iterdir())):
            i += 1
            # Если это файл и его расширение '.png' или '.jpg' выполнять следующие действия
            if image_path.is_file() and (image_path.suffix.lower() == '.png' or image_path.suffix.lower() == '.jpg'):
                # Получение маски
                img = get_image(image_path.resolve())
                hsv_frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                red_mask = get_mask(hsv_frame, 'red')
                blue_mask = get_mask(hsv_frame, 'blue')

                # Находим контуры красного цвета
                contours_red, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                contours_blue, _ = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

                # Рисуем контуры и пишем текст на исходной картинке
                draw_contours(img, contours_red)
                draw_contours(img, contours_blue, (255, 0, 0), 'Blue color')
                draw_centers(img, contours_red)
                draw_centers(img, contours_blue)

                # Печать результата
                cv2.imwrite(f'res_{i}.png', img)
                print(f'Результат сохранён в res_{i}.png')
    else:
        # Вызов ошибки если путь не существует или это не папка
        raise Exception('Путь не существует или это не папка')


if __name__ == '__main__':
    scene_2()

