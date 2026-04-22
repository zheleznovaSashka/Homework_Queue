"""
Модуль с тестами для очереди.
"""

import unittest
import sys
import os

# Добавляем текущую папку в путь для импорта
sys.path.insert(0, os.path.dirname(__file__))

# Выберите один из вариантов:
# Вариант 1: Очередь на списке
from queue import Queue

# Вариант 2: Очередь на узлах (раскомментировать если используете узлы)
# from queue_node import Queue


class TestQueue(unittest.TestCase):
    """Тесты для очереди."""

    def setUp(self):
        """Создание новой очереди перед каждым тестом."""
        self.q = Queue(max_size=5)

    # ============ ТЕСТЫ ISEMPTY ============

    def test_is_empty_new_queue(self):
        """Тест: новая очередь должна быть пустой."""
        self.assertTrue(self.q.is_empty())

    def test_is_empty_after_enqueue(self):
        """Тест: после добавления элемента очередь не пуста."""
        self.q.enqueue('A')
        self.assertFalse(self.q.is_empty())

    def test_is_empty_after_enqueue_and_dequeue(self):
        """Тест: после добавления и удаления очередь пуста."""
        self.q.enqueue('A')
        self.q.dequeue()
        self.assertTrue(self.q.is_empty())

    # ============ ТЕСТЫ ISFULL ============

    def test_is_full_when_queue_is_full(self):
        """Тест: очередь заполнена после добавления max_size элементов."""
        for i in range(5):
            self.q.enqueue(chr(65 + i))
        self.assertTrue(self.q.is_full())

    def test_is_full_when_queue_not_full(self):
        """Тест: очередь не заполнена."""
        self.q.enqueue('A')
        self.q.enqueue('B')
        self.assertFalse(self.q.is_full())

    def test_is_full_after_dequeue_from_full(self):
        """Тест: после удаления из заполненной очереди она перестает быть полной."""
        for i in range(5):
            self.q.enqueue(chr(65 + i))
        self.q.dequeue()
        self.assertFalse(self.q.is_full())

    # ============ ТЕСТЫ ENQUEUE ============

    def test_enqueue_one_element(self):
        """Тест: добавление одного элемента."""
        result = self.q.enqueue('A')
        self.assertTrue(result)
        self.assertEqual(self.q.size(), 1)

    def test_enqueue_multiple_elements(self):
        """Тест: добавление нескольких элементов."""
        self.q.enqueue('A')
        self.q.enqueue('B')
        self.q.enqueue('C')
        self.assertEqual(self.q.size(), 3)

    def test_enqueue_when_full(self):
        """Тест: добавление в заполненную очередь."""
        for i in range(5):
            self.q.enqueue(chr(65 + i))
        result = self.q.enqueue('F')
        self.assertFalse(result)
        self.assertEqual(self.q.size(), 5)

    def test_enqueue_string(self):
        """Тест: добавление строки."""
        result = self.q.enqueue("Hello")
        self.assertTrue(result)
        self.assertEqual(self.q.peek(), "Hello")

    def test_enqueue_empty_string(self):
        """Тест: добавление пустой строки."""
        result = self.q.enqueue("")
        self.assertTrue(result)
        self.assertEqual(self.q.size(), 1)

    # ============ ТЕСТЫ DEQUEUE ============

    def test_dequeue_from_empty(self):
        """Тест: удаление из пустой очереди."""
        result = self.q.dequeue()
        self.assertIsNone(result)

    def test_dequeue_order_fifo(self):
        """Тест: порядок FIFO (первый пришел - первый ушел)."""
        self.q.enqueue('A')
        self.q.enqueue('B')
        self.q.enqueue('C')

        self.assertEqual(self.q.dequeue(), 'A')
        self.assertEqual(self.q.dequeue(), 'B')
        self.assertEqual(self.q.dequeue(), 'C')

    def test_dequeue_until_empty(self):
        """Тест: удаление всех элементов."""
        self.q.enqueue('A')
        self.q.enqueue('B')
        self.q.enqueue('C')

        self.q.dequeue()
        self.q.dequeue()
        self.q.dequeue()

        self.assertTrue(self.q.is_empty())

    def test_dequeue_returns_correct_type(self):
        """Тест: удаление возвращает правильный тип данных."""
        self.q.enqueue(123)
        result = self.q.dequeue()
        self.assertIsInstance(result, int)
        self.assertEqual(result, 123)

    # ============ ТЕСТЫ SIZE ============

    def test_size_empty(self):
        """Тест: размер пустой очереди."""
        self.assertEqual(self.q.size(), 0)

    def test_size_after_enqueue(self):
        """Тест: размер после добавления."""
        self.q.enqueue('A')
        self.assertEqual(self.q.size(), 1)
        self.q.enqueue('B')
        self.assertEqual(self.q.size(), 2)

    def test_size_after_dequeue(self):
        """Тест: размер после удаления."""
        self.q.enqueue('A')
        self.q.enqueue('B')
        self.q.enqueue('C')
        self.q.dequeue()
        self.assertEqual(self.q.size(), 2)

    # ============ ТЕСТЫ PEEK ============

    def test_peek_empty(self):
        """Тест: просмотр первого элемента пустой очереди."""
        result = self.q.peek()
        self.assertIsNone(result)

    def test_peek_does_not_remove(self):
        """Тест: peek не удаляет элемент."""
        self.q.enqueue('A')
        self.q.enqueue('B')

        first = self.q.peek()
        self.assertEqual(first, 'A')
        self.assertEqual(self.q.size(), 2)

    def test_peek_after_dequeue(self):
        """Тест: peek после удаления."""
        self.q.enqueue('A')
        self.q.enqueue('B')
        self.q.dequeue()
        self.assertEqual(self.q.peek(), 'B')

    # ============ ТЕСТЫ CLEAR ============

    def test_clear_empty_queue(self):
        """Тест: очистка пустой очереди."""
        self.q.clear()
        self.assertTrue(self.q.is_empty())
        self.assertEqual(self.q.size(), 0)

    def test_clear_non_empty_queue(self):
        """Тест: очистка непустой очереди."""
        self.q.enqueue('A')
        self.q.enqueue('B')
        self.q.enqueue('C')
        self.q.clear()
        self.assertTrue(self.q.is_empty())
        self.assertEqual(self.q.size(), 0)

    def test_clear_then_enqueue(self):
        """Тест: очистка, затем добавление новых элементов."""
        self.q.enqueue('A')
        self.q.enqueue('B')
        self.q.clear()
        self.q.enqueue('C')
        self.assertEqual(self.q.size(), 1)
        self.assertEqual(self.q.peek(), 'C')

    # ============ ТЕСТЫ SHOW ============

    def test_show_empty_queue(self):
        """Тест: отображение пустой очереди (должно быть без ошибок)."""
        # Просто проверяем, что метод не вызывает ошибку
        try:
            self.q.show()
            result = True
        except:
            result = False
        self.assertTrue(result)

    def test_show_non_empty_queue(self):
        """Тест: отображение непустой очереди."""
        self.q.enqueue('A')
        self.q.enqueue('B')
        self.q.enqueue('C')

        try:
            self.q.show()
            result = True
        except:
            result = False
        self.assertTrue(result)

    # ============ КОМПЛЕКСНЫЕ ТЕСТЫ ============

    def test_complex_scenario(self):
        """Тест: комплексный сценарий использования."""
        # Добавляем элементы
        self.q.enqueue('A')
        self.q.enqueue('B')
        self.q.enqueue('C')
        self.assertEqual(self.q.size(), 3)

        # Удаляем один
        self.assertEqual(self.q.dequeue(), 'A')
        self.assertEqual(self.q.size(), 2)

        # Добавляем еще
        self.q.enqueue('D')
        self.q.enqueue('E')
        self.assertEqual(self.q.size(), 4)

        # Проверяем порядок
        self.assertEqual(self.q.dequeue(), 'B')
        self.assertEqual(self.q.dequeue(), 'C')
        self.assertEqual(self.q.dequeue(), 'D')
        self.assertEqual(self.q.dequeue(), 'E')

        # Очередь должна быть пуста
        self.assertTrue(self.q.is_empty())

    def test_mixed_data_types(self):
        """Тест: разные типы данных."""
        self.q.enqueue('A')
        self.q.enqueue(123)
        self.q.enqueue(3.14)
        self.q.enqueue(True)
        self.q.enqueue("Hello")

        self.assertEqual(self.q.dequeue(), 'A')
        self.assertEqual(self.q.dequeue(), 123)
        self.assertEqual(self.q.dequeue(), 3.14)
        self.assertEqual(self.q.dequeue(), True)
        self.assertEqual(self.q.dequeue(), "Hello")

    def test_boundary_full_then_empty(self):
        """Тест: заполнение до предела, затем полное опустошение."""
        # Заполняем до предела
        for i in range(5):
            self.q.enqueue(str(i))
        self.assertTrue(self.q.is_full())

        # Опустошаем
        for i in range(5):
            self.q.dequeue()
        self.assertTrue(self.q.is_empty())

        # Снова добавляем
        self.q.enqueue('New')
        self.assertEqual(self.q.size(), 1)
        self.assertEqual(self.q.peek(), 'New')


class TestQueueDifferentSizes(unittest.TestCase):
    """Тесты для очередей разного размера."""

    def test_queue_size_1(self):
        """Тест: очередь размером 1."""
        q = Queue(max_size=1)

        q.enqueue('A')
        self.assertTrue(q.is_full())

        result = q.enqueue('B')
        self.assertFalse(result)

        self.assertEqual(q.dequeue(), 'A')
        self.assertTrue(q.is_empty())

    def test_queue_size_10(self):
        """Тест: очередь размером 10."""
        q = Queue(max_size=10)

        for i in range(10):
            q.enqueue(str(i))

        self.assertTrue(q.is_full())
        self.assertEqual(q.size(), 10)

        for i in range(10):
            self.assertEqual(q.dequeue(), str(i))

        self.assertTrue(q.is_empty())

    def test_queue_size_100(self):
        """Тест: очередь размером 100."""
        q = Queue(max_size=100)

        for i in range(100):
            q.enqueue(str(i))

        self.assertEqual(q.size(), 100)
        self.assertTrue(q.is_full())


if __name__ == "__main__":
    # Запуск тестов с подробным выводом
    unittest.main(verbosity=2)