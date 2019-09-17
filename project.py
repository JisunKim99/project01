from flask import Flask, escape, request, render_template
from account import account_info

app = Flask(__name__)


@app.route('/bank/')
@app.route('/bank/<name>')
def home(name=None):

    if name == None:
        bank_details = account_info()
        return render_template(
            'home.html',
            bank_details=bank_details
            )

    else:
        bank_details = account_info()
        one_person = bank_details[name]
        amount = one_person['amount']
        bank_name= one_person['bank_name']


        return render_template(
            'one_person.html',
            amount = amount,
            bank_name = bank_name,
            person_name = name
            )


