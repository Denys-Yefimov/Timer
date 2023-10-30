from contextlib import contextmanager
import time


@contextmanager
def Timer():
    start_time = time.time()
    yield
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Час виконання: {round(elapsed_time, 4)} секунд")


with Timer():

    for _ in range(100000):
        print(_)
