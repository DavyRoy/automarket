CREATE TABLE cars (
                      id          INT AUTO_INCREMENT PRIMARY KEY,
                      brand       VARCHAR(100) NOT NULL,
                      model       VARCHAR(100) NOT NULL,
                      year        INT CHECK (year >= 2000),
                      price       DECIMAL(10,2) CHECK (price > 0),
                      mileage     INT CHECK (mileage >= 0),
                      description TEXT,
                      created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 20 тестовых записей — реальные марки, реальные цены
INSERT INTO cars (brand, model, year, price, mileage) VALUES
                                                          ('Toyota', 'Camry', 2021, 2500000, 15000),
                                                          ('Toyota', 'RAV4', 2022, 3200000, 22000),
                                                          ('Toyota', 'Land Cruiser 200', 2020, 5800000, 45000),
                                                          ('BMW', '3 Series', 2021, 3900000, 28000),
                                                          ('BMW', '5 Series', 2020, 4700000, 35000),
                                                          ('BMW', 'X5', 2022, 6900000, 18000),
                                                          ('Mercedes-Benz', 'C-Class', 2021, 4100000, 26000),
                                                          ('Mercedes-Benz', 'E-Class', 2020, 5200000, 32000),
                                                          ('Mercedes-Benz', 'GLE', 2022, 7600000, 14000),
                                                          ('Audi', 'A4', 2021, 3600000, 30000),
                                                          ('Audi', 'A6', 2020, 4700000, 34000),
                                                          ('Audi', 'Q7', 2022, 7100000, 17000),
                                                          ('Kia', 'K5', 2021, 2400000, 29000),
                                                          ('Kia', 'Sportage', 2022, 2800000, 21000),
                                                          ('Hyundai', 'Sonata', 2020, 2200000, 40000),
                                                          ('Hyundai', 'Tucson', 2021, 2700000, 25000),
                                                          ('Volkswagen', 'Passat', 2020, 2300000, 38000),
                                                          ('Volkswagen', 'Touareg', 2021, 5200000, 27000),
                                                          ('Lexus', 'RX350', 2022, 6500000, 16000),
                                                          ('Nissan', 'X-Trail', 2021, 2600000, 31000);