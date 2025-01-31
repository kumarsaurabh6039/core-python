class Greet:
    def _init_(self, name, age):
        self.name = name
        self.age = age
        
    def greetMe(self):
        print(f"Hello {self.name}")
        
    def myAge(self):
        print(f"Your Age is {self.age}")
        
    
obj1 = Greet('Shiv', 32)
obj1.greetMe()
obj1.myAge()


class Cuboid:
    def _init_(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        
    def getVolume(self):
        return f"Cuboid Volume is {self.length * self.width * self.height}"
    
    
    def getArea(self):
        return f"LitArea of Cuboid is {self.length * self.width}"

    def getPerimeter(self):
        return f"Perimeter of Big Side {self.length + self.width}" 
    
    
obj1 = Cuboid(10, 5, 3)
print(obj1.getArea())

print(obj1.getPerimeter())  

print(obj1.getVolume())   

print(obj1.height)  
print(obj1.length)
print(obj1.width)



obj2 = Cuboid(12, 4, 2)
print(obj2.getArea())
print(obj2.length)

print(id(obj1))
print(id(obj2))

##############################################
############################################
# 1. Create a Class and Objects
# Create a class Car with the following:

# Attributes: brand, model, year.
# A method display_details that prints the car details.
class cars:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def display_details(self):
        print (f"{self.brand},{self.model},{self.year}")
        
obj1= cars('Thar','ptah nahi',2026)
obj2 = cars('sift','nahi ptah',2022)
obj1.display_details()
obj2.display_details()

#################################################
#################################################
# 3. Inheritance
# Create a parent class Animal with a method speak that prints a generic sound.
# Then, create two child classes:

# Dog: Override the speak method to print "Bark".
# Cat: Override the speak method to print "Meow".

class Animal:
    def speak(self):
        print("Some generic sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

class Cat(Animal):
    def speak(self):
        print("Meow")
dog = Dog()
cat = Cat()
dog.speak()
cat.speak()
# 4. Bank Account System
# Create a class BankAccount with the following:

# Attributes: account_number, balance.
# Methods:
# deposit(amount): Adds the amount to the balance.
# withdraw(amount): Deducts the amount if enough balance exists; otherwise, print "Insufficient funds".
# check_balance(): Prints the current balance.

class account:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = balance
    def deposit(self,amount):
        return f"{self.balance+amount}"
    def withdraw(self,amount):
        if amount > self.balance:
            return f"tumhare account me kam paise hai or dalo"
        else:
            return f"{self.balance-amount}"
    def check_balance(self):
        return f'{self.balance}'
check_balance = account(4796021,6000)
print(check_balance.deposit(500))
print(check_balance.withdraw(7000))
print(check_balance.check_balance())
        
############################################
#################################################
# write a class named car with instance variables brand and model .
# and an instance method display _info that print the car brand and model.

class cars:
    def __init__(self,brand,model):
       self.brand = brand
       self.model = model
    def display_info(self):
        print(f"{self.brand},{self.model}")
car_infro = cars('Thar',2024)
car_infro.display_info()

# write a class named circle with an instance variable radius and a method area that calculates 
# and returns the area of the circle.
class area:
    def __init__(self,radius):
        self.radius= radius
    def area_of_circle(self):
        return f'{3.14 * self.radius*self.radius}'
obj1 = area(5)
print(obj1.area_of_circle())
        
# write a class named bankaccount with instance variables account_number and balance.
# add methods to deposit and withdraw money from the account.
class account:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = balance
    def deposit(self,amount):
        return f'{self.balance+amount}'
    def withdraw(self,amount):
        if self.balance<amount:
            return f"chala ja gareeb"
        else:
            return f"{self.balance-amount}"
    def available_balance(self):
        return f"{self.balance}"
    
check_balance = account(479602130000592,50000)
print(check_balance.deposit(500))
print(check_balance.withdraw(78990008877))
print(check_balance.available_balance())



            
    
        
