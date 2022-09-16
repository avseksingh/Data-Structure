from time import sleep

import threading


def f(name, n, delay):
    for i in range(1, n + 1):
        print(name, i)
        sleep(delay)


print("Normal")
f("One", 5, 1)
f("Two", 5, 2)
print("Thread")

t1 = threading.Thread(target=f, args=("One", 5, 1,))
t2 = threading.Thread(target=f, args=("Two", 5, 2,))

t1.start()
t2.start()
t1.join()
t2.join()
print("Over")
