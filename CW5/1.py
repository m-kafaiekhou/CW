import re


class User:
    users = {}

    def __init__(self, nat_id, name, lname, phone, email, passw, age, address):
        self.nat_id = str(nat_id) 
        self.name = name
        self.lname = lname
        self.phone = phone
        self.email = self.validate_email(email)
        self.passw = self.validate_passw(passw)
        self.age = age
        self.address = address
        self.__class__.users[self.nat_id] = self

    @staticmethod
    def validate_passw(passw):
        passw = str(passw)
        if len(passw) < 8:
            raise ValueError("pass must be at least 8 chars")
        if not re.search("[a-z]", passw):
            raise ValueError("pass must contain lower case letters")
        if not re.search("[A-Z]", passw):
            raise ValueError("pass must contain upper case letters")
        if not re.search("[0-9]", passw):
            raise ValueError("pass must contain digits")

        return passw
            
    @staticmethod
    def validate_email(email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if(re.fullmatch(regex, email)):
            return email
        else:
            raise ValueError("Invaid email")
        
    @classmethod  
    def change_pass(cls, nat_id, old_pass, new_pass):
        nat_id = str(nat_id)
        if nat_id not in cls.users:
            raise ValueError("id not found")
        if cls.users[nat_id].passw == old_pass:
            cls.users[nat_id].passw = cls.validate_passw(new_pass)
            print("password has been changed successfuly")
        else:
            raise ValueError("Old password is not valid")

    def __str__(self) -> str:
        return self.nat_id
        


u = User(12,23,3,3,"salam@gmail.com","As8@._djde",10,232)
print(u.users)
u.change_pass(12,"As8@._djde","As50@._djde")
print(u.passw)
        


