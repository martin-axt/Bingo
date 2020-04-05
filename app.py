from flask import Flask, render_template
import random

app = Flask(__name__)
users = {}

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/<name>")
def  user(name):
	if name not in users:
		users[name] = sorted(random.sample(range(1, 90), k=27))
		empties = random.sample(range(0, 27), k=12)
		for empt in empties:
			users[name][empt] = 0
	return render_template("card.html", name=name, numbers=users[name])

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)
