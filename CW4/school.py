
class School:
    def __init__(self, num, name, age_lst, height_lst, weight_lst):
        self.num = num
        self.name = name
        self.std_lst = Student(age_lst, height_lst, weight_lst).get_av()

    def compare(self, obj):
        if self.std_lst[1] > obj.std_lst[1]:
            print(self.name)
        elif self.std_lst[1] < obj.std_lst[1]:
            print(obj.name)
        else:
            if self.std_lst[2] > obj.std_lst[2]:
                print(self.name)
            elif self.std_lst[2] < obj.std_lst[2]:
                print(obj.name)
            else:
                print("Same")


    
class Student:
    def __init__(self, age, height, weight):
        self.age = eval(age)
        self.height = eval(height)
        self.weight = eval(weight)

    def get_av(self):
        self.avg_age = sum(self.ages) / len(self.ages)
        print(self.avg_age)
        self.avg_height = sum(self.hight) / len(self.hight)
        print(self.avg_height)
        self.avg_weight = sum(self.weight) / len(self.weight)
        print(self.avg_weight)
        
        return self.avg_age, self.avg_height, self.avg_weight
    

A = School(num=2, name="A", age_lst=[1,2,3,4,5], height_lst=[2,3,4,5,6], weight_lst=[11,22,33,44,55])
B = School(num=2, name="A", age_lst=[9,2,3,4,5], height_lst=[9,3,4,5,6], weight_lst=[60,22,33,44,55])

A.compare(B)

    


