from multiprocessing import Process, current_process
import os
import random
import time


def square(n):
	time.sleep(random.randint(1, 3))
	process_id = os.getpid()
	process_name = current_process().name
	result = n * n
	print(f"Process ID: {process_id}, Process Name: {process_name}")
	print(f"Result of {n} square : {result}")


if __name__ == "__main__":
	parent_process_id = os.getpid()
	print(f"Parent process ID {parent_process_id}")

	processes = list()
	for i in range(1, 10):
		t = Process(target=square, args=(i,))
		processes.append(t)
		t.start()

	for process in processes:
		process.join()

	print("Done!")
