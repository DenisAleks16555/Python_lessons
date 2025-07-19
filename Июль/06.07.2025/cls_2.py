# Class Person 
# name, surname, fullname(name, surname) - должны задать
# Реализовать методы доступа к name, surname, fullname(get)
# Реализовать методы изменения к name surname

class Person:
     def __init__(self, name, surname):
          self.__name = name
          self.__surname = surname
          self.__fullname = name + " " + surname

     def get_name(self):
      return  self.__name
     
     def get_surname(self):
         return self.__surname
     
     def get_fullname(self):
         return self.__fullname
     
     def set__name(self, new_name):
        self.__name = new_name
       
        self.__fullname = self.__name  + " " +  self.__surname

men = Person("Aleks", "Smith")
print(men.get_fullname())

men.set__name("Den")
print(men.get_fullname())
