from multiprocessing import Process,Lock,Array,Pool
from lock_based_queue import lock_based_queue


def f1(queue):
    queue.enq(1)
    queue.enq(2)
    queue.enq(3)
    queue.enq(4)
    queue.enq(5)
    queue.deq()
    queue.deq()
    queue.deq()
    
def f2(queue):
    queue.enq(6)
    queue.enq(7)
    queue.deq()
    queue.enq(8)
    queue.enq(9)
    #queue.deq()
    queue.enq(10)
    queue.enq(11)
    queue.enq(12)
    
def f3(queue):
    queue.enq(13)
    queue.enq(14)
    #queue.deq()
    #queue.deq()
    #queue.deq()
    queue.enq(15)
    queue.enq(16)
    #queue.deq()
    queue.enq(17)
    queue.enq(18)
    queue.enq(19)


def unir(lista_queues):
    res = []
    for  i in lista_queues:
        if i != 0:
            res.append(i)
    return res

if __name__ == "__main__":
    """
    queue1 = lock_based_queue(10)
    queue2 = lock_based_queue(10)
    queue3 = lock_based_queue(10)
       
    p1 = Process(target=f1,args=(queue1,))
    p2 = Process(target=f2,args=(queue2,))
    p3 = Process(target=f3,args=(queue3,))
    
    p2.start()
    p2.join()
    p1.start()
    p1.join()
    p3.start()
    p3.join()
    
    p = Pool(5)
    print(p.map(unir, [queue1.items[:], queue2.items[:], queue3.items[:]]))
    """
    a = Array("i", 10, lock=True)
    a[0] = 1
    a[1] = 2
    a[2] = 3
    print(a)
            