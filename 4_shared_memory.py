import multiprocessing
import random


def generate_random_numbers(data):
	for i in range(10):
		data[i] = random.randint(1, 101)
	print("Random numbers in ", multiprocessing.current_process().name, [num for num in data])


def sum_of_numbers(numbers, total):
	total.value = sum(numbers)
	print("Total in ", multiprocessing.current_process().name, total.value)


random_numbers = multiprocessing.Array("i", 10)
total = multiprocessing.Value("i", 0)

print("Random numbers in parent process before MP", [num for num in random_numbers])

process_1 = multiprocessing.Process(target=generate_random_numbers, args=(random_numbers, ))
process_1.start()
process_1.join()

print("Random numbers in parent process after MP", [num for num in random_numbers])
print("Total in parent process before MP", total.value)

process_2 = multiprocessing.Process(target=sum_of_numbers, args=(random_numbers, total))
process_2.start()
process_2.join()

print("Total in parent process after MP", total.value)
