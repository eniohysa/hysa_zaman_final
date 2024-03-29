class Student:
    def __init__(self, name, student_id, mailing_address, birth_date,
                 acceptance, start_semester, major, email_addresses=[], phone_numbers=[]):
        self.__name = name
        self.__student_id = student_id
        self.__mailing_address = mailing_address
        self.__birth_date = birth_date
        self.__acceptance = acceptance
        self.__start_semester = start_semester
        self.__major = major
        self.__email_addresses = email_addresses
        self.__phone_numbers = phone_numbers

    def set_name(self, name):
        self.__name = name

    def set_student_id(self, student_id):
        self.__student_id = int(student_id)

    def set_mailing_address(self, mailing_address):
        self.__mailing_address = mailing_address

    def set_birth_date(self, birth_date):
        self.__birth_date = birth_date

    def set_acceptance(self, acceptance):
        self.__acceptance = acceptance

    def set_start_semester(self, start_semester):
        self.__start_semester = start_semester

    def set_major(self, major):
        self.__major = major

    def add_email_address(self, email_address):
        self.__email_addresses.append(email_address)

    def add_phone_number(self, phone_number):
        self.__phone_numbers.append(phone_number)

    def remove_email_address(self, email_address):
        self.__email_addresses.remove(email_address)

    def remove_phone_number(self, phone_number):
        self.__phone_numbers.remove(phone_number)

    def get_name(self):
        return self.__name

    def get_student_id(self):
        return self.__student_id

    def get_mailing_address(self):
        return self.__mailing_address

    def get_birth_date(self):
        return self.__birth_date

    def get_acceptance(self):
        return self.__acceptance

    def get_start_semester(self):
        return self.__start_semester

    def get_major(self):
        return self.__major

    def display(self):
        print(f"Student ID: {self.__student_id}")
        print(f"Student name: {self.__name}")
        for email in self.__email_addresses:
            print(f'Email: {email}')
        for phone in self.__phone_numbers:
            print(f'Phone: {phone}')
        print(f"Birthday: {self.__birth_date}")
        print(f"Acceptance: {self.__acceptance}")
        print(f"Major: {self.__major}")
        print(f"Start {self.__start_semester}")
