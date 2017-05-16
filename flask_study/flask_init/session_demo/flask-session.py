from flask import Flask, request, session, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def head():
    return redirect(url_for('register'))

@app.route('/home', methods=['GET'])
def index():
    return 'hello world!'
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_name = request.form['user']
        session['user'] = user_name
        return 'hello, ' + session['user']
    elif request.method == 'GET':
        if 'user' in session:
            return redirect(url_for('index'))
        else:
            return render_template('login.html')

app.secret_key = '123456'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5632, debug=True)