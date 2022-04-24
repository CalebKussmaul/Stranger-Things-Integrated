from flask import render_template, redirect
from messages import messages


def index():
    return render_template('index.html')


def display(message):
    messages.add_message(message)
#    return None, 204  # this works fine on desktop browsers, bugs on mobile.
    return redirect("https://1800butts.com/")

