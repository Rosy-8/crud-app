from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:632003@localhost:5432/fastapi_db"
engine = create_engine(DATABASE_URL)

try:
    conn = engine.connect()
    print("Connected!")
    conn.close()
except Exception as e:
    print("Error:", e)
