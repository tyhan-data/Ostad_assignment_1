# Q1. Create a Python class representing a student with attributes such as name and ID,
and include both a default constructor and a parameterized constructor.Add a method to display the student details, 
and use the pass statement inside an empty placeholder method. Then create multiple objects from this class to test each constructor.


class Student :
    def __init__(self, name = 'Tyhan', ID = 870255):
           self.name = name
           self.ID = ID

    def display(self):
          print(f"Hey everyone, i'm {self.name}. I'm a student and my student ID numbers are {self.ID}")

    def placeholder(self):
          pass
 
student_1 = Student("Joy", 5555)
student_2 = Student()

student_1.display()
student_2.display()



# Q2. Write a Python program demonstrating single, multilevel, and hierarchical inheritance using simple classes such as Person, Student, and Teacher.
Include at least one overridden method in the child classes to show method overriding.


class Person :
    def introduce(self):
        print("Hello everyone...")

# single inheritance
class Student(Person):
    def hobby(self):
        print("My hobby is coding and watching Football matches in my free time.")

# multilevel inheritance
class Teacher(Student):
    def introduce(self):    # method overriding
        print("I am a teacher and i teach students math.")

# Hierarchical inheritance
class Principal(Person):
    def introduce(self):     # method overriding
      print("I'm the principal of the college")      

obj = Teacher()
obj.introduce() 
obj.hobby() 

obj2 = Student()
obj2.hobby()
obj2.introduce()

obj3 = Principal()
obj3.introduce()



# Q3. Define a class that shows encapsulation by using private attributes and public getter/setter methods. 
Add two methods with the same name but different parameter counts to illustrate method overloading (using default arguments). 
Then create another class to demonstrate multiple inheritance.


class Father :
    def __init__(self, money):
        self.__money = money
     
    def get_money(self):
        return self.__money
    
    def set_money(self, value):
         self.__money = value
        
class Mother :
    def display_info(self, arg = None , type = 'work'):
        if type == "work":
            print(f"She is a {arg}")
        else:
            print(f"She love to watch TV {arg} show.")

class Child(Father, Mother):
    pass


child = Child(10000)

print(child.get_money())
child.set_money(20000)
print(child.get_money())

child.display_info(' housewife ', 'work')
child.display_info('Serial', 'like')



