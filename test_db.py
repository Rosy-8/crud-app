import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    print("Error: DATABASE_URL is not set in the environment or .env file.")
    exit(1)

engine = create_engine(DATABASE_URL)

try:
    conn = engine.connect()
    print("Connected successfully using environment variables!")
    conn.close()
except Exception as e:
    print("Error connecting to the database:", e)
