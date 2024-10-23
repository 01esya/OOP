class Pair:
    # Список допустимых номиналов
    VALID_DENOMINATIONS = {1, 2, 5, 10, 50, 100, 500, 1000, 5000}

    def __init__(self, first, second):
        """
        Инициализация объекта Pair. Проверка корректности переданных значений.
        :param first: номинал купюры (должен быть допустимым целым положительным числом)
        :param second: количество купюр (должно быть положительным целым числом)
        """
        if first not in self.VALID_DENOMINATIONS:
            raise ValueError("Номинал купюры недопустим.")
        if not isinstance(second, int) or second <= 0:
            raise ValueError("Количество купюр должно быть положительным целым числом.")
        self.first = first
        self.second = second

    def read(self):
        """
        Ввод значений с клавиатуры с проверкой корректности.
        """
        while True:
            try:
                # Ввод номинала купюры
                self.first = int(input("Введите номинал купюры (1, 2, 5, 10, 50, 100, 500, 1000, 5000): "))
                if self.first not in self.VALID_DENOMINATIONS:
                    raise ValueError("Неверный номинал купюры. Попробуйте снова.")

                # Ввод количества купюр
                self.second = int(input("Введите количество купюр (положительное целое число): "))
                if self.second <= 0:
                    raise ValueError("Количество купюр должно быть положительным числом. Попробуйте снова.")

                break  # Прерываем цикл при успешном вводе данных

            except ValueError as e:
                print(f"Ошибка ввода: {e}")

    def display(self):
        """
        Вывод значений полей на экран.
        """
        print(f"Номинал купюры: {self.first}, Количество купюр: {self.second}")

    def summa(self):
        """
        Вычисление общей денежной суммы.
        :return: сумма денег (номинал умноженный на количество купюр)
        """
        return self.first * self.second


def make_pair(first, second):
    """
    Функция для создания объекта Pair с проверкой корректности параметров.
    :param first: номинал купюры
    :param second: количество купюр
    :return: объект класса Pair
    """
    try:
        pair = Pair(first, second)
        return pair
    except ValueError as e:
        print(f"Ошибка создания пары: {e}")
        exit(1)


if __name__ == '__main__':
    # Создаем объект класса Pair
    pair = Pair(0, 0)  # Начальная инициализация с фиктивными значениями
    pair.read()  # Ввод данных пользователем
    pair.display()  # Вывод данных
    print(f"Общая сумма: {pair.summa()}")  # Вычисляем и выводим общую сумму
