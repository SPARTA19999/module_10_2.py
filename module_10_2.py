# Импорт необходимых модулей и классов
import threading
import time

# Функция для правильного склонения слова "день"
def get_day_word(days):
    if 11 <= days % 100 <= 14:
        return "дней"
    elif days % 10 == 1:
        return "день"
    elif 2 <= days % 10 <= 4:
        return "дня"
    else:
        return "дней"

# Объявление класса Knight, наследованного от threading.Thread
class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name      # Имя рыцаря
        self.power = power    # Сила рыцаря

    def run(self):
        enemies = 100        # Изначальное количество врагов у каждого рыцаря
        days = 0             # Счетчик дней сражения
        print(f"{self.name}, на нас напали!")

        while enemies > 0:
            time.sleep(1)    # Задержка в 1 секунду, имитирующая один день
            days += 1
            enemies -= self.power
            if enemies < 0:
                enemies = 0
            # Получение правильной формы слова "день"
            day_word = get_day_word(days)
            print(f"{self.name} сражается {days} {day_word}..., осталось {enemies} воинов.")

        # Получение правильной формы слова "день" для финального сообщения
        day_word = get_day_word(days)
        print(f"{self.name} одержал победу спустя {days} {day_word}!")

def main():
    # Создание объектов класса Knight с заданными параметрами
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight('Sir Galahad', 20)

    # Запуск потоков
    first_knight.start()
    second_knight.start()

    # Ожидание завершения обоих потоков
    first_knight.join()
    second_knight.join()

    # Вывод сообщения об окончании битв
    print("Все битвы закончились!")

if __name__ == "__main__":
    main()
