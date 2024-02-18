from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name, value):
            super().__init__(self, value)
            self.name = name


class Phone(Field):
    def __init__(self, phone, value):
        super().__init__(self, value)
        if len(value) == 10:
            self.phone = phone

    def setValue(self, value: str):
        if len(value) == 10:
            self.value = value
        

class Record:
    def __init__(self, name, value):
        self.name = Name(name)
        self.value = Field(value)
        self.phones = []


    def __str__(self):
        return f"Contact name: {self.name.value}, \
            phones: {'; '.join(p.value for p in self.phones)}"
    

    def add_phone(self, phone: Phone):
        """
        Метод додає новий номер телефону
        """
        if phone.value and not self.find_phone(phone)[0]:
             self.phones.append(phone)
    

    def edit_phone(self, value1: str, value2: str):
        """
        Метод редагує номер телефону
        """
        phone1 = Phone(value1)
        phone2 = Phone(value2)
        phone1, i = self.find_phone(phone1)
        phone2 = self.find_phone(phone2)[0]
        if not phone1:
            self.phones[i] = phone2 

    def find_phone(self, phone: Phone):
        """
        Метод шукає номер телефону
        """
        i = -1
        for p in self.phones:
            i += 1
            if phone.value == p.value:
                return (True, i)


    def remove_phone(self, phone: Phone):
        """
        Метод видаляє номер телефону
        """
        if phone is self.phones:
            self.phones.remove(phone)
        return self.phones
  

class AddressBook(UserDict):

    def add_record(self, record: Record):
        """
        Метод додає запис в телефону книгу 
        """
        key = record.name
        self.data[key] = record


    def find_record(self, name: str):
        """
        Метод шукає запис в телефоній книзі 
        за іменем
        """
        for i in self.data.items():
             if i[0].value == name:
                  return f"tel.: {'; '.join(p.value for p in i[1].phones)}"
    
    
    def delete_record(self, name: str):
        """
        Метод видаляє запис в телефоній книзі
        """
        for i in self.data.items():
            del self.data
        return f"Запис видалено"
    


    