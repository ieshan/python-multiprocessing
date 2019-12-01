from multiprocessing import Process, Queue


def square(numbers, queue):
	for number in numbers:
		queue.put(number * number)


def print_results(queue):
	while not queue.empty():
		print(queue.get())


if __name__ == "__main__":
	numbers = range(1, 5)
	queue = Queue()

	square_process = Process(target=square, args=(numbers, queue))
	result_process = Process(target=print_results, args=(queue, ))

	square_process.start()
	result_process.start()

	square_process.join()
	result_process.join()
