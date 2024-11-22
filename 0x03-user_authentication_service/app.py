#!/usr/bin/env python3
"""
Flask app to handle user authentication
"""

from flask import Flask, jsonify, request, abort, make_response
from auth import Auth

AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"])
def welcome():
    """GET route for the homepage."""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def register_user():
    """POST route for user registration."""
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        abort(400, "Email and password required")

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"])
def login():
    """POST route for user login."""
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        abort(401, "Invalid credentials")

    if not AUTH.valid_login(email, password):
        abort(401, "Invalid credentials")

    session_id = AUTH.create_session(email)
    if not session_id:
        abort(401, "Invalid credentials")

    response = make_response(
        jsonify({"email": email, "message": "logged in"}), 200
    )
    response.set_cookie("session_id", session_id)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
