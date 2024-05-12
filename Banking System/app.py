from flask import Flask, render_template, request
import random

app = Flask(__name__)

balance = random.randint(10000, 99999)

@app.route('/')
def index():
    return render_template('index.html', balance=balance)

@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    global balance
    if request.method == 'POST':
        amount = float(request.form['amount'])
        if amount < 0:
            return render_template('deposit.html', balance=balance, message="Please enter a valid amount.")
        balance += amount
        return render_template('deposit.html', balance=balance, message="Deposit successful.")
    return render_template('deposit.html', balance=balance)

@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    global balance
    if request.method == 'POST':
        amount = float(request.form['amount'])
        if balance >= amount:
            balance -= amount
            return render_template('withdraw.html', balance=balance, message="Withdrawal successful.")
        else:
            return render_template('withdraw.html', balance=balance, message="Insufficient funds.")
    return render_template('withdraw.html', balance=balance)

@app.route('/balance')
def view_balance():
    return render_template('balance.html', balance=balance)

@app.route('/exit')
def exit():
    return render_template('exit.html')

if __name__ == '__main__':
    app.run(debug=True)