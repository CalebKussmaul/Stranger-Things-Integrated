from datetime import datetime
from queue import Queue
import re

msgs = Queue()
record_file = open("messages.txt", "a+")


def is_spam(msg):
    if re.search(r"([a-zA-Z]+)\1{3,}", msg):  # finds 4+ consecutive repeated sequence
        return True
    if "https://" in msg or "http://" in msg or "@" in msg:
        return True
    return False


def add_message(msg):
    global msgs
    if not is_spam(msg):
        msgs.put(msg)
    record(msg, is_spam(msg))


def next_message():
    return msgs.get()


def record(msg, is_spam):
    record_file.write(("SPAM: " if is_spam else "") + str(datetime.now()) + "\n")
    record_file.write(msg + "\n\n")
    record_file.flush()
