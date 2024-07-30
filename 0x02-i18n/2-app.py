#!/usr/bin/env python3
""" Basic babel setup """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ Configuration for babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Get locale from request """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ Render index page """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
