from flask import Flask, render_template
import random

app = Flask(__name__)
users = {}

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/<name>")
def user(name):
	if name not in users:
		users[name] = sorted(random.sample(range(1, 90), k=27))
		for i in range(0, 3):
			empties = sorted(random.sample(range(0, 9), k=4))
			for empt in empties:
				try:
					users[name][3 * empt + i] = 0
				except:
					print("STOP")
	return render_template("card.html", name=name, numbers=users[name])

@app.route("/leaderboard")
def leaderboard():
	return render_template("leaderboard.html")

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)
