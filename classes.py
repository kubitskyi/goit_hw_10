from collections import UserDict


class Field:
    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        self.value = value
    
    def __str__(self) -> str:
        return str(self.value)
    
    def __repr__(self) -> str:
        return f'{self.value}'

class UserName(Field):
    pass

class PhoneNumber(Field):
    pass

class Record:
    def __init__(self,
                name: UserName,
                number: PhoneNumber):
        self.name = name
        self.numbers = []
        if number:
            self.numbers.append(number)
        
    def __repr__(self) -> str:
        p = self.numbers if self.numbers[0] else 'number is missing'
        return f'{self.name.value.capitalize()} - {p}'

    def add_number(self, number):
        numbers = self.numbers
        number = number
        if number in numbers:
            return "This phone number is in your contacts"
        numbers.append(number)
        return f"{number} phone number is added to {self.name}'s contacts"
    
    def get_number(self):
        return self.numbers

    def change_number(self, old_number, new_number):
        for num in self.numbers:
            if num.value == old_number.value:
                self.numbers.remove(num)
                self.numbers.append(new_number)
                return f"Changet {old_number} to {new_number}"
        return "Number no found"

class ContactsBook(UserDict):

    def add_contact(self, contact: Record):
        self.data[contact.name.value] = contact

if __name__=="__main__":
    pass