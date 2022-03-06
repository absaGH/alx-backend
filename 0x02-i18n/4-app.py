#!/usr/bin/env python3
""" Basic Babel setup with babel.localeselector decorator
    and locale as URL parameter
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)
""" Babel object is instantiated using app """


class Config(object):
    """ configiguration variable for available languages
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
""" Config is used to setup app """


@app.route('/')
def root():
    """ route to render 4-index.html """
    return render_template("4-index.html")


@babel.localeselector
def get_locale():
    """ return the best match from supported language """
    locLang = request.args.get('locale')
    suppLang = app.config['LANGUAGES']
    if locLang in suppLang:
        return locLang
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
