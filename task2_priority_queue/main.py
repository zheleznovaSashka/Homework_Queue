"""
Главное меню для очереди с приоритетами.
"""

import os
import sys
from priority_queue import PriorityQueue


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_menu():
    print("\n" + "=" * 50)
    print("   ОЧЕРЕДЬ С ПРИОРИТЕТАМИ")
    print("=" * 50)
    print(" 1. InsertWithPriority - Добавить элемент")
    print(" 2. PullHighestPriority - Удалить элемент")
    print(" 3. IsEmpty - Проверить на пустоту")
    print(" 4. IsFull - Проверить на заполнение")
    print(" 5. Peek - Показать высший приоритет")
    print(" 6. Show - Показать все элементы")
    print(" 7. Size - Размер очереди")
    print(" 8. Clear - Очистить очередь")
    print(" 0. Выход")
    print("=" * 50)


def main():
    clear_screen()
    print("=" * 50)
    print("    СОЗДАНИЕ ОЧЕРЕДИ С ПРИОРИТЕТАМИ")
    print("=" * 50)

    max_size = int(input("Введите размер очереди: "))
    pq = PriorityQueue(max_size)
    print(f"\n✅ Очередь создана! (размер: {max_size})")
    input("\nНажмите Enter...")

    while True:
        clear_screen()
        print_menu()
        choice = input("Выберите операцию (0-8): ")

        if choice == '0':
            print("\n👋 До свидания!")
            sys.exit(0)

        elif choice == '1':
            data = input("Введите элемент: ")
            priority = int(input("Приоритет (1-10, 1=высший): "))
            pq.insert_with_priority(data, priority)

        elif choice == '2':
            pq.pull_highest_priority_element()

        elif choice == '3':
            print("Очередь пуста" if pq.is_empty() else "Очередь не пуста")

        elif choice == '4':
            print("Очередь полна" if pq.is_full() else "Очередь не полна")

        elif choice == '5':
            result = pq.peek()
            if result:
                print(f"Высший приоритет: '{result[0]}' (приоритет: {result[1]})")

        elif choice == '6':
            pq.show()

        elif choice == '7':
            print(f"Размер очереди: {pq.size()}/{pq.max_size}")

        elif choice == '8':
            pq.clear()

        input("\nНажмите Enter...")


if __name__ == "__main__":
    main()
