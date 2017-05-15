from flask import Flask
from flask import redirect
from flask import abort
from flask_script import Manager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name
@app.route('/website/<website>')
def website(website):
	return redirect('http://www.%s.com'% website)
@app.route('/user/<id>')
def get_uset(id):
	user=load_user(id)
	if not user:
		abort(404)
	return '<h1>Hello</h1>'
if __name__ == '__main__':
    app.run(debug=True)
