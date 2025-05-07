import threading
import time
import random

NUM_PHILOSOPHERS = 5

class Philosopher(threading.Thread):
    def __init__(self, index, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.index = index
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while True:
            self.think()
            self.eat()

    def think(self):
        print(f"فیلسوف {self.index} در حال فکر کردن است.")
        time.sleep(random.uniform(1, 3))

    def eat(self):
        # جلوگیری از بن‌بست با تغییر ترتیب گرفتن چنگال‌ها برای آخرین فیلسوف
        if self.index == NUM_PHILOSOPHERS - 1:
            first_fork, second_fork = self.right_fork, self.left_fork
        else:
            first_fork, second_fork = self.left_fork, self.right_fork

        with first_fork:
            with second_fork:
                print(f"فیلسوف {self.index} در حال خوردن غذا است.")
                time.sleep(random.uniform(1, 2))
                print(f"فیلسوف {self.index} غذا خوردن را تمام کرد.")

def main():
    forks = [threading.Lock() for _ in range(NUM_PHILOSOPHERS)]
    philosophers = []

    for i in range(NUM_PHILOSOPHERS):
        left_fork = forks[i]
        right_fork = forks[(i + 1) % NUM_PHILOSOPHERS]
        philosopher = Philosopher(i, left_fork, right_fork)
        philosophers.append(philosopher)
        philosopher.start()

if __name__ == "__main__":
    main()
