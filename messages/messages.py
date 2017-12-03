from datetime import datetime
from Queue import Queue

msgs = Queue()
record_file = open("messages.txt", "a+")


def add_message(msg):
    global msgs
    msgs.put(msg)

    record(msg)


def next_message():
    return msgs.get()


def record(msg):
    record_file.write(str(datetime.now()) + "\n")
    record_file.write(msg + "\n\n")
    record_file.flush()
