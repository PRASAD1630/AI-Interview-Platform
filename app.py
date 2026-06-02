from models import user
from services.pdf_parser import extract_text
from services.pdf_report import generate_pdf_report
from services.ai_skill_extractor import extract_skills_ai
from services.ats_calculator import calculate_ats_score
from services.question_generator import generate_questions
from services.evaluator import evaluate_answer
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session

import sqlite3
import os 

app = Flask(__name__)

app.secret_key = "secret123"


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload_resume", methods=["GET", "POST"])
def upload_resume():

    if "user" not in session:
        return redirect("/login")

    if request.method == "POST":

        # Get Uploaded File
        file = request.files["resume"]

        # Save File
        filepath = os.path.join(
            "static",
            "uploads",
            file.filename
        )

        file.save(filepath)

        # Extract Text
        resume_text = extract_text(filepath)

        # AI Skill Extraction
        skills_text = extract_skills_ai(
            resume_text
        )

        skills = [
            skill.strip()
            for skill in skills_text.split(",")
        ]

        # Selected Role
        role = session.get(
            "selected_role",
            "AI Engineer"
        )

        # ATS Score
        ats_score, missing_skills = calculate_ats_score(
            skills,
            role
        )

        # Database Connection
        conn = sqlite3.connect(
            "database/interview.db"
        )

        cursor = conn.cursor()

        # Get User ID
        cursor.execute("""
        SELECT id
        FROM users
        WHERE name=?
        """,
        (session["user"],))

        user = cursor.fetchone()

        user_id = user[0]

        # Save Resume Data
        cursor.execute("""
        INSERT INTO resumes
        (
            user_id,
            resume_name,
            ats_score,
            skills,
            resume_text
        )
        VALUES (?,?,?,?,?)
        """,
        (
            user_id,
            file.filename,
            ats_score,
            ",".join(skills),
            resume_text
        ))

        conn.commit()
        conn.close()

        # Save ATS Data For PDF Download
        session["ats_score"] = ats_score
        session["role"] = role
        session["skills"] = ",".join(skills)
        session["missing_skills"] = ",".join(missing_skills)

        # ATS Suggestions
        suggestions = []

        for skill in missing_skills:

            suggestions.append(
        f"Learn {skill} and add it to your resume."
    )

        # Show ATS Result Page
        return render_template(
    "ats_result.html",
    role=role,
    ats_score=ats_score,
    skills=skills,
    missing_skills=missing_skills,
    suggestions=suggestions,
    resume_text=resume_text
)

    return render_template(
        "upload_resume.html"
    )
# -------------------------
# REGISTER
# -------------------------
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("database/interview.db")
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO users
            (name,email,password)
            VALUES (?,?,?)
            """,
            (name, email, password)
        )

        conn.commit()
        conn.close()

        return redirect("/login")

    return render_template("register.html")


# -------------------------
# LOGIN
# -------------------------
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("database/interview.db")
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM users
            WHERE email=?
            AND password=?
            """,
            (email, password)
        )

        user = cursor.fetchone()

        conn.close()

        if user:

            session["user"] = user[1]

            return redirect("/dashboard")

        else:
            return "Invalid Credentials"

    return render_template("login.html")

@app.route("/history")
def history():

    if "user" not in session:
        return redirect("/login")

    conn = sqlite3.connect(
        "database/interview.db"
    )

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        resume_name,
        ats_score,
        skills
    FROM resumes
    ORDER BY id DESC
    """)

    data = cursor.fetchall()

    conn.close()

    html = """

    <table class="table table-dark table-hover table-bordered">

        <thead>

            <tr>

                <th>Resume Name</th>

                <th>ATS Score</th>

                <th>Skills</th>

            </tr>

        </thead>

        <tbody>

    """

    for row in data:

        html += f"""

        <tr>

            <td>
                {row[0]}
            </td>

            <td>

                <span class="badge bg-success">

                    {row[1]}%

                </span>

            </td>

            <td>

                {row[2]}

            </td>

        </tr>

        """

    html += """

        </tbody>

    </table>

    """

    return render_template(
        "history.html",
        table=html
    )
@app.route("/generate_questions")
def generate_questions_page():

    if "user" not in session:
        return redirect("/login")

    conn = sqlite3.connect("database/interview.db")
    cursor = conn.cursor()

    # Get User ID
    cursor.execute("""
    SELECT id
    FROM users
    WHERE name=?
    """, (session["user"],))

    user = cursor.fetchone()

    if not user:
        conn.close()
        return "User Not Found"

    user_id = user[0]

    # Get Latest Resume Skills
    cursor.execute("""
    SELECT skills
    FROM resumes
    WHERE user_id=?
    ORDER BY id DESC
    LIMIT 1
    """, (user_id,))

    result = cursor.fetchone()

    if not result:
        conn.close()
        return "No Resume Found"

    skills = result[0]

    # Generate Questions using Gemini
    role = session.get(
    "selected_role",
    "AI Engineer"
)

    questions = generate_questions(
    skills,
    role
)

    # Split Questions
    question_list = questions.split("\n")

    # Save Questions
    for q in question_list:

        q = q.strip()

        if q:

            cursor.execute("""
            INSERT INTO questions
            (
            user_id,
            question
            )
            VALUES (?,?)
            """,
            (
            user_id,
            q
            ))

    conn.commit()
    conn.close()

    return redirect("/questions")
@app.route("/questions")
def questions():

    if "user" not in session:
        return redirect("/login")

    conn = sqlite3.connect(
        "database/interview.db"
    )

    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, question
    FROM questions
    ORDER BY id DESC
    """)

    data = cursor.fetchall()

    conn.close()

    html = ""

    count = 1

    for row in data:

        html += f"""
        <div class="glass-card p-4 mb-4">

            <h4> style="color:white;">
                Question {count}
            </h4>

            <hr>

            <p style="
                font-size:18px;
                color:white;
            ">
                {row[1]}
            </p>

            <a href="/answer_question/{row[0]}"
               class="btn btn-success">

                ✍ Answer Question

            </a>

        </div>
        """

        count += 1

    return render_template(
        "questions_list.html",
        questions_html=html
    )

