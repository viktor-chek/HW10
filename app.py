from flask import Flask

from utils import load_json

candidates = "candidates.json"
data = load_json(candidates)

app = Flask(__name__)


@app.route("/")
def page_index():
    result = ""
    for i in data:
        name = i["name"]
        result += "Имя кандидата - " + name + "\n"
        position = i["position"]
        result += "Позиция кандидата: " + position + "\n"
        skills = i["skills"]
        result += "Навыки через запятую: " + skills + "\n" + "\n"
    return f"<pre>{result}<pre>"


@app.route("/candidate/<int:x>")
def user_profile(x):
    picture = ""
    result = ""
    for i in data:
        if i["id"] == x:
            picture += i["picture"]
            result += "Имя кандидата - " + i["name"] + "\n" + \
                      "Позиция кандидата: " + i["position"] + "\n" + "Навыки через запятую: " + i["skills"]
    return f'<img src="{picture}"> <pre>{result}<pre>'


@app.route("/skills/<x>")
def user_skills(x):
    x = x.lower()
    result = ""
    for i in data:
        if x in i["skills"].lower().split(", "):
            name = i["name"]
            result += "Имя кандидата - " + name + "\n"
            position = i["position"]
            result += "Позиция кандидата: " + position + "\n"
            skills = i["skills"]
            result += "Навыки через запятую: " + skills + "\n" + "\n"
    return f"<pre>{result}<pre>"


app.run(host='127.0.0.1', port=8000)
