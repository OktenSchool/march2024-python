import time
import math
import multiprocessing

def time_decor(func):
    def inner(*args, **kwargs):
        time_start = time.time()
        func(*args, **kwargs)
        print(time.time() - time_start)
    return inner


def work(num):
    return str(math.sqrt(math.sqrt(math.sqrt(num/2))/20*1500))+'I'

@time_decor
def main_process():
    print('main process')
    r = range(50_000_000)
    with open('file.txt', 'w') as f:
        for i in r:
            res = work(i)
            print(res, file=f)


# main_process()


@time_decor
def mp():
    print('multi process')
    count = multiprocessing.cpu_count()
    print(count, 'CPUs')
    with multiprocessing.Pool(count) as p:
        r = range(50_000_000)
        with open('file.txt', 'w') as f:
            tasks = p.map(work, r)
            for res in tasks:
                print(res, file=f)


mp()
