class Maths():
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1/self.num2

r = Maths(4,5)

print (" add : %s " % r.add())
print (" sub : %s " % r.sub())
print (" mul : %s " % r.mul())
print (" div : %s " % r.div())