@app.route("/mock_interview", methods=["GET", "POST"])
def mock_interview():

    if "user" not in session:
        return redirect("/login")

    if request.method == "POST":

        question = request.form["question"]

        answer = request.form["answer"]

        feedback = evaluate_answer(
            question,
            answer
        )
        conn = sqlite3.connect("database/interview.db")
        cursor = conn.cursor()

        cursor.execute("""
        SELECT id
        FROM users
        WHERE name=?
        """, (session["user"],))

        user = cursor.fetchone()

        user_id = user[0]

        cursor.execute("""
INSERT INTO interviews
(
user_id,
question,
answer,
feedback
)
VALUES (?,?,?,?)
""",
(
user_id,
question,
answer,
feedback
))

        conn.commit()
        conn.close()

        return render_template(
    "evaluation_result.html",
    feedback=feedback
)

    return render_template(
        "mock_interview.html"
    )

@app.route("/interview_history")
def interview_history():

    if "user" not in session:
        return redirect("/login")

    conn = sqlite3.connect(
        "database/interview.db"
    )

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        question,
        answer,
        feedback
    FROM interviews
    ORDER BY id DESC
    """)

    data = cursor.fetchall()

    conn.close()

    html = """

    <table class="table table-dark table-hover table-bordered">

        <thead>

            <tr>

                <th>Question</th>

                <th>Answer</th>

                <th>Feedback</th>

            </tr>

        </thead>

        <tbody>

    """

    for row in data:

        html += f"""

        <tr>

            <td>
                {row[0]}
            </td>

            <td>
                {row[1][:100]}...
            </td>

            <td>
                {row[2][:150]}...
            </td>

        </tr>

        """

    html += """

        </tbody>

    </table>

    """

    return render_template(
        "interview_history.html",
        table=html
    )
@app.route("/answer_question/<int:question_id>", methods=["GET", "POST"])
def answer_question(question_id):

    if "user" not in session:
        return redirect("/login")

    conn = sqlite3.connect("database/interview.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT question
    FROM questions
    WHERE id=?
    """, (question_id,))

    result = cursor.fetchone()

    if not result:
        conn.close()
        return "Question Not Found"

    question = result[0]

    if request.method == "POST":

        answer = request.form["answer"]

        feedback = evaluate_answer(
            question,
            answer
        )

        cursor.execute("""
        SELECT id
        FROM users
        WHERE name=?
        """, (session["user"],))

        user = cursor.fetchone()

        user_id = user[0]

        cursor.execute("""
        INSERT INTO interviews
        (
        user_id,
        question,
        answer,
        feedback
        )
        VALUES (?,?,?,?)
        """,
        (
        user_id,
        question,
        answer,
        feedback
        ))

        conn.commit()
        conn.close()

        return render_template(
    "evaluation_result.html",
    feedback=feedback
)

    conn.close()

    return render_template(
        "answer_question.html",
        question=question
    )
@app.route("/analytics")
def analytics():

    if "user" not in session:
        return redirect("/login")

    conn = sqlite3.connect(
        "database/interview.db"
    )

    cursor = conn.cursor()

    # Get User ID
    cursor.execute("""
    SELECT id
    FROM users
    WHERE name=?
    """,
    (session["user"],))

    user = cursor.fetchone()

    user_id = user[0]

    # Total Resumes
    cursor.execute("""
    SELECT COUNT(*)
    FROM resumes
    WHERE user_id=?
    """,
    (user_id,))

    total_resumes = cursor.fetchone()[0]

    # Total Interviews
    cursor.execute("""
    SELECT COUNT(*)
    FROM interviews
    WHERE user_id=?
    """,
    (user_id,))

    total_interviews = cursor.fetchone()[0]

    # Average ATS Score
    cursor.execute("""
    SELECT AVG(ats_score)
    FROM resumes
    WHERE user_id=?
    """,
    (user_id,))

    avg_ats = cursor.fetchone()[0]

    if avg_ats is None:
        avg_ats = 0

    avg_ats = round(avg_ats, 2)

    conn.close()

    return render_template(
        "performance_dashboard.html",
        total_resumes=total_resumes,
        total_interviews=total_interviews,
        avg_ats=avg_ats
    )
@app.route("/select_role", methods=["GET", "POST"])
def select_role():

    if "user" not in session:
        return redirect("/login")

    if request.method == "POST":

        role = request.form["role"]

        session["selected_role"] = role

        return redirect("/generate_questions")

    return render_template(
        "select_role.html"
    )
# -------------------------
# DASHBOARD
# -------------------------
@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/login")

    return render_template("dashboard.html")

@app.route("/download_report")
def download_report():

    if "user" not in session:
        return redirect("/login")

    role = session.get("role", "AI Engineer")

    ats_score = session.get("ats_score", 0)

    skills = session.get(
        "skills",
        ""
    ).split(",")

    missing_skills = session.get(
        "missing_skills",
        ""
    ).split(",")

    filename = os.path.join(
        "static",
        "ATS_Report.pdf"
    )

    generate_pdf_report(
        filename,
        role,
        ats_score,
        skills,
        missing_skills
    )

    from flask import send_file

    return send_file(
        filename,
        as_attachment=True
    )
# -------------------------
# LOGOUT
# -------------------------
@app.route("/logout")
def logout():

    session.pop("user", None)

    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)