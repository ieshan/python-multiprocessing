from multiprocessing import Manager, Process


def add_records(records):
	records.append(("Salayhin", 4))
	records.append(("Shemul", 5))
	records.append(("Eshan", 6))
	records.append(("Adnan", 7))
	records.append(("Ekramul", 8))
	records.append(("Shuvo", 9))


def print_records(records):
	for record in records:
		print(f"Name {record[0]}\nScore {record[1]}")


def sum_score(records, result):
	for record in records:
		result.value += record[1]


with Manager() as manager:
	records = manager.list([("Abdullah", 1), ("Ashfak", 2), ("Shihab", 3)])
	score_sum = manager.Value("i", 0)
	add_process = Process(target=add_records, args=(records, ))
	print_process = Process(target=print_records, args=(records, ))
	sum_process = Process(target=sum_score, args=(records, score_sum, ))

	add_process.start()
	print_process.start()
	sum_process.start()

	add_process.join()
	print_process.join()
	sum_process.join()

	print("Total score", score_sum.value)
