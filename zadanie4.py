import cv2
import pathlib
import joblib
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from zadanie1 import get_image
import warnings
from sklearn.ensemble import ExtraTreesClassifier


def make_model():
    """Обучаем модель на основе деревьев"""
    # Грузим размеченные данные из интернета
    mnist_data = fetch_openml('mnist_784', parser='auto')
    x, y = mnist_data['data'], mnist_data['target']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
    clf = ExtraTreesClassifier(n_estimators=37)
    clf.fit(x_train, y_train)
    # Сохраняем модель в файл
    joblib.dump(clf, "tree_model.joblib")
    score = clf.score(x_test, y_test)
    print(score)


def get_model():
    """Загружаем предобученную модель с файла"""
    clf = joblib.load("tree_model.joblib")
    return clf


def scene_4():
    """Сценарий 4"""
    mode = input("Выберете режим. 1 - обучить модель, 2 - предположение: ")
    if mode == '1':
        make_model()
    else:
        res = ''
        # Получение модели с помощью ввода путя
        tree_model = get_model()
        path = input('Введите путь к папке: ')
        p = pathlib.Path(path)
        # Если путь существует и это папка выполнять следующие действия
        if p.exists() and p.is_dir():
            # Сортировка изображений
            for image_path in sorted(list(p.iterdir())):
                # Если это файл и его расширение '.png' выполнять следующие действия
                if image_path.is_file() and image_path.suffix == '.png':
                    image = get_image(image_path.resolve())
                    # Если количество чисел внутри массива равно 3 преобразовывать изображение в серо-белую палитру
                    if len(image.shape) == 3:
                        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
                    # Меняем чёрный цвет на белый, а белый на чёрный
                    image = 255 - image.reshape(784)
                    # Убираем warnings
                    with warnings.catch_warnings():
                        warnings.simplefilter("ignore")
                        # Предсказываем цифру
                        pred = tree_model.predict([image])
                        res += pred[0]
            # Печать результата
            print(res)
        else:
            # Вызов ошибки если путь не существует или это не папка
            raise Exception('Путь не существует или это не папка')


if __name__ == '__main__':
    scene_4()
