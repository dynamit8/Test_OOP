class Citizen(object):
    amount = 0
    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        Citizen.amount += 1

    def get_fullname(self):
        return str(self.first_name) +' '+ str(self.last_name)

    
    
# How to create an instance of class Citizen as 'Jor'
Jor = Citizen('Wisanu', 'Upatumphun', '21-09-1985')
# How to get first_name of Jor
print(Jor.first_name)
# How to get Jor's fullname
print(Jor.get_fullname())

"""
Problems...
1. I need new citizen instances to represent 1 family at least three people(Father, Mother, Child).
2. I need a new class called 'Employee' which has 5 attributes
   (first_name,last_name,date_of_birth,salary,employer).
3. I need a new instance of class 'Employee' as a Japanese guy. 
   When getting fullname of this guy, it must be 'Lastname Firstname' ordered.

"""
