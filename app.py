from flask import Flask, render_template
import random
import json

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/<name>")
def user(name):
	with open('users.txt') as json_file:
		users = json.load(json_file)
	if name not in users:
		users[name] = sorted(random.sample(range(1, 75), k=27))
		for i in range(0, 3):
			empties = sorted(random.sample(range(0, 9), k=3))
			for empt in empties:
				users[name][3 * empt + i] = 0
		with open('users.txt', 'w') as json_file:
			json.dump(users, json_file)

	return render_template("card.html", name=name, numbers=users[name])

@app.route("/leaderboard")
def leaderboard():
	return render_template("leaderboard.html")

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)
