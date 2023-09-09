from flask import render_template, Flask, flash, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import InputRequired, Email, Length
from google.oauth2 import id_token
from google.auth.transport import requests

from forms import TranslateForm, RegistrationForm, LoginForm
from googletrans import Translator
from deep_translator import GoogleTranslator
from flask_cors import cross_origin
from models.speech import  text_to_speech
from gtts import gTTS
import os


app = Flask(__name__)
app.secret_key = os.urandom(12)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def translate():
    translated_text = ""
    #src_lang=""
    #target_lang=""

    if request.method == 'POST':
        try:
            text_to_translate = request.form.get("text-to-translate").lower()
            selected_language = request.form.get("select-language")

            # Initialize the translator
            my_translator = GoogleTranslator(source='auto', target= selected_language)

            # Translate text
            result = my_translator.translate(text=text_to_translate)

            # Access the translated text
            translated_text = result
        
            #src_lang=result.src
            # target_lang=result.target
        except Exception as e:
            print(e)
            translated_text = "ERROR: We are not able to handle your request right now"

    return render_template('index.html', translated_text=translated_text)

@app.route('/voice', methods=['POST'])
@cross_origin()
def homepage():
    if request.method == 'POST':

        text = ""
        text = request.form["translation-result"]
        gender = request.form['voices']
        print(text)
        # Call your text_to_speech function here
        text_to_speech(text,gender)
            
        # Redirect to the main page or render it with a success message
        flash("Text converted to speech successfully!", 'success')
        return redirect('/')
    else:
        print(gender)
        print(e)
        flash("Error converting text to speech", 'error')
    
    # Render the template with the translated text if needed
    return render_template('index.html', text=text)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)  # For registration route
 


    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        # Check if the user with this email already exists in the database
        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash('Email address already registered. Please log in.')
            return redirect(url_for('login'))

        # If the email is not in use, create a new user
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! You can now log in.')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        # Check if the provided email and password match a user in the database
        user = User.query.filter_by(email=email, password=password).first()

        if user:
            flash('Login successful! Welcome back.')
            return redirect(url_for('dashboard'))

        flash('Invalid email or password. Please try again.')

    return render_template('login.html', form=form)
@app.route('/google-login', methods=['POST'])
def google_login():
    try:
        # Receive the ID token from the client
        id_token_received = request.json.get('idToken')

        # Verify the ID token with Google's servers
        id_info = id_token.verify_oauth2_token(id_token_received, requests.Request(), '160112374519-a963oshs8nfjk0ilecet0d42l8kubgig.apps.googleusercontent.com')

        # Extract user information from id_info
        user_email = id_info['email']
        # You can also extract other user information such as name, profile picture, etc. from id_info

        # Perform user registration or login based on the user_email
        # ...

        # Return a success response to the client
        return jsonify({'message': 'Login successful'})

    except ValueError as e:
        # Handle verification failure
        return jsonify({'error': 'Invalid ID token'})

#


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
