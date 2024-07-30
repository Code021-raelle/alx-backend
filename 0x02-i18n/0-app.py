from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
app.config.from_pyfile('mysettings.cfg')
babel = Babel(app)

app.route('/')
def index():
    render_template('index.html')
