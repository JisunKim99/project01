from flask import Flask, escape, request, render_template
from account import account_info

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == "POST":
        return "you called the post method"
    else:
        details = account_info()
        return 'The balance is  and the bank is {details[1]}'

@app.route('/account_info/<name>')
def get_account(name):
    details = account_info()
    return f"The balance for {name} is {details[name]['amount']} and the bank is {details[name]['bank_name']}"


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

    from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def home(name=None):
    return render_template('home.html')


