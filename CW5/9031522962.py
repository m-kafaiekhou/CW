
class Human:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = self.validate_age(age)

    @staticmethod
    def validate_age(age, ranje=None):
        if ranje != None:
            if  ranje[0]< age < ranje[1]:
                return age
            else:
                raise ValueError("Not in age range")
        else:
            if age < 0:
                raise ValueError("Wronge age format")
            else:
                return age

class Player(Human):
    def __init__(self, name, age, salary, position, score) -> None:
        super().__init__(name, age)
        self.salary = self.validate_salary(salary)
        self.age = self.validate_age(age, ranje=[15,30])
        self.position = position
        self.score = self.validate_score(score)

    @staticmethod
    def validate_salary(salary):
        if salary < 0:
            raise ValueError("wrong salary format")
        else:
            return salary
        
    @staticmethod
    def validate_score(score):
        if 0 <score < 100:
            return score
        else:
            raise ValueError("wrong score format")
        
class Coach(Human):
    def __init__(self, name, age, salary, start_of_contract, end_of_contract) -> None:
        super().__init__(name, age)
        self.salary = salary
        self.age = self.validate_age(age, ranje=[30,65])
        self.start_of_contract = start_of_contract
        self.end_of_contract = end_of_contract
        
    def __repr__(self) -> str:
        return self.name

class Team:
    coach_list = []
    def __init__(self, team_name, team_score, player_list, team_coach):
        self.team_name = team_name
        self.team_score = team_score
        self.player_list = player_list
        self.team_coach = self.validate_teamCoach(team_coach)
        self.__class__.coach_list.append(self.team_coach)

    @classmethod
    def validate_teamCoach(cls,coach_name):
        
        if coach_name in cls.coach_list:
            raise ValueError("error")
        else:
            return coach_name

    def __len__(self):
        return len(self.player_list)
        

c1 = Coach("ahmad", 50, 500, 1, 30)
t1 = Team("baradaranahmadi", 6,["a","b","c","d","e","f","g","h","i","j","k"], c1)

print(t1.__dict__)

