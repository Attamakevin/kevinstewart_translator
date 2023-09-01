from flask import render_template
from app import app
from app.forms import TranslateForm
from googletrans import translator


# ...

@app.route('/translate')
def Translate():
    form = TranslateForm()
    if form.validate_on_submit():
        flash('Translation requested please wait')
        translator = Translator()
        translated=translator.translate(“translated_text”,dest=’target_language’)
        return redirect('/index.html')
    return render_template('index.html', title='Translate', form=form)
