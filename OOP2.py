# class student:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def profile(self):
#         return f"Your name is {self.name}, you are {self.gender}, and you are {self.age}"
        
# student_1 = student("Joseph", 22, "male")
# print(student_1.profile())



# class student:
#     school 
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def profile(self):
#         return f"Your name is {self.name}, you are {self.gender}, and you are {self.age}"
    
# student.school = "Babcock" #CHANGING A CLASS VARIABLE USING THE CLASS  
# student_1 = student("Joseph", 22, "male")
# student_2 = student("Jide", 18, male)
# print(student_1.profile())




# class Car:
#     no_of_tyres =4
#     def __init__(self, manufacturer, name, year_of_prod):
#         self.manufacturer
#         self.name = name
#         self.year_of_prod = year_of_prod

#     def details(self):
#         return f"{self.manufacturer}, {self.name}, {self.year_of_prod}"
# car_1 = Car("Mercedes Bens", "C300", 2018)
# print(car_1.__dict__)

# print(car_1.details())
# print(car_1.no_of_tyres)




# class Employee:
#     company = "Apple"
#     def __init__(self, name, job, salary):
#         self.name = name
#         self.job = job
#         self.salary = salary

#     def bio(self):
#         return f" hello {self.name}, you work for {Employee.company}"
# emp_1 = Employee("Mariana", "Backend Developer", 4500000)

# print(emp_1.bio())



# class Employee:
#     company = "Apple"
#     def __init__(self, name, job, salary):
#         self.name = name
#         self.job = job  
#         self.salary = salary

#     def bio(self):
#         return f" hello {self.name}, you work for {Employee.company}"
# class marketers(Employee):
#     pass
# marketer_1 = marketers("Esther", "social media marketer", 334433)
# print(marketer_1.bio())
# # # emp_1 = Employee("Mariana", "Backend Developer", 4500000)
# # # print(emp_1.bio())



# class Employee:
#     company = "Apple"
#     raise_percentage = 1.10   #110/100
#     def __init__(self, name, job, salary):
#         self.name = name
#         self.job = job
#         self.salary = salary

#     def raise_salary(self):
#         self.salary = self.salary * self.raise_percentage
#         return self.salary

#     def bio(self):
#         return f" hello {self.name}, you work for {self.company}"
# class marketers(Employee):
#     company = "univelcity"
# marketer_1 = marketers("Esther", "social media marketer", 334433)
# print(marketer_1.bio())
# print(int(marketer_1.raise_salary()))




# class Employee:
#     company = "Apple"
#     raise_percentage = 1.10   #110/100
#     def __init__(self, name, job, salary):
#         self.name = name
#         self.job = job
#         self.salary = salary

#     def raise_salary(self):
#         self.salary = self.salary * self.raise_percentage
#         return self.salary

#     def bio(self):
#         return f" hello {self.name}, you work for {self.company}"
    
# class marketers(Employee):
#     company = "univelcity"
#     raise_percentage = 1.05
# marketer_1 = marketers("Esther", "social media marketer", 334433)
# print(marketer_1.bio())
# print(int(marketer_1.raise_salary()))
# print(marketer_1.)




# class Employee:
#     company = "Apple"
#     raise_percentage = 1.10   #110/100
#     def __init__(self, name, job, salary):
#         self.name = name
#         self.job = job
#         self.salary = salary

#     def raise_salary(self):
#         self.salary = self.salary * self.raise_percentage
#         return self.salary

#     def bio(self):
#         return f" hello {self.name}, you work for {self.company}"
    
# class marketers(Employee):
#     company = "univelcity"
#     raise_percentage = 1.05

#     def __init__(self, name, job, salary):
#         super().__init__(name, job, salary)
#         self.years_of_experience = years_of_experience 
    
#     def bio(self):
#         return {self.name}, {self.salary}, {self.years_of_experience}




# marketer_1 = marketers("Esther", "social media marketer", 334433, 5)
# print(marketer_1.bio())
# print(marketer_1.salary)
# print(int(marketer_1.raise_salary()))
# print(marketer_1.years_of_experience)
# print(marketer_1.company)








# class Human:
#     no_of_eyes = 2
#     no_of_legs = 2
#     def __init__(self, name, gender, age):
#         self.name = name
#         self.gender = gender
#         self.age = age

#     def summary(self):
#         return f"Hello {self.name}, you are {self.age}, years old. You are {self.gender}"
    
# class African(Human):
#     race = "Black"

#     def __init__(self, name, gender, age, country):
#         super().__init__(name, gender, age)
#         self.country = country

#     def summary(self):
#         return f"Hello {self.name}, you are {self.age}, years old. You are {self.gender} and you're from {self.country}"
    

# class Nigerian(African):
#     def __init__(self, name, gender, age, state, country="Nigerian"):
#         super().__init__(name, gender, age, country)
#         self.state = state

# nigerian_1=Nigerian("Joseph", "Male", 22, "Nigeria", "Lagos")
# print(nigerian_1.summary())



        

# class Human:
#     no_of_eyes = 2
#     no_of_legs = 2
#     def __init__(self, name, gender, age):
#         self.name = name
#         self.gender = gender
#         self.age = age

#     def summary(self):
#         return f"Hello {self.name}, you are {self.age}, years old. You are {self.gender}"
    
# class African(Human):
#     race = "Black"

#     def __init__(self, name, gender, age, country):
#         super().__init__(name, gender, age)
#         self.country = country

#     def summary(self):
#         return f"Hello {self.name}, you are {self.age}, years old. You are {self.gender} and you're from {self.country}"
    

# class Nigerian(African):
#     def __init__(self, name, gender, age, state, country="Nigerian"):
#         super().__init__(name, gender, age, country)
#         self.state = state

# nigerian_1=Nigerian("Joseph", "Male", 22, "Nigeria", "Lagos")

# print(isinstance(nigerian_1, Nigerian))
# print(isinstance(nigerian_1, African))






# class Human:
#     no_of_eyes = 2
#     no_of_legs = 2
#     def __init__(self, name, gender, age):
#         self.name = name
#         self.gender = gender
#         self.age = age

#     def summary(self):
#         return f"Hello {self.name}, you are {self.age}, years old. You are {self.gender}"
    
# class African(Human):
#     race = "Black"

#     def __init__(self, name, gender, age, country):
#         super().__init__(name, gender, age)
#         self.country = country

#     def summary(self):
#         return f"Hello {self.name}, you are {self.age}, years old. You are {self.gender} and you're from {self.country}"
    

# class Nigerian(African):
#     def __init__(self, name, gender, age, state, country="Nigerian"):
#         super().__init__(name, gender, age, country)
#         self.state = state

# nigerian_1=Nigerian("Joseph", "Male", 22, "Nigeria", "Lagos")


# print(issubclass(Nigerian, Human))




# class Person:
#     def __init__(self, name, country, year_of_birth):
#         self.name = name
#         self.country = country
#         self.year_of_birth = year_of_birth
    
#     def find_age(self):
#         return 2023 - int(self.year_of_birth)
# person_1 = Person("Jide", "Nigeria", 2001)
# print(person_1.find_age())
        

