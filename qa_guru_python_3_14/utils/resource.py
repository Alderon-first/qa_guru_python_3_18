import os


# узнать относительный путь к файлу
def path_file(name_file):
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__),  # узнать абсолютный путь к файлу
                     os.path.pardir, os.path.pardir, name_file))  # обрезать его до относительного,
    # где os.path.pardir шаг вверх
