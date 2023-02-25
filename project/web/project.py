from flask import Flask , render_template

Portfolio = Flask(__name__)

@Portfolio.route('/')
def homepage():
    return render_template('home.html',title='my website')


if __name__ == '__main__':
    Portfolio.run(debug=True, port=9000)
