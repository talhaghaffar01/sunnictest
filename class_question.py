
class Foo:
    var = 1

    def set_var(self, num: int):
        self.var = num


f1 = Foo()
f2 = Foo()

print(f1.var)
print()

f1.var = 2

print(f2.var)
print()

f2.set_var(3)

print(f1.var)
print(f2.var)
print()

f2.var = 4

print(f1.var)
print(f2.var)
print()

Foo.var = 5
f3 = Foo()

print(f3.var)
print(f1.var)
print(f2.var)
