#!/usr/bin/python3
"""
Script starts Flask web app
- listen on 0.0.0.0, port 5000
- routes:
  /: display “Hello HBNB!”
  /hbnb: display “HBNB”
  /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space)
  /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space)
  /number/<n>: display “n is a number” only if n is an integer
  /number_template/<n>: display a HTML page only if n is an integer:
     H1 tag: “Number: n” inside the tag BODY
  /number_odd_or_even/<n>: display a HTML page only if n is an integer:
     H1 tag: “Number: n is even|odd” inside the tag BODY
"""
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """display text"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """display text"""
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """display custom text given"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_text(text="is cool"):
    """display custom text given"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def text_if_int(n):
    """display text only if int given"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """display HTML page if n is an integer"""
    return render_template('6-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """display HTML page if n is an integer, stating if it's odd or even"""
    return render_template('6-number_odd_or_even.html', number=n, odd_even=('even' if n % 2 == 0 else 'odd'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

