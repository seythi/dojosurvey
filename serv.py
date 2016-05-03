from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route("/")
def renderfoo():
	return render_template("start.html")
@app.route("/user", methods = ["post"])
def handle():
	print("user")
	name = request.form['name']
	location = request.form['location']
	language = request.form['language']
	comment = request.form['comment']
	# return redirect("/out")
	return render_template("out.html", name = name, location = location, language = language, comment = comment)
# @app.route("/out")
# def out(name, location, language, comment):
# 	return render_template("out.html", name = name, location = location, language = language, comment = comment)
app.run(debug=True)