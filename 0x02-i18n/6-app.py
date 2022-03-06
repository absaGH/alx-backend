#!/usr/bin/env python3
""" Basic Babel setup with babel.localeselector decorator"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)
""" Babel object is instantiated using app """

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
""" mock of a database user table """


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
    """ route to render 6-index.html """
    return render_template("6-index.html")


@babel.localeselector
def get_locale():
    """ select the best match from supported languages """
    locLang = request.args.get('locale')
    suppLang = app.config['LANGUAGES']
    if locLang in suppLang:
        return locLang
    userId = request.args.get('login_as')
    if userId:
        locLang = users[int(userId)]['locale']
        if locLang in suppLang:
            return locLang
    locLang = request.headers.get('locale')
    if locLang in suppLang:
        return locLang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """ returns a user dictionary or None
    if the ID cannot be found or if login_as was not passed """
    try:
        userId = request.args.get('login_as')
        return users[int(userId)]
    except Exception:
        return None


@app.before_request
def before_request():
    """ executed before all other functions and
        use get_user to find a user if any,
        and set it as a global on flask.g.user
    """
    g.user = get_user()


if __name__ == "__main__":
    app.run()
