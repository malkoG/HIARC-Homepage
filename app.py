from flask import Flask 
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/a')
def dddd():
    return render_template('a.html')

@app.route('/b')
def eeee():
    return render_template('b.html')

if __name__ == '__main__':
    app.run()
