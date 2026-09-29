@echo off
echo Starting Online Aptitude Assessment System...
cd /d "%~dp0"

if not exist "venv\Scripts\python.exe" (
    echo Virtual environment not found. Initializing...
    "C:\Users\MSI\AppData\Local\Programs\Python\Python313\python.exe" -m venv venv
    venv\Scripts\pip install -r requirements.txt
    venv\Scripts\python manage.py migrate
)

echo Starting server at http://127.0.0.1:8000/
start http://127.0.0.1:8000/
venv\Scripts\python.exe manage.py runserver 127.0.0.1:8000
pause
