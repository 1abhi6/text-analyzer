from flask import Flask, render_template,request
from database import Database


app = Flask(__name__)
db = Database()



@app.route('/')
def index():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/perform_registration',methods=['POST'])
def perform_registration():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    
    response = db.insert(name,email,password)
    
    if response:
        return "Bhai tu login hogya"
    return 'Abey tera email already register h login kr'

@app.route('/perform_login',methods=['POST'])
def perform_login():
    email = request.form.get('email')
    password = request.form.get('password')


    response = db.fetch(email,password)
    
    if response:
        return 'Beta tu login hogya'
    return render_template('register.html')

app.run(debug=True)
