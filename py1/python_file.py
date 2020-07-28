# public libraries
from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    return ("'Hello World' %s" % datetime.now()), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("80"), debug=True)
