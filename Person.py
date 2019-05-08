# 2. Define a class Person and its two child classes: Male and Female. All classes have a
# method "getGender" which can print "Male" for Male class and "Female" for Female
# class.

class Person:
  def __init__(self):
    print("Parent class is called and I am a human ")

class Male(Person):
    def getGender(self):
      print("I am Male")

class Female(Person):
    def getGender(self):
      print("I am Female")

x = Male()
x.getGender()