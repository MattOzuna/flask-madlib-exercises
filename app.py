from flask import Flask, request, render_template
from stories import Story, story
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# app.config['SECRET_KEY'] = "oh-so-secret"
# debug = DebugToolbarExtension(app)

@app.route('/')
def homepage():
    return render_template('home.html', words=story.prompts)

@app.route('/madlib')
def madlibs():
    answer = story.generate(request.args)
    return render_template('madlib.html', answer = answer)
