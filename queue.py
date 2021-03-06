# Dora Jambor
# queue.py
# 12.12.2014

class Queue:
    def __init__(self,queue = None):
        if queue is None:
            self.queue = []
        else:
            self.queue = list(queue)
            
    def insert(self,element):
        self.queue.append(element)

    def remove(self):
        try:
            return self.queue.pop(0)
        except IndexError:
            raise IndexError('Queue is empty')
    def show(self):
        print self.queue
            
q = Queue([1,2,3])
q.insert(4)
q.show()
q.remove()
q.show()
      
