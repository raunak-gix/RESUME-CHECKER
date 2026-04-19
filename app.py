from flask import Flask, render_template, request
import pdfplumber
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Basic skill keywords
REQUIRED_SKILLS = [
    "python", "java", "react", "node", "aws",
    "machine learning", "sql", "html", "css", "javascript"
]

def extract_text_from_pdf(filepath):
    text = ""
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text.lower()

def analyze_resume(text):
    score = 0
    found_skills = []
    
    for skill in REQUIRED_SKILLS:
        if skill in text:
            found_skills.append(skill)

    # Scoring logic
    skill_score = (len(found_skills) / len(REQUIRED_SKILLS)) * 40
    length_score = 20 if len(text.split()) > 200 else 10
    project_score = 20 if "project" in text else 10
    format_score = 20 if "@" in text else 10  # email check

    total_score = int(skill_score + length_score + project_score + format_score)

    missing_skills = list(set(REQUIRED_SKILLS) - set(found_skills))

    suggestions = []
    if missing_skills:
        suggestions.append("Add missing skills: " + ", ".join(missing_skills[:5]))
    if "project" not in text:
        suggestions.append("Include project experience")
    if "@" not in text:
        suggestions.append("Add contact email")
    if len(text.split()) < 200:
        suggestions.append("Increase content length")

    return total_score, found_skills, missing_skills, suggestions

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["resume"]

        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            text = extract_text_from_pdf(filepath)
            score, found, missing, suggestions = analyze_resume(text)

            return render_template("index.html",
                                   score=score,
                                   found=found,
                                   missing=missing,
                                   suggestions=suggestions)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)