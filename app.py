from flask import render_template, Flask, flash, request, jsonify, redirect
from forms import TranslateForm  # You need to import the TranslateForm if it exists
from googletrans import Translator
from deep_translator import GoogleTranslator
from flask_cors import cross_origin
from models.speech import  text_to_speech
from gtts import gTTS
import os

app = Flask(__name__)
app.secret_key = 'YOUR_SECRET_KEY'  # Set your own secret key

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

