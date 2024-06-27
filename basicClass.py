class Myclass:
    x=5

p1 = Myclass()
# print(p1.x)


class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = person('john',87)
print(p1.name)
print(p1.age)
