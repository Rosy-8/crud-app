# CRUD Application using FastAPI

This is a simple CRUD (Create, Read, Update, Delete) application built using **Python** and **FastAPI** with a **PostgreSQL** database.

---

## 🚀 Tech Stack
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Uvicorn

---

## 📌 Features
- Create a user
- Get all users
- Get user by ID
- Update user details
- Delete user
- Interactive API documentation using Swagger UI

---

## 🛠️ How to Run the Project

Follow these steps to run the project locally.

1️⃣ Clone the repository
git clone https://github.com/Rosy-8/crud-app.git
cd crud-app

2️⃣ Create a virtual environment
venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

If requirements.txt is not available, install manually:
pip install fastapi uvicorn sqlalchemy psycopg2

4️⃣ Configure Database
Install PostgreSQL
Create a database
Update database credentials in the code (example):
DATABASE_URL = "postgresql://username:password@localhost:5432/dbname"

5️⃣ Run the application
uvicorn main:app --reload
or
python -m uvicorn main:app --reload

6️⃣ Open in browser
Swagger UI:
http://127.0.0.1:8000/docs

Redoc:
http://127.0.0.1:8000/redoc

📬 API Testing
You can test APIs using:
Swagger UI
Postman

👩‍💻 Author
Roselin Dsouza

📄 License
This project is for learning and internship purposes.
