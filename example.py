import time
import threading

def foo():
    print("1")
    time.sleep(1)
    print("2")

thread1 = threading.Thread(target=foo)
thread2 = threading.Thread(target=foo)

thread1.start()
thread2.start()

thread1.join()
thread2.join()