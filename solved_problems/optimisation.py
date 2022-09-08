from time import time
from threading import Thread
import concurrent.futures

NB_ITERATIONS = 1_000_000

# Timer decorator
def timer(func):
    def f(*args, **kwargs):
        start = time()
        rv = func(*args, **kwargs)
        end = time()
        print('Elapsed time: {:.3f} [s]'.format(end-start)) # time in seconds
        #print('Elapsed time: {:.3f} [ms]'.format((end-start)*1000)) # time in milliseconds
        return rv
    return f


# class CustomThread(Thread):
#     def __init__(self, tid):
#         super(CustomThread, self).__init__()
#         self.tid = tid
#         self.n = NB_ITERATIONS
#         self.s = 0
    

#     def run(self):
#         if self.tid == 1:
#             self.s = sum((_ for _ in range(self.n) if _ % 3 == 0))
#         elif self.tid == 2:
#             self.s = sum((_ for _ in range(self.n) if _ % 5 == 0))
#         elif self.tid == 3:
#             self.s = sum((_ for _ in range(self.n) if _ % 3 == 0 and _ % 5 == 0))
#         else:
#             self.s = 0
    

#     def join(self, *args):
#         Thread.join(self, *args)
#         return self.s


def tfunction(tid):
    if tid == 0:
        return sum((_ for _ in range(NB_ITERATIONS) if _ % 3 == 0 and _ % 5 != 0))
    if tid == 1:
        return sum((_ for _ in range(NB_ITERATIONS) if _ % 5 == 0 and _ % 3 != 0))
    if tid == 2:
        return sum((_ for _ in range(NB_ITERATIONS) if _ % 5 == 0 and _ % 3 == 0))
    return -1


def add(idx):
    if idx % 3 == 0 or idx % 5 == 0:
        return idx
    return 0



@timer
def main():
    # threads = [None] * 3
    # for i in range(len(threads)):
    #     threads[i] = CustomThread(i+1)
    #     threads[i].start()

    # total = threads[0].join() + threads[1].join() - threads[2].join()
    # return total

    with concurrent.futures.ThreadPoolExecutor(max_workers = 10) as executor:
        # results = [executor.submit(tfunction, tid) for tid in range(3)]
        # total = 0
        # for f in concurrent.futures.as_completed(results):
        #     total += f.result()
        # return total
        #return sum(executor.map(tfunction, [0,1,2]))
        return sum(executor.map(add, [_ for _ in range(NB_ITERATIONS)]))
        

if __name__ == '__main__':
    total = main()
    print(total)