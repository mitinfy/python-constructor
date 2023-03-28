# class with methods to raise salary by 5%
class employee:
    def __init__(self, first, last, sal):
        self.fname=first
        self.lname=last
        self.sal=sal
        self.email=first + '.' + last + '@mitindia.in' #concatnate

    def detail(self):
            return 'email:{}'.format(self.email)

    def apply_hike(self):
        self.sal=int(self.sal*(5/100)+self.sal)

emp1=employee('Venkat','joshi',35000)
emp2=employee('Sham','KK',15000)

print(emp1.detail())

print('Before Hike:',emp1.sal)
emp1.apply_hike()
print('After Hike:',emp1.sal)

print(emp2.detail())
print('Before Hike:',emp2.sal)
emp2.apply_hike()
print('After Hike:',emp2.sal)
