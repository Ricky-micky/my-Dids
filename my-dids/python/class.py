#  1-1 relentionship
class Profile:
    def __init__(self, profile_picture ,bio):
        self.profile_picture =profile_picture
        self.bio = bio

class User:
    def __init__(self, email, profile):
        self.email = email
        self.profile = profile 
         
        

  ##1- many
class student:
    def __init__(self, name):
        self.name = name

class Tm:
    def __init__(self, name):
        self.name = name
        self.student = []

    def add_student(self, student):
        self.student.extend(student)

s1 = student("Ricky")      
s2 = student("mary")      
s3 = student("gibson")      
s4 = student("mark")      

tm = Tm("Hamida")
tm.add_student([s1,s2,s3,s4])
for  student in tm.student:
    
print(tm.student)