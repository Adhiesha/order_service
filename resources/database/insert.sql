USE ordersdb;

-- Insert a sample order
INSERT INTO orders (customer_name, total_price)
VALUES ('Alice Johnson', 74.00);

-- Insert items for that order (assumes last inserted order ID = 1)
INSERT INTO order_items (order_id, game_id, game_title, quantity, price)
VALUES
  (1, 'AC003', 'Assassin''s Creed: Valhalla', 1, 30.00),
  (1, 'COD MMII', 'Call of Duty®: Modern Warfare® II', 2, 22.00);

-- Insert another order
INSERT INTO orders (customer_name, total_price)
VALUES ('Bob Smith', 26.00);

INSERT INTO order_items (order_id, game_id, game_title, quantity, price)
VALUES
  (2, 'AC004', 'Assassin''s Creed: Origins', 1, 26.00);
