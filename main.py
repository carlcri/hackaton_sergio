import os
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def root():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    last_directory = os.path.basename(current_directory)

    return f'Current Project: {last_directory}'
