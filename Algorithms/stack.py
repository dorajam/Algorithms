# Dora Jambor
# stack.py
# 12.12.2014

class Stack(list):
    def push(self, item):
        self.append(item)
        
    def isEmpty(self):
        print 'Empty'
        return not self


stack = Stack()
stack.push(5)
stack.push(3)
stack.pop()
