import datetime

class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        if phone not in self.phones:
            self.phones.append(phone)

    def set_birthday(self, birthday):
        self.birthday = birthday

class AddressBook:
    def __init__(self):
        self.records = {}

    def add_record(self, record):
        self.records[record.name] = record

    def find(self, name):
        return self.records.get(name)

    def get_upcoming_birthdays(self):
        today = datetime.date.today()
        upcoming_birthdays = []
        for record in self.records.values():
            if record.birthday and today <= record.birthday <= today + datetime.timedelta(days=7):
                upcoming_birthdays.append(record.name)
        return upcoming_birthdays

def parse_input(input_string):
    parts = input_string.strip().split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args

def add_contact(args, book):
    if len(args) < 2:
        return "Error: Missing arguments for add. Usage: add [name] [phone]"
    name, phone = args[0], args[1]
    record = book.find(name)
    if not record:
        record = Record(name)
        book.add_record(record)
    record.add_phone(phone)
    return f"Contact {name} added or updated with phone {phone}."

def add_birthday(args, book):
    if len(args) < 2:
        return "Error: Missing arguments for add-birthday. Usage: add-birthday [name] [DD.MM.YYYY]"
    name, date_str = args[0], args[1]
    try:
        birthday = datetime.datetime.strptime(date_str, "%d.%m.%Y").date()
    except ValueError:
        return "Invalid date format. Use DD.MM.YYYY"
    record = book.find(name)
    if not record:
        return f"No contact found with name {name}."
    record.set_birthday(birthday)
    return f"Birthday set for {name} on {birthday.strftime('%d.%m.%Y')}."

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("Hello! How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "all":
            for record in book.records.values():
                phones = ', '.join(record.phones)
                print(f"Name: {record.name}, Phones: {phones}")
        elif command == "birthdays":
            upcoming = book.get_upcoming_birthdays()
            if upcoming:
                print("Upcoming birthdays:")
                for name in upcoming:
                    print(name)
            else:
                print("No birthdays in the next week.")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

