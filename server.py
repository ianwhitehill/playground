from flask import Flask, render_template 

app = Flask(__name__)
@app.route('/')
def home():
    return 'Would you like ot play a game'

@app.route('/play/<int:times>/<color>')
def index(times, color):
    return render_template("index.html", times = times, color = color)
if __name__ == "__main__":
    app.run(debug=True)