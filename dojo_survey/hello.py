from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "what time is it?"


@app.route('/')
def hello_world():
	# return "hello world"
	return render_template('index.html')



@app.route('/survey', methods=['POST'])
def survey():
	print request.form['name']
	session['name'] = request.form
	return redirect('/success')



@app.route('/success')
def success():
	render_template('success.html')	


app.run(debug=True)	