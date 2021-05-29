from flask import Flask
from flask.templating import render_template

app = Flask(__name__)


@app.route('/home')
def home():
    #return "<h1>hello</h1>"
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)