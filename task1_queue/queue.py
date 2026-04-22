"""
Модуль реализации очереди на основе списка (стандартные типы).
"""


class Queue:
    """
    Класс очереди на основе списка.

    Поддерживает операции:
    - IsEmpty - проверка на пустоту
    - IsFull - проверка на заполнение
    - Enqueue - добавление элемента
    - Dequeue - удаление элемента
    - Show - отображение всех элементов
    """

    def __init__(self, max_size=10):
        """
        Инициализация очереди.

        Args:
            max_size: Максимальный размер очереди (по умолчанию 10)
        """
        self.max_size = max_size
        self.queue = []  # Используем список как хранилище

    def is_empty(self):
        """
        Проверка очереди на пустоту.

        Returns:
            bool: True если очередь пуста, False в противном случае
        """
        return len(self.queue) == 0

    def is_full(self):
        """
        Проверка очереди на заполнение.

        Returns:
            bool: True если очередь заполнена, False в противном случае
        """
        return len(self.queue) >= self.max_size

    def enqueue(self, item):
        """
        Добавление элемента в очередь.

        Args:
            item: Элемент для добавления (символ или строка)

        Returns:
            bool: True если добавление успешно, False если очередь заполнена
        """
        if self.is_full():
            print("❌ Ошибка: Очередь переполнена!")
            return False

        self.queue.append(item)
        print(f"✅ Добавлен элемент: '{item}'")
        return True

    def dequeue(self):
        """
        Удаление элемента из очереди.

        Returns:
            Any: Удаленный элемент или None если очередь пуста
        """
        if self.is_empty():
            print("❌ Ошибка: Очередь пуста!")
            return None

        removed_item = self.queue.pop(0)
        print(f"🗑️ Удален элемент: '{removed_item}'")
        return removed_item

    def show(self):
        """
        Отображение всех элементов очереди.
        """
        if self.is_empty():
            print("📭 Очередь пуста.")
            return

        print("\n" + "=" * 50)
        print("📋 ТЕКУЩАЯ ОЧЕРЕДЬ")
        print("=" * 50)
        print(f"Размер: {self.size()}/{self.max_size}")
        print("Элементы (слева направо):")

        for i, item in enumerate(self.queue, 1):
            print(f"  [{i}] → '{item}'")

        print("=" * 50 + "\n")

    def size(self):
        """
        Возвращает текущий размер очереди.

        Returns:
            int: Количество элементов в очереди
        """
        return len(self.queue)

    def peek(self):
        """
        Просмотр первого элемента без удаления.

        Returns:
            Any: Первый элемент очереди или None
        """
        if self.is_empty():
            print("📭 Очередь пуста.")
            return None
        return self.queue[0]

    def clear(self):
        """
        Очистка очереди.
        """
        self.queue.clear()
        print("🧹 Очередь очищена.")


# Демонстрация работы
if __name__ == "__main__":
    q = Queue(max_size=5)

    print("=== ДЕМОНСТРАЦИЯ РАБОТЫ ОЧЕРЕДИ ===\n")

    # Добавляем элементы
    q.enqueue('A')
    q.enqueue('B')
    q.enqueue('C')
    q.enqueue('D')

    # Показываем очередь
    q.show()

    # Удаляем элемент
    q.dequeue()
    q.show()

    # Добавляем еще
    q.enqueue('E')
    q.enqueue('F')

    # Пробуем добавить в переполненную
    q.enqueue('G')

    q.show()

    # Проверяем на пустоту
    print(f"Очередь пуста? {q.is_empty()}")
    print(f"Очередь заполнена? {q.is_full()}")
    print(f"Размер очереди: {q.size()}")
    print(f"Первый элемент: {q.peek()}")

    # Очищаем очередь
    q.clear()
    q.show()