class Stack:
    def __init__(self):
        self.stack=[]

    def isEmpty(self):
        if self.stack==[]:
            return True

        else:
            return False 

    def push(self,x):
        self.stack.append(x)

    def pop(self):
        if self.stack==[]:
            print("警告！栈为空")
        else:
            self.stack.pop()

    def bottom(self):
        if self.stack==[]:
            print("警告！栈为空")
        else:
            print(self.stack[0])

    def top(self):
        if self.stack==[]:
            print("警告！栈为空")
        else:
            print(self.stack[len(self.stack)-1])

s=Stack()

#print(s.isEmpty())

s.push(3)

s.push(4)

s.bottom()
s.top()

print(s.stack)


