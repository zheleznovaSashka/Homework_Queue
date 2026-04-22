"""
Главное меню для работы с очередью.
"""

import sys
from task1_queue.queue import Queue


def clear_screen():
    """Очистка экрана."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def print_menu():
    """Печать меню."""
    print("\n" + "="*50)
    print("       ОПЕРАЦИИ С ОЧЕРЕДЬЮ")
    print("="*50)
    print(" 1. Enqueue  - Добавить элемент")
    print(" 2. Dequeue  - Удалить элемент")
    print(" 3. IsEmpty  - Проверить на пустоту")
    print(" 4. IsFull   - Проверить на заполнение")
    print(" 5. Show     - Показать все элементы")
    print(" 6. Size     - Показать размер очереди")
    print(" 7. Peek     - Показать первый элемент")
    print(" 8. Clear    - Очистить очередь")
    print(" 0. Выход")
    print("="*50)


def get_queue_size():
    """Получение размера очереди от пользователя."""
    while True:
        try:
            size = input("Введите максимальный размер очереди: ")
            size = int(size)
            if size > 0:
                return size
            else:
                print("❌ Размер должен быть положительным числом!")
        except ValueError:
            print("❌ Пожалуйста, введите целое число!")


def get_element():
    """Получение элемента от пользователя."""
    element = input("Введите элемент (символ или строку): ").strip()
    if not element:
        print("❌ Элемент не может быть пустым!")
        return None
    return element


def main():
    """Главная функция."""
    clear_screen()

    print("="*50)
    print("    СОЗДАНИЕ НОВОЙ ОЧЕРЕДИ")
    print("="*50)

    max_size = get_queue_size()
    queue = Queue(max_size=max_size)

    print(f"\n✅ Очередь создана! Максимальный размер: {max_size}")
    input("\nНажмите Enter для продолжения...")

    while True:
        clear_screen()
        print_menu()

        try:
            choice = input("Выберите операцию (0-8): ").strip()

            if choice == '0':
                print("\n👋 До свидания!")
                sys.exit(0)

            elif choice == '1':  # Enqueue
                element = get_element()
                if element:
                    queue.enqueue(element)

            elif choice == '2':  # Dequeue
                queue.dequeue()

            elif choice == '3':  # IsEmpty
                if queue.is_empty():
                    print("✅ Очередь ПУСТА")
                else:
                    print("❌ Очередь НЕ ПУСТА")

            elif choice == '4':  # IsFull
                if queue.is_full():
                    print("⚠️ Очередь ЗАПОЛНЕНА")
                else:
                    print("✅ Очередь НЕ ЗАПОЛНЕНА")

            elif choice == '5':  # Show
                queue.show()

            elif choice == '6':  # Size
                print(f"📊 Размер очереди: {queue.size()} элементов")

            elif choice == '7':  # Peek
                front = queue.peek()
                if front is not None:
                    print(f"👁️ Первый элемент очереди: '{front}'")

            elif choice == '8':  # Clear
                confirm = input("Вы уверены? (y/n): ").strip().lower()
                if confirm == 'y':
                    queue.clear()

            else:
                print("❌ Неверный выбор! Попробуйте снова.")

        except KeyboardInterrupt:
            print("\n\n👋 До свидания!")
            sys.exit(0)
        except Exception as e:
            print(f"❌ Ошибка: {e}")

        input("\nНажмите Enter для продолжения...")


if __name__ == "__main__":
    main()