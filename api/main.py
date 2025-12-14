from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

def get_db_connection():
    return psycopg2.connect(
        host="db",
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
    )

@app.get("/")
def health():
    try:
        conn = get_db_connection()
        conn.close()
        return {"status": "API running and DB connected"}
    except Exception as e:
        return {"status": "API running but DB not reachable", "error": str(e)}
