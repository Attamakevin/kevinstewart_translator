from flask import render_template, flash
from app import app
from app.forms import TranslateForm
from googletrans import Translator  # Corrected the import statement

@app.route('/translate', methods=['GET', 'POST'])  # Added 'POST' to the methods
def translate():  # Renamed the function to lowercase
    form = TranslateForm()
    if form.validate_on_submit():
        flash('Translation requested. Please wait.')  # Fixed the flash message
        translator_instance = Translator()  # Renamed the variable to avoid conflicts
        translated = translator_instance.translate(form.translated_text.data, dest=form.target_language.data)  # Fixed form attribute access
        return translated.text

    return render_template('index.html', title='Translate', form=form)

