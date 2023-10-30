from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    frutas = ["maçã", "banana", "pera"]

    return frutas[1]


if __name__ == "__main__":
    app.run()
