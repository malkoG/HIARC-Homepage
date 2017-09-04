from flask import Flask, render_template, request

app = Flask(__name__)


class Student:
    def __init__(self, apply_form):
        self.name    = apply_form['name']
        self.faculty = apply_form['faculty']
        self.phone = apply_form['phone']
        self.email   = apply_form['email']
        self.portfolio = apply_form['portfolio']
        self.comment = apply_form['comment']


@app.route('/apply', methods=['GET', 'POST'])
def apply_page():
    if request.method == 'POST':
        
    return render_template('apply.html')

@app.route('/admin/applies')
def applier_page():
    return render_template('appliers_page.html')

if __name__ == '__main__':
    app.run()
