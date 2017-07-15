from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)


@app.route('/')
def hello_world():
	# return "hello world"
	return render_template('index.html')

@app.route('/success')
def success():
	return render template("success.html")	


@app.route('/survey', methods=['POST'])
def survey():
	print request.form['name']
	session['survey_info'] = request.form
	return redirect('/success')




app.run(debug=True)	