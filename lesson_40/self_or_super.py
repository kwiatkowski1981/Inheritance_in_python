class Parent:
    def parent_method(self):
        return 'parent_method >'

    def common_method(self):
        return 'common_method <'


class Child(Parent):
    def child_method(self):
        return self.parent_method()

    def common_method(self):
        return super().common_method()


example = Parent()
print(example.parent_method())
print(example.common_method())
example2 = Child()
print(example2.child_method())
print(example2.common_method())
