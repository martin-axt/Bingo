from flask import Flask, render_template
import random

app = Flask(__name__)
users = {}

@app.route("/")
def home():
	return "Hola guapis!"

@app.route("/<name>")
def  user(name):
	if name not in users:
		users[name] = random.sample(range(1, 76), k=24)
	return render_template("home.html", name=name, numbers=users[name])

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)
