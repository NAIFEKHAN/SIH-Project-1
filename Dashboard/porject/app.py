from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample quiz questions
quiz_questions = [
    {"q": "Do you like solving math problems?", "field": "Science"},
    {"q": "Do you enjoy painting or literature?", "field": "Arts"},
    {"q": "Do you like managing money or business?", "field": "Commerce"}
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        answers = request.form.getlist("answer")
        # Simple scoring
        result = max(set(answers), key=answers.count)
        return redirect(url_for("dashboard", stream=result))
    return render_template("quiz.html", questions=quiz_questions)

@app.route("/dashboard/<stream>")
def dashboard(stream):
    # Dummy career mapping
    careers = {
        "Science": ["Engineer", "Doctor", "Researcher"],
        "Arts": ["Teacher", "Writer", "Designer"],
        "Commerce": ["Accountant", "Banker", "Business Analyst"]
    }
    return render_template("dashboard.html", stream=stream, careers=careers.get(stream, []))

if __name__ == "__main__":
    app.run(debug=True)
