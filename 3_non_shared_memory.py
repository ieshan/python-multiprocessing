from multiprocessing import Process, current_process
import random


def generate_random_numbers(data: list):
	for _ in range(10):
		data.append(random.randint(1, 101))
	print(current_process().name, "data", data)


random_numbers = []

print("Data in parent process", random_numbers)

process_1 = Process(target=generate_random_numbers, args=(random_numbers, ))
process_1.start()
process_1.join()

print("Data in parent process", random_numbers)

process_2 = Process(target=generate_random_numbers, args=(random_numbers, ))
process_2.start()
process_2.join()
