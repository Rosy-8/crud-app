# 🚀 CRUD Application using FastAPI & PostgreSQL

This is a simple, robust CRUD (Create, Read, Update, Delete) application built using **Python**, **FastAPI**, and a **PostgreSQL** database.

---

## 📌 Features
* 👤 **Create a User** - Add new users to the database.
* 📋 **Get All Users** - Retrieve the full list of users.
* 🔍 **Get User by ID** - Find specific user details.
* ✏️ **Update User** - Modify existing user details.
* ❌ **Delete User** - Remove users from the database.
* 📖 **Interactive API Docs** - Built-in interactive documentation using Swagger UI & ReDoc.

---

## 🛠️ Tech Stack
* **Framework:** FastAPI
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy
* **Server:** Uvicorn
* **Security:** Python-dotenv (Environment Variables)

---

## 🚀 How to Run the Project

Follow these steps to set up and run the project locally.

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Rosy-8/crud-app.git
cd crud-app
```

### 2️⃣ Create and Activate a Virtual Environment
**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```
**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure the Database
1. Make sure you have **PostgreSQL** installed and running on your machine.
2. Create a new database named `fastapi_db`.
3. Create a `.env` file in the root of the project:
   * Copy the template: `cp .env.example .env` (or manually create a `.env` file).
4. Open the `.env` file and replace the credentials with your local PostgreSQL username and password:
   ```env
   DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/fastapi_db
   ```

### 5️⃣ Run the Application
Start the Uvicorn development server:
```bash
python -m uvicorn main:app --reload
```

### 6️⃣ Open in Browser
Once the server is running, you can access the interactive API documentations at:
* **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📬 API Testing
You can test the APIs directly using:
* **Swagger UI** (interactive browser client)
* **Postman** (by sending requests to `http://127.0.0.1:8000`)

---

## 👩‍💻 Author
**Roselin Dsouza**

---

## 📄 License
This project is for learning and internship purposes.
