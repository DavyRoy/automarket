CREATE TABLE orders (
                        id          SERIAL PRIMARY KEY,
                        user_id     INTEGER NOT NULL,
                        car_id      INTEGER NOT NULL,
                        status      VARCHAR(50) CHECK (status IN ('pending', 'confirmed', 'cancelled')),
                        total_price NUMERIC CHECK (total_price > 0),
                        created_at  TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_orders_status  ON orders(status);