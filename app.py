"""
A Flask web application for user authentication and natural language processing.

This application uses the Flask web framework to provide a user authentication system
and natural language processing capabilities. Users can register, login, and access
a profile page. The application also allows users to perform named entity recognition
on text input via an external API.

Attributes:
    app (Flask): A Flask object representing the web application.
    db (Database): A Database object representing the user database.
    api (API): An API object representing an external API for natural language processing.

Functions:
    index: Renders the login page.
    register: Renders the registration page.
    perform_registration: Handles user registration.
    perform_login: Handles user login.
    profile: Renders the user profile page.
    ner: Renders the named entity recognition page.
    perform_ner: Handles named entity recognition.
    page_not_found: Renders the 404 error page.
"""

# import necessary libraries
from flask import Flask, render_template, request, redirect, session
from database import Database
import api
import os

# create a Flask instance
app = Flask(__name__)

# set a random secret key for the Flask app
app.secret_key = os.urandom(24)

# create a Database instance
db = Database()

# create an API instance
api = api.API()


# define the '/' route
@app.route('/')
def index():
    # render the login page
    return render_template('login.html')


# define the '/register' route
@app.route('/register')
def register():
    # render the registration page
    return render_template('register.html')


# define the '/perform_registration' route
@app.route('/perform_registration', methods=['POST'])
def perform_registration():
    # get the form data
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    # insert the user into the database
    response = db.insert(name, email, password)

    # check if the insert was successful
    if response:
        # render the login page with a registration success message
        return render_template('login.html', register_success=True)
    # render the registration page with a registration failure message
    return render_template('register.html', register_failed=True)


# define the '/perform_login' route
@app.route('/perform_login', methods=['POST'])
def perform_login():
    # get the form data
    email = request.form.get('email')
    password = request.form.get('password')

    # fetch the user from the database
    response = db.fetch(email, password)

    # check if the fetch was successful
    if response[0]:
        # set the session variable
        session['logged_in'] = True
        session['response_value'] = response[1]
        # redirect to the profile page
        return redirect('/profile')
    # render the login page with a login failure message
    return render_template('login.html', login_failed=True)


# define the '/profile' route
@app.route('/profile')
def profile():
    # check if the user is logged in
    if session.get('logged_in'):
        # get the user's name from the session variable
        name = session.get('response_value')
        # render the profile page with the user's first name
        return render_template('profile.html', name=name.split()[0])
    # redirect to the login page
    return redirect('/')


# define the '/sentiment_analysis' route
@app.route('/sentiment_analysis')
def sentiment_analysis():
    # check if the user is logged in
    if session.get('logged_in'):
        # render the named entity recognition page
        return render_template('sentiment.html')
    # redirect to the login page
    return redirect('/')


# define the '/sentiment-analysis' route
@app.route('/perform-sentiment-analysis', methods=['POST'])
def perform_sentiment_analysis():
    # get the form data
    text = request.form.get('text')
    # perform named sentiment analysis using the API
    response = api.sentiment_analysis(text)
    round_function = round
    # check if the user is logged in
    if session.get('logged_in'):
        # render the named sentiment analysis page with the API response and input text
        return render_template('sentiment.html', response=response, text=text, round_function=round)
    # redirect to the login page
    return redirect('/')


# define the 'abuse-detection' route
@app.route('/abuse-detection')
def abuse_detection():
    if session.get('logged_in'):
        return render_template('abuse.html')
    return redirect('/')


# define the '/perform_abuse_detection' route
@app.route('/perform-abuse-detection', methods=['POST'])
def perform_abuse_detection():
    # get the form data
    text = request.form.get('text')
    # perform named abuse detection using the API
    response = api.abuse_detection(text)
    round_function = round
    if session.get('logged_in'):
        # render the named abuse page with the API response and input text
        return render_template('abuse.html', response=response, text=text, round_function=round)
    # redirect to the login page
    return redirect('/')


# define the 'ner' route
@app.route('/ner')
def ner():
    if session.get('logged_in'):
        return render_template('ner.html')
    return redirect('/')


# define the '/perform_ner' route
@app.route('/perform-ner', methods=['POST'])
def perform_ner():
    # get the form data
    text = request.form.get('text')
    # perform named entity recognition using the API
    response = api.ner_analysis(text)
    round_function = round
    if session.get('logged_in'):
        # render the named ner page with the API response and input text
        return render_template('ner.html', response=response, text=text, round_function=round)
    # redirect to the login page
    return redirect('/')


# define the 'emotion-detection' route
@app.route('/emotion-detection')
def emotion_detection():
    if session.get('logged_in'):
        return render_template('emotion.html')
    return redirect('/')


# define the '/perform-emotion-detection' route
@app.route('/perform-emotion-detection', methods=['POST'])
def perform_emotion_detection():
    # get the form data
    text = request.form.get('text')
    # perform named emotion detection using the API
    response = api.emotion_prediction(text)
    round_function = round
    if session.get('logged_in'):
        # render the named emotion detection page with the API response and input text
        return render_template('emotion.html', response=response, text=text, round_function=round)
    # redirect to the login page
    return redirect('/')


# define the 'keyword-detection' route
@app.route('/keyword-detection')
def keyword_detection():
    if session.get('logged_in'):
        return render_template('keyword.html')
    return redirect('/')


# define the '/perform-keyword-detection' route
@app.route('/perform-keyword-detection', methods=['POST'])
def perform_keyword_detection():
    # get the form data
    text = request.form.get('text')
    # perform named keyword recognition using the API
    response = api.keyword_detection(text)
    round_function = round
    if session.get('logged_in'):
        # render the named keyword detection page with the API response and input text
        return render_template('keyword.html', response=response, text=text, round_function=round)
    # redirect to the login page
    return redirect('/')


# define the 404 error handler
@app.errorhandler(404)
def page_not_found(error):
    # render the 404 page
    return render_template('404.html'), 404


# run the Flask app if the script is run
if __name__ == '__main__':
    app.run(debug=True)
