# 1.  Make the class with composition.

class Laptop:
    def __init__(self, name, capacity, display):
        self.name = name
        self.display = display
        self.battery = Battery(capacity)

class Battery:
    def __init__(self, capacity):
        self.capacity = capacity

laptop = Laptop("Lenovo", 2000, 2160)
print(laptop.battery.capacity)

# 2. Make the class with aggregation

class Guitar:
    def __init__(self, guitar_str):
        self.guitar_str = guitar_str

class GuitarString:
    def __init__(self, string):
        self.string = string

guitar_string = GuitarString('A')
guitar = Guitar(guitar_string)

# 3. Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
#     Note: this method should be static

class Calc:
    @staticmethod
    def add_numbers(a, b, c):
        return a + b +c

print(Calc.add_numbers(3, 5, 8))

# 4*. Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
#     It should have 2 methods:
#     carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
#     which should create Pasta instances with predefined list of ingredients.

class Pasta:
    def __init__(self, list_of_ingredients):
        self.list_of_ingredients = list_of_ingredients

    @classmethod
    def carbonara(cls):
        list_of_ingredients = ['forcemeat', 'tomatoes']
        return cls(list_of_ingredients)

    @classmethod
    def bolognaise(cls):
        list_of_ingredients = ['bacon', 'parmesan', 'eggs']
        return cls(list_of_ingredients)

pasta_1 = Pasta(["tomato", "cucumber"])
print(pasta_1.list_of_ingredients)

pasta_2 = Pasta.bolognaise()
print(pasta_2.list_of_ingredients)

# 5*. Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
#    In case of setting visitors_count - max_visitors_num should be checked,
#    if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.

class Concert:
    max_visitors_num = 0

    def __init__(self):
        self.__visitors_count = 0

    @property
    def visitors_count(self):
        return self.__visitors_count

    @visitors_count.setter
    def visitors_count(self, value):
        if value > Concert.max_visitors_num:
            self.__visitors_count = Concert.max_visitors_num
        else:
            self.__visitors_count = value

Concert.max_visitors_num = 50
concert = Concert()
concert.visitors_count = 1000
print(concert.visitors_count)

# 6. Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str), birthday (str), age (int)

import dataclasses

@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int

address_book = AddressBookDataClass(0, "Julia", "+380675456348", "Dnipro, UA", "gmail@gmail.com", "12.12.12", 25)
print(address_book.name)

# 7. Create the same class (6) but using NamedTuple
from collections import namedtuple

AddressBookNamedTuple = namedtuple("AddressBookNamedTuple", ["key", "name", "phone_number", "address", "email", "birthday", "age"])

address_book_tuple = AddressBookNamedTuple(0, "Julia", "+380675456348", "Dnipro, UA", "gmail@gmail.com", "12.12.12", 25)
print(address_book_tuple)

# 8.
class AddressBook:
    """
    Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
    Make its str() representation the same as for AddressBookDataClass defined above.
    Expected result by printing instance of AddressBook: AddressBook(key='', name='', phone_number='', address='', email='', birthday= '', age='')
    """

    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f'AddressBook(key=\'{self.key}\', name=\'{self.name}\', phone_number=\'{self.phone_number}\', ' \
               f'address=\'{self.address}\', email=\'{self.email}\', birthday= \'{self.birthday}\', age=\'{self.age}\')'

address_book_3 = AddressBook(0, "Julia", "+380675456348", "Dnipro, UA", "gmail@gmail.com", "12.12.12", 25)
print(address_book_3)

# 9. Change the value of the age property of the person object

class Person:
    name = "John"
    age = 36
    country = "USA"

setattr(Person, 'age', 25)
print(Person.age)

# 10. Add an 'email' attribute of the object student and set its value
#     Assign the new attribute to 'student_email' variable and print it by using getattr

class Student:
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name

setattr(Student, "email", "gmail@gmail.com")
student_email = getattr(Student, "email")
print(student_email)

#11*. By using @property convert the celsius to fahrenheit
#     Hint: (temperature * 1.8) + 32)

class Celsius:

    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temp_fahrenheit(self):
        temp_fahr = (self._temperature * 1.8) + 32
        return temp_fahr

temperature = Celsius(20)
print(temperature.temp_fahrenheit)

