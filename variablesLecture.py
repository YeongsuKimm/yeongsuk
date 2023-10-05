num = 1;
bool = True;
stri = "hello";

print(num)
print(bool)
print(stri)



num1 = 1;
num2 = 2;
num3 = 3;


#num1 ==> num3
#num2 ==> num1
#num3 ==> num2

temp = num1;
num1 = num3;
temp2 = num2;
num2 = temp;
num3 = temp2;
print(num1)
print(num2)
print(num3)

lst = ["one","two","three"]
print(lst[0])


# HOMEWORK:


class Person:
    def __init__(self, name, age):
        self.name = name;
        self.age = age;

person1 = Person("John", 13);
person2 = Person("Doe", 16);
person3 = Person("HON", 12);


lst = [person1, person2, person3];
def print_people(Personlst):
    for i in range(len(Personlst)):
        print(Personlst[i].name, end= ": ");
        print(Personlst[i].age);

print_people(lst);

dict = {
    "one": person1,
    "two": person2,
    "three": person3,
}
def print_oldest(pdict):
    oldest = list(pdict.keys())[0]
    oldest_age = pdict[oldest].age
    for name in pdict.keys():
        if pdict[name].age > oldest_age:
            oldest = name
            oldest_age = pdict[name].age
    print(pdict[oldest].name)

print_oldest(dict)

import json

secretNumber = 15
print(secretNumber) #int
print(type(secretNumber))

food = "Pizza"
print(food) #string
print(type(food))

names = ["Nandan", "Arnav", "Torin", "Remy"]
print(names) # array or list
print(type(names))

IamCool = True

print(IamCool) # boolean
print(type(IamCool))

##Bonus Problem:

names_2 = {
    "Nandan": "TeamMate1",
    "Arnav": "TeamMate2",
    "Torin": "TeamMate3",
    "Remy": "TeamMate4",
}

print(names_2) #dictionary
print(type(names_2))



variables = {
    "numbers": [1,2,3,4,5],
    "names": ["John", "Robert", "Bob", "Doe", "Bill"],
    "isDict": True,
}

def print_largest(dict):
    max = dict["numbers"][0];
    for i in range(1, len(dict["numbers"])):
        if max < dict["numbers"][i]:
            max = dict["numbers"][i];
    print(f"Largest Number is {max}")
    
    longestName = dict["names"][1];
    max = len(dict["names"][0])
    for i in range(1, len(dict["names"])):
        if max < len(dict["names"][i]):
            max = len(dict["names"][1]);
    print(f"Longest Name is {longestName}");
    
    if(dict["isDict"]):
        print("This is a dictionary");
    else:
        print("This is not a dictionary");
    
print_largest(variables);