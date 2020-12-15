import threading
import random
import matplotlib.pyplot as plt
import time

def histogram(lock, seq, hist):
    lock.acquire()
    for j in seq:
        hist[j] = hist.get(j, 0) + 1
    lock.release()


numberRange = 500
data = []
hist = {}

lock = threading.Lock()
random.seed(time.ctime())

for i in range(100000):
    data.append(random.randint(1, 100))

for i in range(numberRange):
    thread = threading.Thread(target=histogram, args=(lock, data[(i*numberRange):((i+1)*numberRange-1)], hist))
    thread.start()
    thread.join()

plt.bar(*zip(*hist.items()))
plt.show()
