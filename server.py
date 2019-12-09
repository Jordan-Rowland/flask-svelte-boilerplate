from random import randint

from flask import Flask, jsonify, send_from_directory


app = Flask(__name__)

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')


# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)


@app.route("/rand")
def rand():
    return jsonify(random_number=randint(0, 100))


@app.route("/posts")
def posts():
    return jsonify(
        posts=[
            {
                "username": "J-Sun",
                "message": "First message!"
            },
            {
                "username": "J-Sun",
                "message": "Second message!"
            },
            {
                "username": "J-Sun",
                "message": "Third message!"
            },
            {
                "username": "Dave Dawn",
                "message": "Nuggets!"
            },
        ]
    )


if __name__ == "__main__":
    app.run(debug=True)
