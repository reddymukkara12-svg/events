from flask import Flask, render_template, request

app = Flask(__name__)

# Home page
@app.route('/')
def index():
    return render_template("index.html")

# Quote form page
@app.route('/quote')
def quote():
    return render_template("quote.html")

# Form submit
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    budget = request.form.get('budget')
    return f"Hello {name}, your budget is {budget}"

# Show images page
@app.route('/show/<int:id>')
def show(id):
    return render_template("show.html", id=id)