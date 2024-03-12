from datetime import datetime

class Student:
    def __init__(self,
        name: str,
        birthday: 'Birthday'
    ):
        self.name     = name
        self.birthday = birthday

    def getName(self) -> str:
        return self.name
    
    def getBirthday(self) -> 'Birthday':
        return self.birthday
    
    def getAge(self) -> int:
        # Get the current date
        today = datetime.now()

        # Calculate the age by subtracting the birth year from the current year
        age = today.year - self.birthday.getYear()

        # Subtract one from the age if the birthday has not occurred this year
        if (today.month, today.day) < (self.birthday.getMonth(), self.birthday.getDay()):
            age -= 1

        return age
        
class Birthday:
    def __init__(self,
        month: int,
        day: int,
        year: int
    ):
        self.month = month
        self.day   = day
        self.year  = year

    def getMonth(self) -> int:
        return self.month
    
    def getDay(self) -> int:
        return self.day
    
    def getYear(self) -> int:
        return self.year

# List of students
students = [
    Student("John", Birthday(1, 20, 2003)),
    Student("Paul", Birthday(3, 12, 2003)),
    Student("Jake", Birthday(2, 4, 2002)),
    Student("Nate", Birthday(3, 12, 2001))
]

# Current date
currentDate = {"month": 3, "day": 12}

# Notify happy birthday
for student in students:
    birthday = student.getBirthday()
    if currentDate["month"] != birthday.getMonth():
        continue
    if currentDate["day"] != birthday.getDay():
        continue
    print("Happy Birthday, " + student.getName() + "! Your age is now " + str(student.getAge()))