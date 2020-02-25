from multiprocessing import Process,Lock,Queue

class lock_based_queue():
    
    def __init__(self, capacity):
        self.head = 0
        self.tail = 0
        self.items = []
        for i in range(capacity):
            self.items.append(0)
        self.lock = Lock()
        
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
            self.items[self.items.index(x)] = 0
            self.head += 1
            return x
        except Exception as err:
            raise err
        finally:
            self.lock.release()
            return self
            
            
if __name__ == "__main__":
    """
    queue = lock_based_queue(10)
    
    queue.enq(12)
    queue.enq(13)
    queue.enq(14)
    queue.enq(15)
    queue.enq(16)
    print(queue.items)
    
    
    return_dict = manager.dict()
    p1 = Process(target=queue.enq,args=(12,return_dict))
    p2 = Process(target=queue.enq,args=(12,return_dict))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print (return_dict.values())
    """
    q = Queue(100)
    q.put(12)
    q.put(12)
    print(q)
    
      
        