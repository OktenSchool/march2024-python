import threading
import time

# def for_thread(a,b):
#     for i in range(100):
#         print('Hello', a,b)
# thread = threading.Thread(target=for_thread, args=(5, 2))
# thread.start()
# for i in range(100):
#     print(i)
# else:
#     print('finish')
#
# # print(threading.current_thread().name)


# def show(n):
#     for i in range(n):
#         print(i, threading.current_thread().name)
#         time.sleep(1)
#
#
# thread1 = threading.Thread(target=show, args=(5,))
# thread2 = threading.Thread(target=show, args=(10,))
#
# thread1.start()
# thread1.join()
# thread2.start()
# thread2.join()
# for i in range(100):
#     print(i)

count = 0
lock = threading.Lock()


def inc():
    with lock:
        global count
        count += 1
        print(count)


threads = []
for _ in range(1000):
    thread = threading.Thread(target=inc)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
