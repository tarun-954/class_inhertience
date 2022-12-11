class name:
    def __init__(self,first_name,second_name,age):
        self.first_name=first_name
        self.second_name=second_name
        self.age=age
    def full_name(self):
        return f"Your name is {self.first_name} {self.second_name}"


object_Name=name("tarun","choudhary",19)
object_Name2=name("vaishu","choudhary",18)
print(object_Name.full_name())
print(object_Name2.full_name())

