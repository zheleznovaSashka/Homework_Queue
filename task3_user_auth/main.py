"""
Главное меню для управления пользователями.
"""

import os
import sys
from user_manager import UserManager


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_menu():
    print("\n" + "=" * 50)
    print("      УПРАВЛЕНИЕ ПОЛЬЗОВАТЕЛЯМИ")
    print("=" * 50)
    print(" 1. Добавить нового пользователя")
    print(" 2. Удалить существующего пользователя")
    print(" 3. Проверить существование пользователя")
    print(" 4. Изменить логин пользователя")
    print(" 5. Изменить пароль пользователя")
    print(" 6. Показать всех пользователей")
    print(" 0. Выход")
    print("=" * 50)


def main():
    clear_screen()
    print("=" * 50)
    print("    СИСТЕМА УПРАВЛЕНИЯ ПОЛЬЗОВАТЕЛЯМИ")
    print("=" * 50)

    um = UserManager()
    print("\n✅ Система готова к работе!")
    input("\nНажмите Enter...")

    while True:
        clear_screen()
        print_menu()
        choice = input("Выберите операцию (0-6): ")

        if choice == '0':
            print("\n👋 До свидания!")
            sys.exit(0)

        elif choice == '1':
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            um.add_user(login, password)

        elif choice == '2':
            login = input("Введите логин для удаления: ")
            um.remove_user(login)

        elif choice == '3':
            login = input("Введите логин для проверки: ")
            if um.find_user(login):
                print(f"✅ Пользователь '{login}' существует!")
            else:
                print(f"❌ Пользователь '{login}' не найден!")

        elif choice == '4':
            old_login = input("Введите текущий логин: ")
            new_login = input("Введите новый логин: ")
            um.edit_login(old_login, new_login)

        elif choice == '5':
            login = input("Введите логин: ")
            new_password = input("Введите новый пароль: ")
            um.edit_password(login, new_password)

        elif choice == '6':
            um.show_all()

        input("\nНажмите Enter...")


if __name__ == "__main__":
    main()