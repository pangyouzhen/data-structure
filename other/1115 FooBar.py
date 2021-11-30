import threading
from typing import Callable

empty = threading.Semaphore(1)
full = threading.Semaphore(0)


class FooBar:
    def __init__(self, n):
        self.n = n

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            empty.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            full.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            full.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            empty.release()
