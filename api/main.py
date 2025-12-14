from fastapi import FastAPI
import psycopg2
import redis
import os

app = FastAPI()

def get_db_connection():
    return psycopg2.connect(
        host="db",
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
    )

def get_redis_connection():
    return redis.Redis(host="redis", port=6379)

@app.get("/")
def health():
    status = {}

    try:
        conn = get_db_connection()
        conn.close()
        status["database"] = "connected"
    except Exception as e:
        status["database"] = str(e)

    try:
        r = get_redis_connection()
        r.ping()
        status["redis"] = "connected"
    except Exception as e:
        status["redis"] = str(e)

    return status
