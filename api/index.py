from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World! More stuff to come!'

@app.route('/about')
def about():
    return 'About'
