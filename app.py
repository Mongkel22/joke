from flask import Flask, render_template
import pyjokes

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/get_joke")
def get_joke():
    joke = pyjokes.get_joke()
    return joke

if __name__ == "__main__":
    app.run(debug=True)

