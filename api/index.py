from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'BlueEgg63's page:\n Projects: Will be updated\n No projects yet!'

@app.route('/about')
def about():
    return 'About'
