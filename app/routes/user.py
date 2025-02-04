from flask import Blueprint, render_template, redirect, flash, url_for, request
from flask_login import login_user, logout_user
from ..functions import save_picture
from ..forms import RegistrationForm, LoginForm
from ..extensions import db, bcrypt
from ..models.user import User


user = Blueprint('user', __name__)


@user.route('/user/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        avatar_filename = save_picture(form.avatar.data)
        user = User(
            name=form.name.data,
            login=form.login.data,
            avatar = avatar_filename,
            password = hashed_password
        )
        try:
            db.session.add(user)
            db.session.commit()
            flash(f'Conratulations! {user.name} registered!', 'Success!!!')
            return redirect(url_for('user.login'))
        except Exception as err:
            print(str(err))
            flash(f'При регистрации произошла ошибка!', 'danger')
    return render_template('user/register.html', form=form)

@user.route('/user/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(login=form.login.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('post.all'))
        else:
            flash('Ошибка входа! Пожалуйста проверьте Логин и Пароль.', 'danger')
    return render_template('user/login.html', form=form)

@user.route('/user/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('post.all'))
