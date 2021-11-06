class Nstr(str):
    def __sub__(self, other):
        return self.replace(other,'')

a=Nstr("I love yu c")
b=Nstr("ov")

print(a-b)
