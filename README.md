# 🚀 AI Interview Preparation Platform

## 📌 Project Overview

The AI Interview Preparation Platform is a Flask-based web application designed to help students and job seekers prepare for technical interviews using Artificial Intelligence.

The platform analyzes resumes, calculates ATS scores, generates interview questions based on skills and job roles, evaluates answers using Gemini AI, provides performance analytics, and generates downloadable reports.

---

# 🎯 Problem Statement

Many candidates struggle to prepare for technical interviews due to:

* Lack of personalized interview questions
* Poor resume ATS optimization
* Limited feedback on interview performance
* Difficulty identifying missing skills

This platform solves these challenges using AI-powered analysis and feedback.

---

# ✨ Features

## 1. User Authentication

* User Registration
* User Login
* Session Management
* Secure Logout

---

## 2. Resume Upload & Analysis

* Upload Resume (PDF)
* Extract Resume Text
* AI Skill Extraction using Gemini
* Resume Storage

---

## 3. ATS Score Calculator

* Role-Based Skill Matching
* ATS Score Calculation
* Missing Skill Detection
* Improvement Suggestions

Supported Roles:

* Data Scientist
* AI Engineer
* Machine Learning Engineer
* Full Stack Developer
* Backend Developer
* Frontend Developer

---

## 4. AI Interview Question Generation

Generates personalized interview questions based on:

* Resume Skills
* Selected Job Role
* AI Analysis

Examples:

* Python Interview Questions
* Machine Learning Questions
* Deep Learning Questions
* SQL Questions
* Flask Questions

---

## 5. Answer Evaluation System

Uses Gemini AI to:

* Evaluate Answers
* Provide Feedback
* Identify Weak Areas
* Suggest Improvements

---

## 6. Mock Interview Module

Provides:

* AI-Based Mock Interviews
* Question Practice
* Answer Submission
* Performance Tracking

---

## 7. Performance Dashboard

Displays:

* Total Resumes Uploaded
* Total Interviews Attempted
* Average ATS Score
* Performance Analytics

---

## 8. Resume History

Stores:

* Uploaded Resumes
* ATS Scores
* Extracted Skills

---

## 9. Interview History

Stores:

* Questions Attempted
* Answers Submitted
* AI Feedback

---

## 10. PDF Report Generation

Generate downloadable reports containing:

* ATS Score
* Skills
* Missing Skills
* Recommendations

---

# 🛠️ Technologies Used

## Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript

## Backend

* Python
* Flask

## Database

* SQLite

## AI Integration

* Google Gemini AI

## PDF Processing

* pdfplumber
* reportlab

## Deployment

* GitHub
* Render

---

# 📂 Project Structure

```text
AI_Interview_Platform
│
├── app.py
├── requirements.txt
├── Procfile
├── runtime.txt
│
├── database
│   └── interview.db
│
├── templates
│   ├── index.html
│   ├── dashboard.html
│   ├── login.html
│   ├── register.html
│   ├── upload_resume.html
│   ├── ats_result.html
│   ├── questions_list.html
│   ├── answer_question.html
│   ├── performance_dashboard.html
│   └── ...
│
├── services
│   ├── ai_skill_extractor.py
│   ├── ats_calculator.py
│   ├── evaluator.py
│   ├── pdf_parser.py
│   ├── question_generator.py
│   └── ...
│
├── static
│   ├── css
│   ├── js
│   └── uploads
│
└── utils
    └── config.py
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/PRASAD1630/AI-Interview-Platform.git
```

## Move into Project

```bash
cd AI-Interview-Platform
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

Windows:

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

# ▶️ Run Project

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

# 📊 Workflow

1. Register/Login
2. Upload Resume
3. Extract Skills
4. Calculate ATS Score
5. Identify Missing Skills
6. Generate AI Questions
7. Submit Answers
8. Receive AI Feedback
9. Track Performance
10. Download Reports

---

# 🚀 Future Enhancements

* Voice-Based Interviews
* Video Interview Analysis
* Facial Expression Analysis
* Job Recommendation System
* AI Career Roadmaps
* Resume Builder
* LinkedIn Integration
* Cloud Database Integration

---

# 👨‍💻 Author

Bhukya Prasad

AI & Machine Learning Engineering

Chaitanya Bharathi Institute of Technology (CBIT)

---

# 📜 License

This project is developed for educational and learning purposes.
