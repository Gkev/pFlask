from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
	# return "hello world"
	return render_template('index.html', name="Kev")

# @app.route('/success')
# def success():
# 	return "success"	


app.run(debug=True)	