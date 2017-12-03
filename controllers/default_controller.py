from flask import render_template
from messages import messages


def index():
    return render_template('index.html')


def display(msg):
    messages.add_message(msg)
    print("recieved message: ", msg)
    return None, 204
