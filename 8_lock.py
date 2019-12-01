from multiprocessing import Lock, Process, Value
import time


def add_5_lock(total, lock):
	for i in range(0, 100):
		time.sleep(0.01)
		lock.acquire()
		total.value += 5
		lock.release()


def sub_5_lock(total, lock):
	for i in range(0, 100):
		time.sleep(0.01)
		lock.acquire()
		total.value -= 5
		lock.release()


if __name__ == "__main__":
	lock = Lock()
	total = Value("i", 0)

	add_process = Process(target=add_5_lock, args=(total, lock, ))
	sub_process = Process(target=sub_5_lock, args=(total, lock, ))

	add_process.start()
	sub_process.start()

	add_process.join()
	sub_process.join()

	print(total.value)
