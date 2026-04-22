"""
Модуль очереди с приоритетами на основе узлов.
"""


class Node:
    """Узел очереди с приоритетом."""

    def __init__(self, data, priority):
        self.data = data
        self.priority = priority  # 1 - высший, 10 - низший
        self.next = None


class PriorityQueue:
    """Очередь с приоритетами."""

    def __init__(self, max_size=10):
        self.head = None
        self.max_size = max_size
        self.current_size = 0

    def is_empty(self):
        return self.head is None

    def is_full(self):
        return self.current_size >= self.max_size

    def insert_with_priority(self, data, priority):
        """Добавление элемента с приоритетом."""
        if self.is_full():
            print("❌ Очередь переполнена!")
            return False

        new_node = Node(data, priority)

        # Вставка в начало (высший приоритет)
        if self.is_empty() or priority < self.head.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.priority <= priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

        self.current_size += 1
        print(f"✅ Добавлен: '{data}' (приоритет: {priority})")
        return True

    def pull_highest_priority_element(self):
        """Удаление элемента с высшим приоритетом."""
        if self.is_empty():
            print("❌ Очередь пуста!")
            return None

        removed = self.head
        self.head = self.head.next
        self.current_size -= 1
        print(f"🗑️ Удален: '{removed.data}' (приоритет: {removed.priority})")
        return removed.data

    def peek(self):
        """Просмотр элемента с высшим приоритетом."""
        if self.is_empty():
            print("📭 Очередь пуста!")
            return None
        return self.head.data, self.head.priority

    def show(self):
        """Отображение всех элементов."""
        if self.is_empty():
            print("📭 Очередь пуста.")
            return

        print("\n" + "=" * 50)
        print("ОЧЕРЕДЬ С ПРИОРИТЕТАМИ")
        print("=" * 50)
        current = self.head
        i = 1
        while current:
            print(f"  {i}. '{current.data}' | приоритет: {current.priority}")
            current = current.next
            i += 1
        print("=" * 50 + f"\nРазмер: {self.current_size}/{self.max_size}\n")

    def size(self):
        return self.current_size

    def clear(self):
        self.head = None
        self.current_size = 0
        print("🧹 Очередь очищена.")