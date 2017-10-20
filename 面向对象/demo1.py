class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s:%s '% (self.__name,self.__score))

std = Student('unicorn', 99)
std.print_score()

#3#
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def print_score(self):
#         print('%s:%s '% (self.name,self.score))
# std = Student('unicorn', 99)
# std.score = 60
# std.print_score()

#2#
# bar = Student('unicorn', 99)
# print(bar.name,bar.score)

#1#
# bar.name = 'unicorn'
# print(bar.name)
# print(Student)