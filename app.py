from flask import render_template, Flask, flash, request
from forms import TranslateForm
from googletrans import Translator  # Corrected the import statement
SECRET_KEY = 'URSECRET'
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])  # Added 'POST' to the methods
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
