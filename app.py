import os
import openai
from flask import Flask, render_template, request

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

questions = {
    "Actor": [
        "Biography",
        "Childhood",
        "Education",
        "Personal Life",
        "Family",
        "Films",
        "Awards",
        "Social Media links"
    ],
    "Politician": [
        "Biography",
        "Childhood",
        "Education",
        "Personal Life",
        "Family",
        "Political Party Details",
        "Awards or Notable Works",
        "Social Media links"
    ],
    "Singer": [
        "Biography",
        "Childhood",
        "Education",
        "Personal Life",
        "Family",
        "Songs",
        "Awards",
        "Social Media links"
    ],
    "Player": [
        "Biography",
        "Childhood",
        "Education",
        "Personal Life",
        "Family",
        "Sports Career",
        "Awards or Notable Works",
        "Social Media links"
    ]
}


@app.route("/", methods=("GET", "POST"))
def index():
    results = []
    if request.method == "POST":
        name = request.form["name"]
        profession = request.form["profession"]
        for question in questions[profession]:
            heading = profession + ' ' + name + ' ' + question
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=heading,
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            results.append((question, response.choices[0].text))
    return render_template("index.html", results=results)
