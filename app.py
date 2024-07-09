from flask import Flask, render_template, request
from db import Database
from  translate1 import TranslateTo
from sentimentanalysis import SentimentAnalysis

app = Flask(__name__)
dbo = Database()
trans_obj = TranslateTo()
sa_obj = SentimentAnalysis()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/perform_login', methods=['post'])
def perform_login():
    email = request.form.get('Email')
    password = request.form.get('Password')

    response = dbo.search(email,password)
    print(response)

    if response :
        return render_template('profile.html')
    else :
        return render_template('login.html', message = 'Invalid User Details. Try Again')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration',methods=['post'])
def perform_registration():
    name = request.form.get('Name')
    email = request.form.get('Email')
    password = request.form.get('Password')

    response = dbo.insert(name, email, password)

    if response == 0 :
        return render_template('login.html', message='Registered Successfully. Login to proceed')
    else:
        return render_template('register.html', message='User Already Exists')

@app.route('/translate')
def translate():
    return render_template('translation_gui.html')


@app.route('/perform_translation', methods=['post'])
def perform_translation():
    txt = request.form.get('txt')
    to_lang = request.form.get('ToLang')
    trans_obj = TranslateTo()
    response = trans_obj.translate_to(txt,to_lang)
    return response

@app.route('/sentiment_analysis')
def sentiment_analysis():
    return render_template('sentiment_analysis_gui.html')

@app.route('/perform_sentiment_analysis', methods=['post'])
def perform_sentiment_analysis():
    txt = request.form.get('txt')
    response = sa_obj.sentiment_analysis(txt)
    return response

app.run(debug=True)



