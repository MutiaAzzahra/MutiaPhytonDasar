class Person:
   def _init_(self, name, age):
    self.name = name
    self.age = age

   def myFunc(self):
     print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myFunc()