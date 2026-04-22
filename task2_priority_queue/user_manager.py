"""
Модуль управления пользователями на основе связного списка.
"""


class UserNode:
    """Узел с данными пользователя."""

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.next = None


class UserManager:
    """Управление пользователями (связный список)."""

    def __init__(self):
        self.head = None

    def add_user(self, login, password):
        """Добавление нового пользователя."""
        if self.find_user(login):
            print(f"❌ Пользователь '{login}' уже существует!")
            return False

        new_user = UserNode(login, password)
        new_user.next = self.head
        self.head = new_user
        print(f"✅ Пользователь '{login}' добавлен!")
        return True

    def remove_user(self, login):
        """Удаление пользователя."""
        if self.head is None:
            print("❌ Список пользователей пуст!")
            return False

        if self.head.login == login:
            self.head = self.head.next
            print(f"✅ Пользователь '{login}' удален!")
            return True

        current = self.head
        while current.next:
            if current.next.login == login:
                current.next = current.next.next
                print(f"✅ Пользователь '{login}' удален!")
                return True
            current = current.next

        print(f"❌ Пользователь '{login}' не найден!")
        return False

    def find_user(self, login):
        """Проверка существования пользователя."""
        current = self.head
        while current:
            if current.login == login:
                return True
            current = current.next
        return False

    def edit_login(self, old_login, new_login):
        """Изменение логина пользователя."""
        if not self.find_user(old_login):
            print(f"❌ Пользователь '{old_login}' не найден!")
            return False

        if self.find_user(new_login):
            print(f"❌ Логин '{new_login}' уже занят!")
            return False

        current = self.head
        while current:
            if current.login == old_login:
                current.login = new_login
                print(f"✅ Логин изменен: '{old_login}' → '{new_login}'")
                return True
            current = current.next
        return False

    def edit_password(self, login, new_password):
        """Изменение пароля пользователя."""
        current = self.head
        while current:
            if current.login == login:
                current.password = new_password
                print(f"✅ Пароль для '{login}' изменен!")
                return True
            current = current.next

        print(f"❌ Пользователь '{login}' не найден!")
        return False

    def show_all(self):
        """Отображение всех пользователей."""
        if self.head is None:
            print("📭 Список пользователей пуст!")
            return

        print("\n" + "=" * 50)
        print("СПИСОК ПОЛЬЗОВАТЕЛЕЙ")
        print("=" * 50)
        current = self.head
        i = 1
        while current:
            print(f"  {i}. Логин: {current.login}, Пароль: {current.password}")
            current = current.next
            i += 1
        print("=" * 50 + f"\nВсего: {i - 1} пользователей\n")

    def get_count(self):
        """Количество пользователей."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count