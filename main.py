from flask import Flask, render_template, jsonify
from users import USERS

app = Flask(__name__)

@app.route ("/")
def main ():
    return render_template("index.html")

@app.route ("/api/health")
def health():
    return jsonify(
        {"status": "ok"}
    )

@app.route ("/user/<string:name>")
def security (name):
    for user in USERS:
        if  user['username'] ==name:
            score = 0
            score += password_length(user)
            score += password_last_changed_days(user)
            score += mfa_enabled(user)
            score += breach_flag(user)

            if score == 100:
                is_compliant = True
            else:
                is_compliant = False

            return render_template("sec_aud.html", user=user, score=score, is_compliant=is_compliant)

    return render_template("not_found.html", name=name), 404



def password_length (user):
    if user["password_length"] >= 12:
        return 20
    return 0

def password_last_changed_days (user):
    if user["password_last_changed_days"] <= 180:
        return 20
    return 0

def mfa_enabled (user):
    if user["mfa_enabled"] == True:
        return 30
    return 0

def breach_flag (user):
    if user["breach_flag"] == False:
        return 30
    return 0
@app.route ("/api/user/<string:name>")
def make_api (name):
    for user in USERS:
        if user['username'] == name:
            score = 0
            score += password_length(user)
            score += password_last_changed_days(user)
            score += mfa_enabled(user)
            score += breach_flag(user)

            is_compliant = score == 100

            return jsonify({
                "user":user,
                "result": {
                    "score":score,
                    "is_compliant": is_compliant
                }
            })
    return jsonify({
        "error": "User not found",
        "name": name
    }), 404

