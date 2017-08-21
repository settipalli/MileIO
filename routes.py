from os import environ as env
from flask import Flask, render_template, request, session, redirect, url_for, abort
from flask_mail import Mail, Message
from flask_security import Security, SQLAlchemyUserDatastore, login_required
from models import db, User, Role
from config import config

# helper method
get_from_env = lambda key: env[key] if key in env else ''

app = Flask(__name__)
app.config.from_object(config['dev'])
mail = Mail(app)
db.init_app(app)

# setup flask-security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# get a handle for the logger
log = app.logger

@app.route('/')
def index():
    log.debug('rendering index.html')
    return render_template('index.html')


@app.route('/terms')
def terms():
    log.debug('rendering terms.html')
    return render_template('terms.html')


@app.route('/privacy')
def privacy():
    log.debug('rendering privacy.html')
    return render_template('privacy.html')


@app.route('/about')
def about():
    log.debug('rendering about.html')
    return render_template('about.html')


@app.route('/profile')
@login_required
def profile():
    return render_template(
        'profile.html',
        content='Profile Page',
        twitter_conn=social.twitter.get_connection(),
        facebook_conn=social.facebook.get_connection(),
        foursquare_conn=social.foursquare.get_connection(),
        google_conn=social.google.get_connection()
    )


@app.route('/signin')
@login_required
def signin():
    return render_template(
        'login.html',
        content='Login Page',
        twitter_conn=social.twitter.get_connection(),
        facebook_conn=social.facebook.get_connection(),
        foursquare_conn=social.foursquare.get_connection(),
        google_conn=social.google.get_connection()
    )


# helper routines

# create a fresh copy of the DB tables (DB should be present)
def init_db():
    with app.app_context():
        # SQLAlchemy now knows what the 'current' app is while within this block
        # therefore, you can now run:
        db.drop_all()
        db.create_all()
        # create a test user
        user_datastore.create_user(email=get_from_env('ADMIN_MAIL_ID'), password=get_from_env('ADMIN_MAIL_PASSWORD'))
        db.session.commit()
        log.info('Database created.')


if __name__ == '__main__':
    if 'MODE' in env and env['MODE'] == 'production':
        app.run()
    else:
        app.run(debug=True)
