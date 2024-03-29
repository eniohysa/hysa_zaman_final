from Student import Student
from Address import Address
from Date import Date
from Phone import Phone
from Email import Email
from Semester import Semester

if __name__ == '__main__':
    street = input('Enter street: ')
    city = input('Enter city: ')
    state = input('Enter state: ')
    zipcode = input('Enter zipcode: ')
    address_type = input('Enter address_type: ')
    mailing_address = Address(street, city, state, zipcode, address_type)

    birth_day = input("Enter birth day: ")
    birth_month = input("Enter birth month: ")
    birth_year = input("Enter birth year: ")
    birth_date = Date(birth_day, birth_month, birth_year)

    acceptance_day = input("Enter acceptance day: ")
    acceptance_month = input("Enter acceptance month: ")
    acceptance_year = input("Enter acceptance year: ")
    acceptance = Date(acceptance_day, acceptance_month, acceptance_year)

    student_id = input('Enter student ID: ')

    start_semester_season = input('Enter start semester season: ')
    start_semester_year = input('Enter start semester year:')
    start_semester = Semester(start_semester_season, start_semester_year)

    student_name = input("Enter student name: ")

    major = input('Enter major: ')

    student1 = Student(student_name, student_id, mailing_address, birth_date, acceptance, start_semester, major)

    email_address = input('Enter email address: ')
    email_type = input('Enter email_type: ')
    email = Email(email_address, email_type)
    more_emails = input('Would you like to enter more emails? (Y/N): ')
    while more_emails.upper() == "Y":
        email_address = input('Enter email address: ')
        email_type = input('Enter email_type: ')
        email = Email(email_address, email_type)
        more_emails = input('Would you like to enter more emails? (Y/N): ')
        student1.add_email_address(email)

    phone_num = input('Enter phone number: ')
    phone_type = input('Enter phone type: ')
    phone = Phone(phone_num, phone_type)
    more_phone = input('Would you like to enter more phone numbers? (Y/N): ')
    while more_phone.upper() == "Y":
        phone_num = input('Enter phone number: ')
        phone_type = input('Enter phone type: ')
        phone = Phone(phone_num, phone_type)
        more_phone = input('Would you like to enter more phone numbers? (Y/N): ')
        student1.add_phone_number(phone)

    student1.display()
