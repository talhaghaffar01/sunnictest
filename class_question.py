
class Foo:
    var = 1

    def set_var(self, num: int):
        self.var = num


f1 = Foo()
f2 = Foo()

input()
print(f'{f1.var=}')
print(f'{f2.var=}')

f1.var = 2

input()
print(f'{f1.var=}')
print(f'{f2.var=}')

f2.set_var(3)

input()
print(f'{f1.var=}')
print(f'{f2.var=}')

f2.var = 4

input()
print(f'{f1.var=}')
print(f'{f2.var=}')

Foo.var = 5
f3 = Foo()

input()
print(f'{f1.var=}')
print(f'{f2.var=}')
print(f'{f3.var=}')

Foo.var = 6

input()
print(f'{f1.var=}')
print(f'{f2.var=}')
print(f'{f3.var=}')

f3.var = Foo.var
Foo.var = 7

input()
print(f'{f1.var=}')
print(f'{f2.var=}')
print(f'{f3.var=}')
