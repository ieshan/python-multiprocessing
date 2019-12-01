from multiprocessing import Process, Value
import time


def add_5_no_lock(total):
	for i in range(0, 100):
		time.sleep(0.01)
		total.value += 5


def sub_5_no_lock(total):
	for i in range(0, 100):
		time.sleep(0.01)
		total.value -= 5


if __name__ == "__main__":
	total = Value("i", 0)

	add_process = Process(target=add_5_no_lock, args=(total, ))
	sub_process = Process(target=sub_5_no_lock, args=(total, ))

	add_process.start()
	sub_process.start()

	add_process.join()
	sub_process.join()

	print(total.value)
