from threading import Thread
import sys

# scrapy startproject 'NAME_PROJECT'

COUNTDOWN = 5


class Th(Thread):
    num = 0

    def __init__(self, num):
        sys.stdout.write("Making thread number " + str(num) + " n ")
        sys.stdout.flush()
        Thread.__init__(self)
        self.num = num
        self.countdown = COUNTDOWN

    def run(self):
        while self.countdown:
            sys.stdout.write("Thread " + str(self.num) +
                             " (" + str(self.countdown) + ")n \n")
            sys.stdout.flush()
            self.countdown -= 1


for thread_number in range(5):
    thread = Th(thread_number)
    thread.start()
