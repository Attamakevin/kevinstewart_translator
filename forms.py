from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class TranslateForm(FlaskForm):
    Translate_text = StringField('translate_text', validators=[DataRequired()])
    target_language = StringField('target_language', validators=[DataRequired()])
    submit = SubmitField('Translate')
