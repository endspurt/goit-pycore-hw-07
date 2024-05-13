import datetime

class Birthday:
    def __init__(self, value):
        # Initialize Birthday with a date string in the format DD.MM.YYYY
        try:
            self.date = datetime.datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            # If the date format is incorrect, raise an error
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record:
    def __init__(self, name):
        # Initialize a Record with a name, an empty list for phones, and None for birthday
        self.name = name
        self.phones = []
        self.birthday = None

    def add_birthday(self, birthday):
        # Add a Birthday object to the record
        if isinstance(birthday, Birthday):
            self.birthday = birthday
        else:
            # Raise an error if the birthday is not a Birthday instance
            raise TypeError("birthday must be a Birthday instance")

class AddressBook:
    def __init__(self):
        # Initialize AddressBook with an empty list of records
        self.records = []

    def add_record(self, record):
        # Add a Record object to the address book
        if isinstance(record, Record):
            self.records.append(record)
        else:
            # Raise an error if the record is not a Record instance
            raise TypeError("record must be a Record instance")

    def get_upcoming_birthdays(self):
        # Return a list of names of contacts with birthdays in the next week
        today = datetime.datetime.today()
        upcoming = []
        for record in self.records:
            # Check if the record has a birthday and if it is within the next 7 days
            if record.birthday and today <= record.birthday.date < today + datetime.timedelta(days=7):
                upcoming.append(record.name)
        return upcoming

# Create an instance of AddressBook
book = AddressBook()
# Example test data
birthday = Birthday("18.05.2024")  # Use a near-future date for the test
record = Record("Alex Schmidt")
record.add_birthday(birthday)
book.add_record(record)

# Print upcoming birthdays to verify functionality
upcoming_birthdays = book.get_upcoming_birthdays()
print("Upcoming birthdays:", upcoming_birthdays)  # Should return 'John Doe' if the date is correct
print("Birthday is set to:", record.birthday.date)  # Verify the birthday date


