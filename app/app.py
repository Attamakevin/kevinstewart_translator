from flask import Flask, request, render_template, jsonify
from googletrans import Translator

app = Flask(__name__)

TRANSLATOR = Translator()

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    text = request.form.get('text')
    result = translate_text(text)
    return jsonify(result)

@app.route('/translate', methods=['POST'])
def translate():
    text = request.form.get('text')
    target = request.form.get('target')
    result = translate_text(text, target)
    return jsonify(result)

def translate_text(text, target_language=None):
    try:
        if target_language:
            translated = TRANSLATOR.translate(text, dest=target_language)
        else:
            translated = TRANSLATOR.detect(text)
        return {'success': True, 'result': translated.text}
    except Exception as e:
        return {'success': False, 'error_message': str(e)}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=30000)
