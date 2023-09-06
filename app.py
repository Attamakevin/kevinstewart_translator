from flask import render_template, Flask, flash, request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from forms import TranslateForm, RegistrationForm, LoginForm 
from googletrans import Translator  # Corrected the import statement
SECRET_KEY = 'URSECRET'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'URSECRET'  # Set your app's secret key
# Configure your SQLAlchemy database URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'  # database name is user.db///
db = SQLAlchemy(app)

# Define your User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
@app.route('/initialize_db')
def initialize_db():
    db.create_all()
    return 'Database initialized!'
@app.route('/', methods=['GET'])
def homepage():
    return render_template('home.html')



@app.route('/translate', methods=['GET', 'POST'])  # Added 'POST' to the methods
def translate():  # Renamed the function to lowercase
    #return render_template('index.html')

    #form = TranslateForm()
    #if form.validate_on_submit():
    #flash('Translation requested. Please wait.') # Fixed the flash message
    if request.method == 'POST':
        try:
            text_to_translate = request.form["text-to-translate"].lower()
            selected_language = request.form["select-language"]
            translated_text = translator.translate(
                text_to_translate, dest=selected_language)
            text = translated_text.text
            pronunciation_data = translated_text.pronunciation
            if pronunciation_data is None:
                pronunciation_data = "Sorry, data not available"
            confidence = round((translated_text.extra_data["confidence"]) * 100, 2)
        except Exception as e:
            pronunciation_data = "-"
            text = "ERROR: We are not able to handle your request right now"
            confidence = "-"
        return render_template('index.html', translation_result=text, pronunciation=pronunciation_data, confidence_level=str(confidence) + " %")
    return render_template('index.html')

# Add a route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Check if the email already exists
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('Email already registered. Please use a different email.', 'danger')
        else:
            # Create a new user and add it to the database
            new_user = User(email=form.email.data)
            db.session.add(new_user)
            db.session.commit()
            flash('Your account has been created! You can now log in.', 'success')
            return redirect(url_for('login'))
    return render_template('register.html', form=form)

# Add a route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Check if the user exists in the database
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            # Authenticate the user (you can use Flask-Login for more advanced authentication)
            flash('Login successful!', 'success')
            return redirect(url_for('translate'))
        else:
            flash('Login failed. Please check your email and password.', 'danger')
    return render_template('login.html', form=form)

