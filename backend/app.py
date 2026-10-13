from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Temporary storage: keeps the latest submission in memory
latest_user = None


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Flask backend is running"})


@app.route("/user", methods=["GET", "POST"])
def user_route():
    global latest_user

    # Display the latest submitted data in the browser
    if request.method == "GET":
        if latest_user is None:
            return jsonify({
                "message": "No user data submitted yet"
            }), 404

        return jsonify({
            "message": "User data retrieved successfully",
            "user": latest_user
        }), 200

    # Receive data from the frontend
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "message": "A valid JSON request is required"
        }), 400

    name = data.get("name")
    age = data.get("age")
    email = data.get("email")

    if not isinstance(name, str) or not name.strip():
        return jsonify({"message": "Name is required"}), 400

    if (
        isinstance(age, bool)
        or not isinstance(age, int)
        or not 1 <= age <= 120
    ):
        return jsonify({"message": "Invalid age"}), 400

    if (
        not isinstance(email, str)
        or not re.fullmatch(
            r"[^@\s]+@[^@\s]+\.[^@\s]+",
            email.strip()
        )
    ):
        return jsonify({"message": "Invalid email"}), 400

    latest_user = {
        "name": name.strip(),
        "age": age,
        "email": email.strip()
    }

    print("Received user data:", latest_user, flush=True)

    return jsonify({
        "message": "Form submitted successfully by Flask!",
        "user": latest_user
    }), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)