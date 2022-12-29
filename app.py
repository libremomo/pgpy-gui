from flask import Flask, render_template, request
from helpers import call, load_key, pgpy_encrypt


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/encrypt", methods=["GET", "POST"])
def encrypt():
    if request.method == "POST":

        query = request.form.get("query")

        # Contact the OpenPGP server api
        apiResponse = call(query)
        if apiResponse == None:
            return "ERROR: Key was not found on the server!"

        # if response is valid, pass the key and message to the PGPy
        else:
            key = load_key(apiResponse)
            message = request.form.get("message")
            encryptedMessage = pgpy_encrypt(key, message)

            return str(encryptedMessage)

    else:
        return render_template("encrypt.html")