from flask import Flask 
from flask import render_template


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/a')
def example1():
    return render_template('a.html')

@app.route('/b')
def example2():
    return render_template('b.html')

@app.route('/c')
def example3():
    return render_template('c.html')




if __name__ == '__main__':
    app.run()
