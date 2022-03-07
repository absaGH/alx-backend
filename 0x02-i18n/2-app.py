#!/usr/bin/env python3
""" Basic Babel setup with babel.localeselector decorator"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)
""" instantiate the Babel object """


class Config(object):
    """ configiguration variable for
       available languages
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def root():
    """ route to render 2-index.html """
    return render_template("2-index.html")


@babel.localeselector
def get_locale():
    """ return the best match from the supported languages """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
