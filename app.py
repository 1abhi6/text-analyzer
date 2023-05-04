from flask import Flask, render_template, request, redirect
from database import Database
import api

app = Flask(__name__)
db = Database()
api = api.API()


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/perform_registration', methods=['POST'])
def perform_registration():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    response = db.insert(name, email, password)

    if response:
        return render_template('login.html', register_success=True)
    return render_template('register.html', register_failed=True)


@app.route('/perform_login', methods=['POST'])
def perform_login():
    email = request.form.get('email')
    password = request.form.get('password')

    response = db.fetch(email, password)

    if response:
        return redirect('/profile')
    return render_template('login.html', login_failed=True)


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/ner')
def ner():
    return render_template('ner.html')


@app.route('/perform_ner', methods=['POST'])
def perform_ner():
    text = request.form.get('text')
    response = api.sentiment_analysis(text)
    return render_template('ner.html', response=response,text=text)


app.run(debug=True)
