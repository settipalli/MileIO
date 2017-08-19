from os import environ as env
from collections import namedtuple
from flask import Flask, render_template, request, session, redirect, url_for, abort

app = Flask(__name__)
app.secret_key = 'f6da2f74842ece5618b5383c71062e12362cbbd5db13cee0'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/terms')
def terms():
    return render_template('terms.html')


@app.route('/privacy')
def privacy():
    return render_template('privacy.html')


if __name__ == '__main__':
    if 'MODE' in env and env['MODE'] == 'production':
        app.run()
    else:
        app.run(debug=True)
