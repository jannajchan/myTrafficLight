import os
from flask import Flask, render_template, request

# === 1. Configuration ===
app = Flask(__name__, template_folder="templates", static_folder="static")

HOME_FORM = "home.html"
TRAFFIC_LIGHT_FORM = "traffic-light.html"


# Route 1: Home --------------------------------------------------------------------------------------------------------
@app.route("/")
def home():
    return render_template(HOME_FORM)


# Route 2: My Traffic Light --------------------------------------------------------------------------------------------
@app.route("/traffic-light")
def traffic_light():
    return render_template(TRAFFIC_LIGHT_FORM)

"""
Setting debug=True tells Flask to:
    - Auto-reload on any file change (HTML, CSS, Python)
    - Show helpful error messages
"""
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
