class Student:
    Count = 0
    def __init__(self,Name,banji,xuehao,male):
        self.Name=Name
        self.banji=banji
        self.xuehao=xuehao
        self.male=male
        Student.Count += 1

    def displayCount(self):
        return Student.Count

class xStudent(Student):
    xCount = 0
    
    def BKW(self):
        print "xStudent can Bei Ke Wen"
    def KS(self):
        print "xStudent can Kou Suan"



class zStudent(Student):
    zCount = 0

    def WL(self):
        print "zStudent can Wu Li"
    def HX(self):
        print "zStudent can Hua Xue"
