import threading
import random
import time

class Thread(threading.Thread):
    running = True
    deadlock = False

    def __init__(self, name, rightFork, leftFork):
        threading.Thread.__init__(self)
        self.name = name
        self.rightFork = rightFork
        self.leftFork = leftFork

    def run(self):
        while Thread.running:
            time.sleep(random.randint(5, 15))
            fork = self.leftFork
            fork2 = self.rightFork

            while True:
                if not Thread.running:
                    return
                fork.acquire(True)
                locked = fork2.acquire(False)

                if not Thread.deadlock:
                    if locked:
                        break
                    fork.release()
                    tmp = fork
                    fork = fork2
                    fork2 = tmp

            print(self.name + " zaczyna jesc.")
            time.sleep(random.randint(1, 10))
            print(self.name + " skonczyl jesc.")
            fork.release()
            fork2.release()


def Main():
    random.seed(12345)
    forks = []
    philosopherNames = ('Buddha', 'Aristotle', 'Confucius','Sun Tzu', 'Socrates')
    philosopherList = []

    for i in range(5):
        forks.append(threading.Lock())

    for i in range(5):
        philosopherList.append(Thread(philosopherNames[i], forks[i % 5], forks[(i + 1) % 5]))

    data = input("Aby triggerowac deadlock prosze wpisac d")
    if data == "d":
        Thread.deadlock = True

    for i in philosopherList:
        i.start()
    time.sleep(30)
    Thread.running = False
    print("Main finished")

Main()