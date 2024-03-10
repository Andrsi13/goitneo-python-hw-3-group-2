from collections import UserDict
from datetime import datetime
from get_birthdays import get_birthdays_per_week
import re

class WrongPhoneFormat(Exception):
    pass

class WrongDateFormat(Exception):
    pass

class NotValidDate(Exception):
    pass

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Birthday(Field):
    def __init__(self, date):
        if not re.match(r"^\d{2}\.\d{2}\.\d{4}$", date):
            raise WrongDateFormat
        try:
            datetime.strptime(date, "%d.%m.%Y")
        except ValueError:
            # Якщо виникає помилка, це означає, що рядок не відповідає формату дати
            raise NotValidDate(
                "Please provide valid date"
            )

        super().__init__(date)


class Phone(Field):
    # реалізація класу
    # перевірка довжини номера
    def __init__(self, value):
        if not re.match("^[0-9]{10}$", str(value)):
            raise WrongPhoneFormat("Please provide a 10-digit number.")

        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    # реалізація класу
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def add_birthday(self, date: str):
        self.birthday = Birthday(date)

    def remove_phone(self, phone):
        for to_remove in self.phones:
            if str(to_remove) == phone:
                self.phones.remove(to_remove)
                break

    def edit_phone(self, old_phone, new_phone):
        count = 0
        for p in self.phones:

            if old_phone == str(p):
                self.remove_phone(old_phone)
                self.add_phone(new_phone)
                count += 1
            elif count == 0:
                print("Phone number not found.")

    def find_phone(self, phone):
        for phone_to_find in self.phones:
            if phone == str(phone_to_find):
                return phone

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday}"


class AddressBook(UserDict):
    # реалізація класу
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        name = record.name.value
        if name not in self.data:
            self.data[name] = record
        else:
            print("Record with this name already exist")

    def remove_record(self, name):
        if name in self.data:
            del self.data[name]
        else:
            print("Record not found.")

    def find_record(self, name):
        return self.data.get(name)

    def add_phone_to_record(self, name, phone):
        if name in self.data:
            self.data[name].add_phone(phone)
        else:
            print("Record not found.")

    def delete(self, name):
        count = 0
        if name in self.data:
            self.data.pop(name)
            count += 1
        elif count == 0:
            print("Record not found.")

    def edit_phone_in_record(self, name, old_phone, new_phone):
        if name in self.data:
            self.data[name].edit_phone(old_phone, new_phone)
        else:
            print("Record not found.")

    def find(self, name):
        if name in self.data.keys():
            return self.data.get(name)
        else:
            print("Record not found.")

    def birthdays(self):
        birthday_dicts = []
        for record in self.data.values():
            if record.birthday is not None:
                birthday_dicts.append(
                    {
                        "name": record.name.value,
                        "birthday": datetime.strptime(
                            record.birthday.value, "%d.%m.%Y"
                        ),
                    }
                )
        return get_birthdays_per_week(birthday_dicts)


# Створення нової адресної книги
# book = AddressBook()

# Створення запису для John
# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")
# john_record.add_birthday("13.03.1994")
# john_record.edit_phone('1234567890', '4444444444')
# print(john_record)
# # Додавання запису John до адресної книги
# book.add_record(john_record)
# for name, record in book.data.items():
#     print(record)

# # Створення та додавання нового запису для Jane
# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# jane_record.add_birthday("10.02.2001")
# book.add_record(jane_record)
# print(book.birthdays())
# jane_record.add_birthday("10.03.2010")
# print(book.birthdays())

# # Виведення всіх записів у книзі
# for name, record in book.data.items():
#     print(record)

#     # Знаходження та редагування телефону для John
# john = book.find("John")
# john.edit_phone("1234567890", "1112223333")


# print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# # Пошук конкретного телефону у записі John
# found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# # Видалення запису Jane
# book.delete("Jane")
# book.find("Jane")
