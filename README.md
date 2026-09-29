# 🎓 Online Aptitude Assessment System

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.12%20%7C%203.13-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2-green?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A modern, responsive, full-stack Django web application engineered to conduct automated online aptitude assessments for recruitment and skill evaluation. The system features seamless candidate registration, randomized question sampling across 4 technical categories, locked session states, real-time automated grading, and an administrative dashboard.

---

## 📌 Table of Contents

- [Key Features](#-key-features)
- [System Architecture & Workflow](#-system-architecture--workflow)
- [Tech Stack](#-tech-stack)
- [Directory Structure](#-directory-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation & Setup](#installation--setup)
- [Database Seeding](#-database-seeding)
- [Administrative Portal](#-administrative-portal)
- [Assessment Configuration](#-assessment-configuration)
- [License](#-license)

---

## ✨ Key Features

- **📋 Streamlined Candidate Registration**:
  - Collects candidate profile details (*Full Name, Email, Mobile Number, College, Degree, Year of Passing, Applied Position*).
  - Built-in validation prevents duplicate test attempts by phone number or email address.
- **🔐 Passwordless Session Tracking**:
  - Secure session tracking eliminates the friction of account creation while ensuring test integrity.
- **🎲 Multi-Category Question Randomization**:
  - Samples **5 randomized questions per category** (English, Mathematics, Python, Django) for a total of **20 questions** per assessment attempt.
- **🧠 Frozen Question State**:
  - Selected question IDs are frozen in the candidate's active session. Browser refreshes, accidental reloads, or navigation retain the exact question set without re-shuffling.
- **⚡ Intuitive Candidate Interface**:
  - Interactive choice cards with real-time selection highlighting.
  - Client-side completion guard: detects unanswered questions, alerts the candidate, and smoothly scrolls directly to the first missing answer.
  - Pre-submission confirmation dialog prevents accidental form submissions.
- **📊 Instant Automated Scoring**:
  - Evaluates candidate answers against the answer key immediately upon submission and renders a detailed score report.
- **📁 CSV Question Bank Importer**:
  - Custom Django management command (`import_questions`) loads, parses, and updates questions and categories directly from `questions.csv`.
- **🛠️ Comprehensive Django Admin**:
  - Search, filter, and inspect registered candidates, individual answers submitted, and final scores.

---

## 🛠️ Tech Stack

| Layer | Technology | Description |
| :--- | :--- | :--- |
| **Backend Framework** | [Django 5.2](https://www.djangoproject.com/) | MVC structure, ORM, URL routing, session management, CSRF protection |
| **Language** | [Python 3.10+](https://www.python.org/) | Core backend programming language (Tested on 3.12 & 3.13) |
| **Database** | [SQLite3](https://www.sqlite.org/) | Default relational database engine storing candidates, questions, and scores |
| **Frontend Framework** | [Bootstrap 5.3](https://getbootstrap.com/) | Responsive UI layout, utility classes, and typography |
| **Iconography** | [Bootstrap Icons](https://icons.getbootstrap.com/) | Vector icons for cards, alerts, and navigation |
| **Typography** | [Google Fonts (Poppins)](https://fonts.google.com/specimen/Poppins) | Clean, modern sans-serif typography |
| **Client Scripts** | Vanilla JavaScript | Selection state handler, unanswered validation, and submission confirmation |
| **Custom Styling** | Vanilla CSS (`style.css`) | Curated CSS custom properties, micro-animations, and responsive cards |

---

## 📁 Directory Structure

```
Online_Aptitude_Assessment/
├── Aptitude_Assessment/             # Core Project Configuration
│   ├── __init__.py
│   ├── asgi.py                      # ASGI application entrypoint
│   ├── celery.py                    # Celery application initialization
│   ├── settings.py                  # Django settings, security & static paths
│   ├── urls.py                      # Root URL routing table
│   └── wsgi.py                      # WSGI application entrypoint
├── Test/                            # Main Assessment Application
│   ├── management/
│   │   └── commands/
│   │       └── import_questions.py  # Custom seed command for CSV question data
│   ├── migrations/                  # Database migration history
│   │   ├── 0001_initial.py
│   │   └── 0002_alter_candidate_email_alter_candidate_mobile.py
│   ├── __init__.py
│   ├── admin.py                     # Customized Django admin interfaces
│   ├── apps.py                      # App configuration
│   ├── models.py                    # Candidate, Category, Question, Answer & Result models
│   ├── tasks.py                     # Background scoring tasks
│   ├── tests.py                     # Unit & integration test cases
│   ├── urls.py                      # App-level routes (register, assessment, submit, result)
│   └── views.py                     # Core request handlers and evaluation logic
├── templates/
│   └── Test/                        # HTML Templates
│       ├── base.html                # Base layout with navbar, footer & assets
│       ├── register.html            # Candidate onboarding form
│       ├── register_success.html    # Profile confirmation & assessment rules
│       ├── assessment.html          # Main 20-question assessment interface
│       ├── question_card.html       # Reusable modular question card component
│       └── result.html              # Final scorecard and evaluation summary
├── static/
│   └── Test/                        # Static Assets
│       ├── css/
│       │   └── style.css            # Custom CSS design system
│       └── js/
│           └── assessment.js        # Client validation & option selection script
├── questions.csv                    # 100-question seed dataset (English, Maths, Python, Django)
├── requirements.txt                 # Project dependencies
├── manage.py                        # Django CLI management utility
├── .gitignore                       # Git ignore rules for venv, cache & database
└── README.md                        # Documentation
```

---

## 🚀 Getting Started

Follow these steps to run the application locally on your machine.

### Prerequisites

Ensure you have the following installed:
- **Python 3.10+** ([Download Python](https://www.python.org/downloads/))
- **Git** ([Download Git](https://git-scm.com/))
- **pip** (bundled with Python)

---

### Installation & Setup

#### 1. Clone the Repository
```bash
git clone https://github.com/Mithun1075/Online_Aptitude_Assessment.git
cd Online_Aptitude_Assessment
```

#### 2. Create and Activate Virtual Environment

- **Windows (PowerShell)**:
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
- **Windows (Command Prompt)**:
  ```cmd
  python -m venv venv
  venv\Scripts\activate.bat
  ```
- **macOS / Linux**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Apply Database Migrations
```bash
python manage.py migrate
```

#### 5. Seed the Question Bank
Populate the database with the questions and categories from `questions.csv`:
```bash
python manage.py import_questions
```

#### 6. Create Superuser (Admin Access)
```bash
python manage.py createsuperuser
```
Follow the prompts to configure an admin username, email, and password.

#### 7. Run the Development Server
```bash
python manage.py runserver
```

Open your browser and navigate to:
```
http://127.0.0.1:8000/
```

---

## 📊 Database Seeding

The application includes `questions.csv` pre-populated with **100 multiple-choice questions** across four domains:

| Category | Description | Question Count |
| :--- | :--- | :--- |
| **English** | Vocabulary, grammar, error detection, professional phrasing | 26 |
| **Maths** | Quantitative aptitude, speed & distance, ratios, percentages | 25 |
| **Python** | Core syntax, data structures, generators, OOP concepts | 25 |
| **Django** | ORM queries, middleware, template tags, routing, architecture | 24 |

You can add new questions directly to `questions.csv` using the format:
```csv
category,question,option1,option2,option3,option4,correct_answer
```
Then re-run:
```bash
python manage.py import_questions
```
Existing questions will be safely skipped while new entries are automatically added.

---

## 🔑 Administrative Portal

Access the admin dashboard at `http://127.0.0.1:8000/admin/`:

- **Candidate Profiles**: View candidate registrations, graduation years, and positions applied for.
- **Question Management**: Add, update, or re-categorize questions and answer keys.
- **Answer Logs**: Inspect submitted candidate answers question-by-question.
- **Candidate Results**: View total scores, submission timestamps, and performance metrics.

---

## ⚙️ Assessment Configuration

- **Question Count**: By default, each test loads **5 questions per section** across 4 categories (20 questions total).
- **Duration & Rules**: Standard test guidelines are displayed on the instructions page before starting the exam.
- **Retake Policy**: Once submitted, the candidate is locked to their result page unless an admin clears their record or the session is flushed via `/finish/`.

---

## 📝 License

This project is licensed under the **MIT License**. Feel free to use, modify, and distribute it for academic or commercial purposes.
