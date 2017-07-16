from flask import Flask, render_template, request, redirect, session
from random import randint

app = Flask(__name__)
app.secret_key = "my_key"


@app.route('/')
def index():

	if "number" not in session:
		session['number'] = randint(1,100)
	print session['number'], "This is the number"
	return render_template('index.html')



@app.route('/survey', methods=['POST'])
def survey():
	print request.form['name']
	session['name'] = request.form
	return redirect('/success')


@app.route('/guess', methods=['POST'])
def guess_game():
	guess = int(request.form['guess'])
	print type(guess)
	if guess < session['number']:
		print "in low if"
		session['guess'] = "low"
	elif guess > session['number']:
		print "in high elif"
		session['guess'] = "high"
	else:
		print "in match"
		session['guess'] = "match"
	return redirect('/')


	



@app.route('/success')
def success():
	return render_template('success.html')	
	

app.run(debug=True)	