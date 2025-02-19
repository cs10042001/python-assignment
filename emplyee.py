contacts_employee_data={}

class Contact:
    def __init__(self,name,adress):
        self.name=name
        self.adress=adress

c1=Contact("6204403423","ranchi")
c2=Contact("8789105594","mysore")   
c3=Contact("7992338839","mysore") 
c4=Contact("7004646497","mysore") 

def create_contact(contact):
    return contact in contacts_employee_data



class Person:
    def __init__(self,name:str,dob:str,contacts:list):
        no_error=True
        for contact in contacts:
            if create_contact(contact):
                print("cant be added the contact the contact occupied")
                no_error=False
                break
        if no_error:
            self.name=name
            self.dob=dob
            self.contacts=contacts
            for contact in self.contacts:
                contacts_employee_data[contact.name]=name

    def __str__(self):
        return f"{self.name}  -----"

# p1=Person("mandal","10-04-2001",[c1,c2])
# print(p1)
# print("hello")
# p2=Person("nandu","2-12-2001",[c3])
# print(contacts_employee_data)


        
class Employee(Person):
    def __init__(self, name :str, dob :str, contacts :list, email :str, salary :int):
        super().__init__(name,dob,contacts)
        self.email=email
        self.salary=salary

def get_emplyee(name):
    return contacts_employee_data[name]
    
def get_number(names):
    numbers=[]
    for number,name in contacts_employee_data.items():
        if name==names:
            numbers.append(number)
    return numbers



e1=Employee("mandal","10-04-2001",[c1,c2],"csramdev@gmail.com",34000)
e2=Employee("Nandu","10-04-2001",[c3],"csramdev@gmail.com",43000)
print(get_emplyee("6204403423"))
print(get_number('mandal'))


