from flask import Flask, render_template, redirect, url_for, request, g, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm, Form
from wtforms import StringField, SubmitField, Form, BooleanField, PasswordField, validators
from wtforms.validators import DataRequired
from datetime import datetime
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
import requests
from api import dataweather
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '45345FDF-FREEDJHG4-HDGDTER5'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    Bootstrap(app)

    return app

app = create_app()

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    ime = db.Column(db.String(64))
    korisnicko_ime = db.Column(db.String(64))
    email = db.Column(db.String(64))
    lozinka = db.Column(db.Text)
    def __repr__(self):
        return '{},{},{},{},{}'.format(self.id, self.ime, self.korisnicko_ime, self.email, self.lozinka)


@app.route('/home')
def index():
    weather = dataweather()
    return render_template("index.html", weather = weather, datetime = datetime)

@app.route('/profile')
def indexprofile():
    weather = dataweather()
    return render_template("profile.html", weather = weather, datetime = datetime)

@app.route('/')
def indexlogin():
    weather = dataweather()
    return render_template("login.html", weather = weather, datetime = datetime)

@app.route('/gallery')
def indexgallery():
    weather = dataweather()
    return render_template("gallery.html", weather = weather, datetime = datetime)

@app.route('/guestgallery')
def guestgallery():
    weather = dataweather()
    return render_template("guestgallery.html", weather = weather, datetime = datetime)

@app.route('/', methods=['GET', 'POST'])
def login():
    db.create_all()
    if request.method == 'POST' and request.form.get('kreiraj_racun'):
        user = User(ime = request.form['name'], korisnicko_ime = request.form['username'], email = request.form['email'], lozinka = generate_password_hash(request.form['password']))
        db.session.add(user)
        db.session.commit() 

        return render_template('created.html')

    elif request.method == 'POST' and request.form.get('prijava'):
        user = User.query.filter_by(korisnicko_ime = request.form['username_prijava']).first() 
        if user: 
            if check_password_hash(user.lozinka, request.form['password_prijava']):
                session['username'] = user.korisnicko_ime
                session['email'] = user.email
                return render_template("profile.html", weather = dataweather(), datetime = datetime)
            else:
                return render_template('no_user.html')
        else:
            return render_template('no_user.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/signup')
def indexsignup():
    weather = dataweather()
    return render_template("signup.html", weather = weather, datetime = datetime)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'nikolavjezbapzw@gmail.com'
app.config['MAIL_PASSWORD'] = 'programiranjezaweb'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html')

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == "POST":
        email = request.form['email']
        subject = request.form['subject']
        msg = 'Postovani, \nzahvaljujemo Vam na vasoj zainteresiranosti za boravak u nasem smjestaju. \nOvo je automatska poruka. \nMolimo Vas da u odgovoru na ovu poruku navedete datume za koje ste zainteresirani.\nVasi Memories apartmani.'

        message = Message(subject, recipients=[email], sender="nikolavjezbapzw@gmail.com")

        message.body = msg

        mail.send(message)

        success = "Hvala na upitu! Rezervacija zapoceta. Provjerite svoj mail."

        return render_template("send.html", success=success)

@app.route('/usersend', methods=['GET', 'POST'])
def usersend():
    if request.method == "POST":
        email = request.form['email']
        subject = request.form['subject']
        msg = 'Postovani, \nzahvaljujemo Vam na vasoj zainteresiranosti za boravak u nasem smjestaju. \nOvo je automatska poruka. \nMolimo Vas da u odgovoru na ovu poruku navedete datume za koje ste zainteresirani.\nVasi Memories apartmani.'

        message = Message(subject, recipients=[email], sender="nikolavjezbapzw@gmail.com")

        message.body = msg

        mail.send(message)

        success = "Hvala na upitu! Rezervacija zapoceta. Provjerite svoj mail."

        return render_template("usersend.html", success=success)

mail.init_app(app)

@app.route('/guestkontakt')
def guestkontakt():
    return render_template('guestkontakt.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))