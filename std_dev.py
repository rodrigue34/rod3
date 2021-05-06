# Rodrigue Andela
# 05/5/2021
# in this task I created a class that has two private data members and I created a separate function to calculate the std

class Person:
    __name = None
    __age = None
#  Initializes data members
    def __init__ (self, name ,age):
        self.__name = name
        self.__age = age
    def get_age(self,):
        return self.__age

# Function takes Person class array of object and number of persons
def std_dev(person_list):
    n = len(person_list)
    u = sum([x.get_age() for x in person_list]) / len(person_list)
    ty = 0
    # Calculates standard deviation of age and returns it
    for m in person_list:
        ty = ty + (m.get_age()-u)**2
    return (ty/n) ** 0.5






