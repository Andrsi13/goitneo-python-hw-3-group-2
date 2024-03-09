from classes import Record, AddressBook, WrongPhoneFormat, WrongDateFormat

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return print("Give me name and phone please.")
        except KeyError:
            return "No such contact found"
        except IndexError:
            return "No such element in list"
        except WrongPhoneFormat:
            return print("Please provide a 10-digit number.")

    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contacts(args, book):
    name, phone = args
    record = Record(name)
    record.add_phone(phone)
    if record == WrongPhoneFormat:
        pass
        # print("Please provide a 10-digit number.")
    else:
        book.add_record(record)
        print('Contact added.')
    


@input_error
def change_contact(args, book):
    name, phone = args
    old_phone = book.find(name).phones[0]
    record = book.edit_phone_in_record(name, str(old_phone),phone)
    print("Contact updated.")


@input_error
def phone_username(args, contacts):
    name = args[0]

    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."


@input_error
def all_contacts(book):
    if book:
        for name, record in book.data.items():
            print(record)
    else:
        return "No contacts found."


def main():
    book = AddressBook()
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            add_contacts(args, book)
        elif command == "change":
            change_contact(args, book)
        elif command == "phone":
            print(phone_username(args, contacts))
        elif command == "all":
            all_contacts(book)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()