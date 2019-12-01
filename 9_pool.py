from multiprocessing import Pool
import time


def sum_square(number):
	s = 0
	for i in range(number):
		time.sleep(0.02)
		s += i * i
	return s


if __name__ == "__main__":
	numbers = range(1, 20)
	p = Pool(processes=2)
	start_time = time.time()
	result = p.map(sum_square, numbers)
	end_time = time.time() - start_time

	p.close()
	p.join()

	print(result)
	print(f"Process time: {end_time}")
