import datetime

class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(phone)

    def add_birthday(self, birthday):
        if isinstance(birthday, datetime.datetime):
            self.birthday = birthday
        else:
            raise ValueError("Invalid type for birthday")

class AddressBook:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def find(self, name):
        for record in self.records:
            if record.name == name:
                return record
        return None

    def get_upcoming_birthdays(self):
        today = datetime.datetime.now()
        next_week = today + datetime.timedelta(days=7)
        upcoming = []
        for record in self.records:
            if record.birthday and today <= record.birthday < next_week:
                upcoming.append(record.name)
        return upcoming

def parse_input(user_input):
    parts = user_input.split()
    command = parts[0]
    args = parts[1:]
    return command, args

def add_contact(args, book):
    name, phone = args[0], args[1]
    record = book.find(name)
    if not record:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    else:
        message = "Contact updated."
    record.add_phone(phone)
    return message

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "add":
            print(add_contact(args, book))
        elif command == "all":
            for record in book.records:
                print(f"Name: {record.name}, Phones: {', '.join(record.phones)}")
        # Weitere Befehle hier implementieren nach Bedarf

# Kommentare in Englisch für den gesamten Code
