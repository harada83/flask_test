from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, PasswordField, SubmitField, FileField, ValidationError
from wtforms.fields.choices import SelectField
from wtforms.fields.simple import BooleanField
from wtforms.validators import DataRequired, Length, EqualTo

from .models.user import User


class RegistrationForm(FlaskForm):
    name = StringField('ФИО', validators=[DataRequired(), Length(min=2, max=200)])
    login = StringField('Логин', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=4, max=100)])
    confirm_password = PasswordField('Подтвердите пароль', validators=[DataRequired(), EqualTo('password')])
    avatar = FileField('Загрузите своё фото', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Зарегистрироваться')

    def validate_login(self, login):
        user = User.query.filter_by(login=login.data).first()
        if user:
            raise ValidationError('This login is unawalable!, Enter another.')


class LoginForm(FlaskForm):
    """Form for log in users"""
    login = StringField('Логин', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=4, max=100)])
    remember = BooleanField("Запомнить меня")
    submit = SubmitField('Войти')


class StudentForm(FlaskForm):
    student = SelectField('student', choices=[], render_kw={'class': 'form-control'})

class TeacherForm(FlaskForm):
    teacher = SelectField('teacher', choices=[], render_kw={'class': 'form-control'})