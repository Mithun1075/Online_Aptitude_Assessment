# 🎓 Online Aptitude Assessment System

A modern, responsive, full-stack Django application designed to conduct automated online aptitude tests for candidates. The system handles candidate registration, dynamic question randomization across multiple technical categories, interactive test administration, real-time automated scoring, and detailed result displays.

---

## ✨ Features

- **📋 Candidate Registration**: Collects candidate profiles (Name, Email, Mobile, College, Degree, Year of Passing, Applied Position) with duplicate prevention checks.
- **🔐 Session-Based State Management**: Secure state tracking via Django sessions without requiring candidate account passwords.
- **🎲 Dynamic Question Sampling**: Automatically selects 5 randomized questions per category (English, Mathematics, Python, Django) for a total of 20 questions per test attempt.
- **🧠 Frozen Question Order**: Session locks selected question IDs so refreshing or navigating during the assessment preserves the question set.
- **⚡ Interactive UI & Validation**:
  - Interactive radio card selection with active state highlighting.
  - Client-side completion validation (alerts and smooth scrolls to unanswered questions).
  - Pre-submission confirmation prompt.
- **📊 Real-time Automated Scoring**: Immediate evaluation of submitted answers against correct answers upon test completion.
- **📁 Automated Question Importer**: Custom Django management command (`import_questions`) to seed/update questions directly from CSV files.
- **⚙️ Celery & Redis Support**: Architecture prepared for async score processing via background workers.
- **🛠️ Django Admin Integration**: Fully configured admin dashboard for managing candidates, questions, categories, answers, and results.

---

## 🛠️ Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Backend** | Python 3.12+, Django 5.2 | Core application logic, ORM, routing, and session management |
| **Database** | SQLite3 | Default database storing candidate data, questions, and test results |
| **Task Queue** | Celery 5.6 & Redis 8.0 | Asynchronous background worker setup |
| **Frontend** | HTML5, Bootstrap 5.3, Bootstrap Icons | Responsive page structures and icon set |
| **Styling** | Custom Vanilla CSS (`style.css`) | Custom design system with CSS variables, shadows, and transitions |
| **Client Logic** | Vanilla JavaScript (`assessment.js`) | Client-side validation, UI state handling, and submission logic |

---

## 📁 Directory Structure

```
Aptitude_Assessment/
├── Aptitude_Assessment/             # Core Project Configuration
│   ├── settings.py                   # Django settings & configurations
│   ├── urls.py                       # Global URL routing
│   ├── celery.py                     # Celery application initialization
│   ├── wsgi.py                       # WSGI entrypoint
│   └── asgi.py                       # ASGI entrypoint
├── Test/                             # Main Assessment Django App
│   ├── models.py                     # Candidate, Category, Question, Answer, & Result models
│   ├── views.py                      # Registration, assessment, submission, & result views
│   ├── urls.py                       # App-level routing
│   ├── admin.py                      # Customized Django Admin interfaces
│   ├── tasks.py                      # Celery background scoring task
│   └── management/
│       └── commands/
│           └── import_questions.py   # Seed command for CSV question data
├── templates/
│   └── Test/                         # HTML Templates
│       ├── base.html                 # Main template layout
│       ├── register.html             # Candidate registration form
│       ├── register_success.html     # Confirmation screen & test instructions
│       ├── assessment.html           # 20-question test form
│       ├── question_card.html        # Reusable question component
│       └── result.html               # Final score card
├── static/
│   └── Test/                         # Static Assets
│       ├── css/style.css             # Main stylesheet
│       └── js/assessment.js          # Client-side interactive script
├── questions.csv                     # Dataset containing multiple-choice questions
├── requirements.txt                  # Python dependencies
├── manage.py                         # Django management utility
└── README.md                         # Project documentation
```

---

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

Ensure you have the following installed:
- **Python 3.10+**
- **pip** (Python package installer)
- **Git**

---

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/Aptitude_Assessment.git
cd Aptitude_Assessment
```

---

### Step 2: Set Up Virtual Environment

Create and activate a Python virtual environment:

```bash
# On Linux / macOS
python3 -m venv venv
source venv/bin/activate

# On Windows (Command Prompt)
python -m venv venv
venv\Scripts\activate

# On Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1
```

---

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 4: Apply Database Migrations

Run Django migrations to create the required database tables:

```bash
python manage.py migrate
```

---

### Step 5: Import Question Dataset

Seed the database with questions from `questions.csv`:

```bash
python manage.py import_questions
```

> **Note**: This populates categories (`English`, `Maths`, `Python`, `Django`) and loads questions into the database.

---

### Step 6: Create Admin Superuser (Optional)

To access the Django Admin panel:

```bash
python manage.py createsuperuser
```

---

### Step 7: Run Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Open your browser and navigate to:
```
http://127.0.0.1:8000/
```

---

## 🔑 Administrative Access

Access the admin portal at `http://127.0.0.1:8000/admin/` to:
- View registered candidates.
- Add, edit, or delete questions and categories.
- Inspect submitted candidate answers and final test scores.

---

## ⚙️ Optional: Celery & Redis Setup

If background asynchronous score calculation is enabled in `settings.py`:

1. **Start Redis Server**:
   ```bash
   redis-server
   ```

2. **Start Celery Worker**:
   ```bash
   celery -A Aptitude_Assessment worker --loglevel=info
   ```

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.
