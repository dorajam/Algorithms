# Dora Jambor
# stack.py
# December 2015

class Stack:
    def __init__(self,lista = None):
        if lista is None:
            self.lista = []
        else:
            self.lista = list(lista)
            
    def put(self,item):
        self.lista.append(item)
        
    def remove(self):
        try:
            self.lista.pop()
        except IndexError:
            raise IndexError('Stack\'s empty')
            
    def __str__(self):
        return str(self.lista)
        