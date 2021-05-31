class Parent:
    def get_type(self):
        return 'Parent'


class Child(Parent):
    def get_type(self):
        return 'Child'


sample = Parent()
print(sample.get_type())
sample2 = Child()
print(sample2.get_type())
