from flask import Flask, escape, request, render_template
from account import account_info

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route('/bank/')
@app.route('/bank/<name>')
def bank(name=None):

    if name == None:
        bank_details = account_info()
        return render_template(
            'bank.html',
            bank_details=bank_details
            )

    else:
        bank_details = account_info()
        return render_template(
            'one_person.html',
            bank_details=bank_details,
            name=name
            )


if __name__ == '__main__':
    app.run(debug=True)
