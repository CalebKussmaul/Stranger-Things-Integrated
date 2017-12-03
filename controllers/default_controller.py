from flask import render_template
from messages import messages


def index():
    return render_template('index.html')


def display(message):
    messages.add_message(message)
    return None, 204
