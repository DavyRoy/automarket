from flask import Flask, jsonify
import psycopg2
import pymysql
import redis
import json
import os

app = Flask(__name__)

redis_client = redis.Redis(
    host=os.environ.get("REDIS_HOST", "redis-svc"),
    port=int(os.environ.get("REDIS_PORT", "6379")),
    decode_responses=True
)

def get_postgres():
    return psycopg2.connect(
        host=os.environ.get("POSTGRES_HOST", "postgres-svc"),
        port=os.environ.get("POSTGRES_PORT", "5432"),
        database=os.environ.get("POSTGRES_DB", "automarket_db"),
        user=os.environ.get("POSTGRES_USER", "automarket_user"),
        password=os.environ.get("POSTGRES_PASSWORD", "")
    )

def get_mysql():
    return pymysql.connect(
        host=os.environ.get("MYSQL_HOST", "mysql-svc"),
        port=int(os.environ.get("MYSQL_PORT", "3306")),
        database=os.environ.get("MYSQL_DATABASE", "automarket_db"),
        user=os.environ.get("MYSQL_USER", "automarket_user"),
        password=os.environ.get("MYSQL_PASSWORD", ""),
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/orders")
def get_orders():
    conn = get_postgres()
    cur = conn.cursor()
    cur.execute("SELECT id, user_id, car_id, status, total_price, created_at FROM orders")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([
        {"id": r[0], "user_id": r[1], "car_id": r[2],
         "status": r[3], "total_price": str(r[4]), "created_at": str(r[5])}
        for r in rows
    ])

@app.route("/cars")
def get_cars():
    cache_key = "cars:all"
    cached = redis_client.get(cache_key)

    if cached:
        print("Cache HIT", flush=True)
        return jsonify(json.loads(cached))

    print("Cache MISS", flush=True)
    conn = get_mysql()
    cur = conn.cursor()
    cur.execute("SELECT id, brand, model, year, price, mileage FROM cars")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Конвертируем Decimal в float для JSON сериализации
    serializable_rows = [
        {k: float(v) if isinstance(v, __import__('decimal').Decimal) else v
         for k, v in row.items()}
        for row in rows
    ]

    redis_client.setex(cache_key, 60, json.dumps(serializable_rows))
    return jsonify(serializable_rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)