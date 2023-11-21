import cv2
from zadanie2 import draw_contours, draw_centers, get_mask


def scene_3():
    """Сценарий 3"""
    scene_mode = input('Выберете режим. 1 - вебкамера, 2 - видео файл: ')
    if scene_mode == '1':
        capture = cv2.VideoCapture(0)
    else:
        capture = cv2.VideoCapture("IMG_0298.MP4")
    # Бесконечный цикл
    while True:
        # Преобразование изображения в палитру HSV
        ret, img = capture.read()
        hsv_frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        # Получение маски
        red_mask = get_mask(hsv_frame, 'red')
        blue_mask = get_mask(hsv_frame, 'blue')
        # Работа с контурами меток
        contours_red, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours_blue, _ = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        draw_contours(img, contours_red)
        draw_contours(img, contours_blue, (255, 0, 0), 'Blue color')
        # Работа с центрами меток
        draw_centers(img, contours_red)
        draw_centers(img, contours_blue)
        # Отображение изображения
        cv2.imshow('From', img)
        k = cv2.waitKey(41)
        # При нажатии клавиши ESC завершать цикл
        if k == 27:
            break

    # Завершение работы
    capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    scene_3()
