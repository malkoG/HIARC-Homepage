from flask import Flask, render_template, request, flash

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
        apply_form = request.form
        Student(apply_form)
        flash(apply_form['name'] + "님, 지원해주셔서 감사합니다! Slack 초대장을 확인되는대로 빠른 시일내에 이메일로 발송할 예정이니 참고바랍니다!")
    return render_template('apply.html')

@app.route('/admin/applies')
def applier_page():
    return render_template('appliers_page.html')

if __name__ == '__main__':
    app.run()
