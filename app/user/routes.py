from app import user
from flask import render_template, request, redirect, url_for, Blueprint
from .forms import UserCreationForm, LoginForm, EditProfileForm
from .models import User
from flask_login import login_user, logout_user, current_user, login_required


user = Blueprint('user', __name__, template_folder='user_templates')


@user.route("/signup", methods=["GET", "POST"])
def signUpPage():
    form = UserCreationForm()
    if request.method == "POST":
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data

            user = User(username, email, password)
            print(user)

            user.saveToDB()

            return redirect(url_for('user.loginPage'))

    return render_template("signup.html", form = form)

@user.route("/login", methods=["GET", "POST"])
def loginPage():
    login = LoginForm()

    if request.method == "POST":
        if login.validate():
            username = login.username.data
            password = login.password.data

            user = User.query.filter_by(username = username).first()
            if user:
                if user.password == password:
                    login_user(user)

                else:

                    print(("wrong password"))

            else:
                print("user does not exist")

    return render_template("login.html", login = login) 

@user.route("/logout", methods=["GET"])
@login_required
def logoutRoute():
    logout_user()

    return redirect(url_for('user.loginPage'))

@user.route("/profile", methods=["GET", "POST"])
def profile():
    form = EditProfileForm()
    user = User.query.filter_by(id = current_user.id).first()
    return render_template("profile.html", form = form, current_user = current_user)

@user.route("/editprofile", methods=["GET", "POST"])
@login_required
def editProfileForm():
    form = EditProfileForm()
    user = User.query.filter_by(id = current_user.id).first()
    if request.method == "POST":
        username = form.username.data
        email = form.email.data
        password = form.password.data
        if username != "":
            user.username = username
        if email != "":
            user.email = email
        if password != "":
            user.password = password
        user.saveChanges()
        return render_template('editdelete.html', form = form, current_user = current_user )
    return render_template('editdelete.html', form = form, current_user = current_user )

@user.route("/profile/editdelete", methods=["GET", "POST"])
@login_required
def delProfile():
    user = User.query.filter_by(id = current_user.id).first()
    if request.method == "POST":
        if user:
            user.deleteFromDB()
            return redirect(url_for("user.loginPage"))
    return render_template("editdelete.html") 
