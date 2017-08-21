from os import environ as env
from flask import Flask, render_template, request, session, redirect, url_for, abort
from flask_mail import Mail, Message
from flask_security import Security, SQLAlchemyUserDatastore, login_required
from models import db, User, Role

# helper method
get_from_env = lambda key: env[key] if key in env else ''

app = Flask(__name__)
app.secret_key = get_from_env('APP_SECRET_KEY')

# config values for flask-security
app.config['SECURITY_PASSWORD_HASH'] = get_from_env('SECURITY_PASSWORD_HASH')
app.config['SECURITY_PASSWORD_SALT'] = get_from_env('SECURITY_PASSWORD_SALT')
app.config['SECURITY_RECOVERABLE'] = True

# configure mail
# flask-security uses flask-mail to send emails
app.config['SECURITY_EMAIL_SENDER'] = get_from_env('SECURITY_EMAIL_SENDER')
app.config['MAIL_USERNAME'] = get_from_env('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = get_from_env('MAIL_PASSWORD')
app.config['MAIL_SERVER'] = get_from_env('MAIL_SERVER')
app.config['MAIL_PORT'] = get_from_env('MAIL_PORT')
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

# database configuration

# we do not use the SQLAlchemy event system
# turning it off saves some resources
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = get_from_env('DATABASE_URL')

db.init_app(app)

# setup flask-security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# get a handle for the logger
log = app.logger

@app.route('/')
@login_required
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
