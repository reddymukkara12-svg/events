from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

# Page for form
@app.route('/quote')
def quote():
    return render_template("quote.html")

# Handle form data
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    budget = request.form['budget']
    return f"Hello {name}, your budget is {budget}"
@app.route('/show/<int:id>')
def show(id):
    return render_template("show.html", id=id)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)