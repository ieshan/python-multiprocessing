from multiprocessing import Pipe, Process


def send_msgs(pipe, msgs):
	for msg in msgs:
		pipe.send(msg)
	pipe.close()


def receive_msgs(pipe):
	while True:
		msg = pipe.recv()
		if msg == "END":
			break
		print(f"Received message '{msg}'")


msgs = ["Hey", "Hello", "Hi", "END", ]
parent_pipe, child_pipe = Pipe()

sender_process = Process(target=send_msgs, args=(parent_pipe, msgs, ))
receiver_process = Process(target=receive_msgs, args=(child_pipe, ))

sender_process.start()
receiver_process.start()

sender_process.join()
receiver_process.join()


