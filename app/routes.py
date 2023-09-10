from flask import render_template, flash, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo,ValidationError
from google.oauth2 import id_token
from google.auth.transport import requests
from flask_login import current_user, login_user
from app.model import User
from app import app
#from app.forms import TranslateForm, RegistrationForm, LoginForm
from googletrans import Translator
from deep_translator import GoogleTranslator
from flask_cors import cross_origin
from models.speech import  text_to_speech
from gtts import gTTS
from app import db
import os

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


#app = Flask(__name__)
app.secret_key = os.urandom(12)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
#db = SQLAlchemy(app)


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
    if current_user.is_authenticated:
        return redirect('/login')
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user, please login to continue!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/login')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect('/')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/google-login', methods=['POST'])
def googlelogin():
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
 #   db.create_all()
    app.run(debug=True)
