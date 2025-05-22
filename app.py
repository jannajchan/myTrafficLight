import os
from flask import Flask, render_template, request, jsonify, session

# === Configuration ===
app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = os.environ.get("SECRET_KEY", "mydefaultsecretkey")

HOME_FORM = "home.html"
TRAFFIC_LIGHT_FORM = "traffic-light.html"

# Initialize counters if not present
def init_counters():
    if "counter" not in session:
        session["counter"] = {"stop": 0, "slow": 0, "go": 0}


# Route 1: Home --------------------------------------------------------------------------------------------------------
@app.route("/")
def home():
    return render_template(HOME_FORM)


# Route 2: My Traffic Light --------------------------------------------------------------------------------------------
@app.route("/traffic-light")
def traffic_light():
    init_counters()
    return render_template(TRAFFIC_LIGHT_FORM, counter=session["counter"])

@app.route('/update-light', methods=['POST'])
def update_light():
    data = request.get_json()
    color = data.get("color")

    init_counters()
    if color in session["counter"]:
        session["counter"][color] += 1
        session.modified = True

    print(f"Button pressed: {color} -> New Count: {session['counter'][color]}")
    return jsonify(session["counter"])
"""
Setting debug=True tells Flask to:
    - Auto-reload on any file change (HTML, CSS, Python)
    - Show helpful error messages
"""
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
