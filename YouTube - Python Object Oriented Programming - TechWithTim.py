'''
Link: https://www.youtube.com/watch?v=JeznW_7DlB0&t=1s

NOTES
- an OBJECT is an INSTANCE of a CLASS
    - objects are useful if you want to re-use something
- INSTANTIATING means to create a new instance
- a METHOD is a function inside of a class that acts on a specific object (eg: .upper())

- ATTRIBUTES are variables for a given class
    - Can reference attributes like a METHOD (eg. object.name)

'''

# Example 1
class Dog:
    def __init__(self, name, age):
        self.name = name # created an attribute of the class "Dog"
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


d = Dog("Tim", 34)
d.set_age(23)
print(d.get_age())

# Example 2
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 - 100

    def get_grade(self):
        return self.grade
    

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        
        return value / len(self.students)

s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

# print(course.students[0].name)
# print(course.get_average_grade())

# Example 3: Inheritance
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

class Cat(Pet):
    def __init__(self, name, age, color): # if we want to add a new attribute
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")
        
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old, and I am {self.color}")

class Dog(Pet):
    def speak(self):
        print("Bark")

p = Pet("Tim", 19)
p.show()

c = Cat("Bill", 34, "red")
c.show()

# Example 4
class Person:
    number_of_people = 0 # not specific to any instance

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod # acts on the class itself instead of a particular method
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

# p1 = Person("Tim")
# p2 = Person("jill")
# print(Person.number_of_people_())

# Example 5: Static Methods
class Math:

    @staticmethod # they do something but do not change anything
    def add5(x):
        return x + 5

print(Math.add5(5))