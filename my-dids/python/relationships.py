#  ONE to ONE relentionship
class plants:
    def __init__(self,cash_crop,food_crop):
        self.cash_crop = cash_crop
        self.food_crop = food_crop

    def __str__(self):
        return f"the cash crops are :{self.cash_crop} and cash crops:{self.food_crop}"


class fruit:
    def __init__(self,sales, home_made,plants):
        self.sales = sales
        self.home_made = home_made    
        self.plants = plants     
    def __str__(self):
        return f"The home :{self.sales} and the home made fruits are {self.home_made} also other plants are{self.plants} "
          

#instant
plants1 = plants("coffee", "maize") 
fruit1 = fruit("apple","banana", plants1)


print(fruit1)


### one to many
#One to many ...
#classroom and students
class Classroom:

    def init(self, name, number):
        self.name = name
        self.number = number
        self.students = [] #to hold students

    def add_student(self, student):

        self.students.append(student)

class Students:

    def init(self, email, age, cohort, fees):

        self.email = email
        self.age = age
        self.cohort = cohort
        self.fees = fees

#Instances
classroom1 = Classroom('Software Eng.', 'Room 11')

stud1 = Students('Tembo@gmail.com', 15, 'SDFT11', '0.00 balance')
stud2 = Students('charles@gmail.com', 19, 'SDFT11', '0.00 balance')
stud3 = Students('sucdi@gmail.com', 17, 'SDFT11', '0.00 balance')
stud4 = Students('rose@gmail.com', 16, 'SDFT11', '0.00 balance')

#associate students with the classroom
classroom1.add_student(stud1)
classroom1.add_student(stud2)
classroom1.add_student(stud3)
classroom1.add_student(stud4)

print(f'Classroom {classroom1.name}.... {classroom1.number}')
print('The following are the students in this classroom : ')

for student in classroom1.students:
    print(f'Student Email : {student.email}, Student age : {student.age},, Student Cohort : {student.cohort}, Student Fees Balance : {student.fees}' )
    
    
    
    

class Laptop:

    def init(self, logo, location):

        self.logo = logo
        self.location = location
        self.laptops = []

    def add_laptop(self, laptop):
        self.laptops.append(laptop)

class Pc:
    def init(self, name, warrant, price):

        self.name = name
        self.warrant = warrant
        self.price = price

#Instances
laptop1 = Laptop('PC', 'Malindi')

pc1 = Pc('Dell', '6 months', '60, 000')
pc2 = Pc('Mac', '6 months', '300, 000')
pc3 = Pc('Hp', '6 months', '50, 000')
pc4 = Pc('Acer', '6 months', '100, 000')

#associate ...
laptop1.add_laptop(pc1)
laptop1.add_laptop(pc2)
laptop1.add_laptop(pc3)
laptop1.add_laptop(pc4)

print(f'{laptop1.logo}, {laptop1.location}')
print('This are the laptops available in our store : ')

for tembo in laptop1.laptops:

    print(f'Type: {tembo.name}, Warrant : {tembo.warrant}, {tembo.price}')


    #many to many relantionship


# class author:
#     def __init__(self,name,year):
#         self:name= name
#         self:year = year
#         self:book = []

#         def add_book(self,author):
#             self.apend.book(author)
