from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Flask backend is running"
    })

@app.route("/user", methods=["POST", "GET"])
def submit_user():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "message": "A valid JSON request is required"
        }), 400

    name = data.get("name")
    age = data.get("age")
    email = data.get("email")

    if not isinstance(name, str) or not name.strip():
        return jsonify({
            "message": "Name is required"
        }), 400

    if len(name.strip()) > 100:
        return jsonify({
            "message": "Name must be 100 characters or fewer"
        }), 400

    if (
        isinstance(age, bool)
        or not isinstance(age, int)
        or not 1 <= age <= 120
    ):
        return jsonify({
            "message": "Age must be between 1 and 120"
        }), 400

    if (
        not isinstance(email, str)
        or len(email) > 254
        or not re.fullmatch(
            r"[^@\s]+@[^@\s]+\.[^@\s]+",
            email.strip()
        )
    ):
        return jsonify({
            "message": "Enter a valid email address"
        }), 400

    user = {
        "name": name.strip(),
        "age": age,
        "email": email.strip()
    }

    app.logger.info("Processed submission for %s", user["name"])

    return jsonify({
        "message": "Form submitted successfully by Flask!",
        "user": user
    }), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)