contacts_employee_data={}

class Contact:
    def __init__(self,name,adress):
        self.name=name
        self.adress=adress
        

class Person:
    def __init__(self,name:str,dob:str,contacts:list):
        self.name=name
        self.dob=dob
        self.contacts=contacts

def create_contact(contact):
    return contact in contacts_employee_data
        
class Employee(Person):
    def __init__(self,name:str,dob:str,contacts:list,email:str,salary:str):
        super().__init__(self,name,dob,contacts)
        self.email=email
        self.salary=salary
    



