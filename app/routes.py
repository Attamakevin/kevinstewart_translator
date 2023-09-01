from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import TranslateForm
from app import translate_text  # Import the function from app module

@app.route('/', methods=['GET', 'POST'])
def home():
    form = TranslateForm()  # Create an instance of the TranslateForm
    message = None

    if form.validate_on_submit():
        text = form.Translate_text.data
        target_language = form.target_language.data
        result = translate_text(text, target_language)
        
        if result['success']:
            flash('Translation successful.')
            message = f"Translation: {result['result']}"
        else:
            flash('Translation failed. Please try again later.')

    return render_template('index.html', title='Translate', form=form, message=message)
