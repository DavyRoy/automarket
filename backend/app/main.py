from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db():
    return psycopg2.connect(
        host=os.environ.get("POSTGRES_HOST", "postgres-svc"),
        port=os.environ.get("POSTGRES_PORT", "5432"),
        database=os.environ.get("POSTGRES_DB", "automarket_db"),
        user=os.environ.get("POSTGRES_USER", "automarket_user"),
        password=os.environ.get("POSTGRES_PASSWORD", "")
    )

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/orders")
def get_orders():
    conn = get_db()
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)