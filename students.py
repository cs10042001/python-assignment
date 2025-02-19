class Subject:
    def __init__(self,sub_id :str, name:str):
        self.sub_id=sub_id
        self.name=name
    
sub1=Subject("CS501","Maths")
sub2=Subject("CS502","English")
sub3=Subject("CS601","python")
sub4=Subject("CS602","c++")
sub5=Subject("CS603","AI")
sub6=Subject("CS701","Cloud")
sub7=Subject("CS702","java")


class Semster:
    def __init__(self,semster_no :int,subjects:list):
        self.semster_no=semster_no
        self.subjects=subjects

sem5=Semster(5,[sub1,sub2])
sem6=Semster(6,[sub3,sub4,sub5])
sem7=Semster(7,[sub6,sub7])

class Marks:
    def __init__(self,sub :Subject,semster:int,marks:int):
        self.sub=sub
        self.semster=semster
        self.marks=marks

mark1=Marks(sub1, 5,67)
mark2=Marks(sub2,  5,47)
mark3=Marks(sub3,  6,67)
mark4=Marks(sub4,  6,97)
mark5=Marks(sub5,  6,87)
mark6=Marks(sub6,  7,77)
mark7=Marks(sub7,  7,90)
mark8=Marks(sub1,  5,88)
mark9=Marks(sub2,  5,67)
mark10=Marks(sub3, 6,57)
mark11=Marks(sub4, 6,37)
mark12=Marks(sub5, 6,79)

class Student:
    def __init__(self,student_id,name,contact,marks):
        self.student_id=student_id
        self.name=name
        self.contact=contact 
        self.marks=marks 


def get_marks(student,semster=None):

    student_marks_list=student.marks
    marks={}
    if semster==None:
        get_latest_sem=0
        for sem in student_marks_list:
            if sem.semster>get_latest_sem:
                get_latest_sem=sem.semster
        for sem in student_marks_list:
            if sem.semster==get_latest_sem:
                marks[sem.sub.name]=sem.marks
    else:
        for sem in student_marks_list:
            if sem.semster==semster:
                marks[sem.sub.name]=sem.marks
    return marks
    

stud1=Student("21CS001","mandal","6204403423",[mark1,mark2,mark3,mark4,mark5,mark6,mark7])
stud2=Student("21CS002","nandu","8789105594",[mark8,mark9,mark10,mark11,mark12])

print(get_marks(stud1,6))
print(get_marks(stud1))
print(get_marks(stud2))



        


