from multiprocessing import Lock,Array

class lock_based_queue():
    
    def __init__(self, capacity):
        self.head = Array("i",1)
        self.tail = Array("i",1)
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
            if (self.tail[0] - self.head[0]) == len(self.items):
                raise Exception("FullException")
            self.items[self.tail[0] % len(self.items)] = x
            self.tail[0] += 1
            print("Tail: " + str(self.tail[0]))
        except Exception as err:
            raise err
        finally:
            self.lock.release()
    
    def deq(self):
        self.lock.acquire()
        try:
            if self.tail[0] == self.head[0]:
                raise Exception("EmptyException")
            x = self.items[self.head[0] % len(self.items)]
            self.items[self.index(x)] = 0
            self.head[0] += 1
            print("Head: " + str(self.head[0]))
            return x
        except Exception as err:
            raise err
        finally:
            self.lock.release()
