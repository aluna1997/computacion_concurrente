from multiprocessing import Lock,Array

class lock_based_queue():
    
    def __init__(self, capacity):
        self.head = 0
        self.tail = 0
        self.items = Array("i",capacity)
        self.lock = Lock()
        
    def index(self,x):
        c = 0
        for i in self.items[:]:
            if i == x:
                return c
            else:
                c += 1
                
        
    def enq(self, x):
        self.lock.acquire()
        try:
            if (self.tail - self.head) == len(self.items):
                raise Exception("FullException")
            self.items[self.tail % len(self.items)] = x
            self.tail += 1
        except Exception as err:
            raise err
        finally:
            self.lock.release()
    
    def deq(self):
        self.lock.acquire()
        try:
            if self.tail == self.head:
                raise Exception("EmptyException")
            x = self.items[self.head % len(self.items)]
            self.items[self.index(x)] = 0
            self.head += 1
            return x
        except Exception as err:
            raise err
        finally:
            self.lock.release()
