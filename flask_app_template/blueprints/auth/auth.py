from flask import Blueprint, render_template

auth_bp = Blueprint('auth_bp', __name__,
                    template_folder='templates')


@auth_bp.route('/sing_up', methods=['GET', 'POST'])
def sing_up():
    return render_template('singup.html')


@auth_bp.route('/login_page', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@auth_bp.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    return render_template('forgot_password.html')
