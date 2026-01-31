/* Set up given to us */

-- PostgreSQL Schema & Data

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    joined_at DATE NOT NULL
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    price NUMERIC(8,2) NOT NULL
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE products_tags (
    product_id INTEGER NOT NULL REFERENCES products(id) ON DELETE CASCADE,
    tag_id INTEGER NOT NULL REFERENCES tags(id),
    PRIMARY KEY (product_id, tag_id)
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers(id) ON DELETE CASCADE,
    created_at DATE NOT NULL
);

CREATE TABLE orders_products (
    order_id INTEGER NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
    product_id INTEGER NOT NULL REFERENCES products(id),
    quantity INTEGER NOT NULL,
    PRIMARY KEY(order_id, product_id)
);

INSERT INTO customers (name, joined_at) VALUES
    ('Alice', '2025-01-10'),
    ('Bob',   '2025-02-02'),
    ('Cathy', '2025-02-10'),
    ('Dan',   '2025-02-14'),
    ('Eve',   '2025-03-01'),
    ('Frank', '2025-03-05'),
    ('Grace', '2025-03-07'),
    ('Hank',  '2025-03-09'),
    ('Ivy',   '2025-03-10'),
    ('John',  '2025-03-12'),
    ('Karen', '2025-03-18'),
    ('Ayu',   '2025-03-19'),
    ('Leo',   '2025-03-20');

INSERT INTO products (name, price) VALUES
    ('Laptop Sleeve', 29.99),
    ('Wireless Mouse', 19.99),
    ('Mechanical Keyboard', 89.99),
    ('USB-C Cable', 9.99),
    ('Noise-Canceling Headphones', 129.99),
    ('Standing Desk', 299.99),
    ('LED Monitor', 179.99),
    ('Ergonomic Chair', 249.99),
    ('Webcam', 49.99),
    ('Desk Lamp', 39.99),
    ('Portable SSD', 99.99),
    ('Tablet Stand', 24.99),
    ('Bluetooth Speaker', 59.99),
    ('Microphone', 79.99),
    ('Charging Station', 69.99),
    ('Whiteboard', 59.99),
    ('Laptop Stand', 34.99),
    ('HDMI Switch', 29.99),
    ('Desk Organizer', 19.99),
    ('Graphic Tablet', 149.99);

INSERT INTO tags (name) VALUES
    ('tech'),
    ('accessories'),
    ('audio'),
    ('office'),
    ('furniture'),
    ('storage'),
    ('video'),
    ('lighting'),
    ('productivity');

INSERT INTO products_tags VALUES
    (1,1),(1,2),
    (2,1),(2,2),
    (3,1),
    (4,1),(4,2),
    (5,1),(5,3),
    (6,4),(6,5),
    (7,1),(7,4),(7,7),
    (8,4),(8,5),
    (9,1),(9,2),(9,7),
    (10,8),(10,4),
    (11,1),(11,6),
    (12,2),(12,4),
    (13,3),(13,2),
    (14,3),(14,1),
    (15,1),(15,2),
    (16,4),(16,9),
    (17,2),(17,9),
    (18,1),(18,2),
    (19,4),(19,9),
    (20,1),(20,2);

INSERT INTO orders (customer_id, created_at) VALUES
    (1,'2025-03-01'),
    (1,'2025-03-12'),
    (2,'2025-03-05'),
    (3,'2025-03-09'),
    (5,'2025-03-11'),
    (6,'2025-03-13'),
    (7,'2025-03-14'),
    (7,'2025-03-20'),
    (8,'2025-03-15'),
    (9,'2025-03-15'),
    (10,'2025-03-16'),
    (11,'2025-03-17'),
    (12,'2025-03-18'),
    (3,'2025-03-21'),
    (2,'2025-03-22'),
    (4,'2025-03-23'),
    (4,'2025-03-25'),
    (8,'2025-03-26'),
    (9,'2025-03-27'),
    (5,'2025-03-29'),
    (6,'2025-03-30'),
    (7,'2025-03-30'),
    (1,'2025-03-31'),
    (10,'2025-04-01'),
    (12,'2025-04-02');

INSERT INTO orders_products VALUES
    (1,1,1),(1,4,2),(1,9,1),
    (2,3,1),
    (3,5,1),(3,4,1),
    (4,7,2),(4,2,1),
    (5,6,1),
    (6,10,1),(6,11,1),(6,4,3),
    (7,1,1),(7,2,2),(7,20,1),
    (8,6,1),(8,8,1),
    (9,13,2),
    (10,12,1),(10,18,1),
    (11,14,1),(11,5,1),
    (12,19,2),
    (13,15,1),(13,1,1),
    (14,7,1),(14,9,1),(14,10,1),
    (15,11,1),(15,17,1),
    (16,6,1),(16,3,1),(16,4,2),
    (17,8,1),(17,1,2),
    (18,2,1),(18,3,1),(18,13,1),
    (19,5,2),
    (20,16,1),(20,9,2),
    (21,6,1),(21,7,1),(21,3,1),
    (22,1,1),(22,12,1),(22,13,1),
    (23,2,1),(23,4,1),(23,5,1),
    (24,9,1),(24,10,1),(24,11,1),
    (25,20,1),(25,19,1),(25,3,1);


/* Draw an ERD that shows all tables and their relationships. Be sure to use crow’s foot notation to indicate both cardinality and modality. */

-- See advanced_1_erd.png

/* Let's start by looking at each order. List every order (id and when it was created) along with the customer name for the customer that placed the order. */

SELECT orders.id, orders.created_at, customers.name
FROM orders
LEFT JOIN customers ON orders.customer_id = customers.id;

/* We'd like to know how many products we carry for each tag. List all of the tags, along with the number of products we carry with that tag. Show the tags with the most products first. */
SELECT tags.name, count(products_tags.product_id) AS product_count
FROM tags
LEFT JOIN products_tags ON tags.id = products_tags.tag_id
GROUP BY tags.name
ORDER BY product_count DESC;

/* Given a certain tag name, like 'tech', list the name and price of all products that have that tag, sorted by price, ascending. */
SELECT p.name, p.price
FROM products p
JOIN products_tags pt ON p.id = pt.product_id
JOIN tags t ON pt.tag_id = t.id
WHERE lower(trim(t.name)) = 'tech' -- Proactive from learnings in prior exercises
ORDER BY p.price ASC;

/* Calculate the average number of distinct products in an order across all orders. Ignore the quantity and count each product only once per order. */

-- I use a left join below because there may be orders that don't have any products associated with them, which our database does allow for.

SELECT round(avg(distinct_product_count), 2)
FROM (
  SELECT 
    orders.id, 
    count(distinct orders_products.product_id) as distinct_product_count
  FROM orders
  LEFT JOIN orders_products ON orders.id = orders_products.order_id
  GROUP BY orders.id
) AS avg_items_per_order;

/*
List every product a specific customer has ordered, based on their ID. Each row should represent a single product line from a specific order, even if the same product appears in multiple orders. For each row, include:

the date the order was placed
the product name
the quantity ordered

Sort by most recent order first, and within each order, sort products alphabetically.
*/

SELECT 
  orders.created_at,
  products.name,
  orders_products.quantity
FROM orders
JOIN orders_products ON orders.id = orders_products.order_id
JOIN products ON orders_products.product_id = products.id
WHERE orders.customer_id = 1
ORDER BY orders.created_at DESC, products.name ASC;

/*
Find all products that have more than two tags. Show the product name and the number of tags it has.
*/
SELECT
  products.name,
  count(products_tags.tag_id)
FROM products
JOIN products_tags ON products.id = products_tags.product_id -- We can do a left join to include products that don't have tags but we don't need those for this query anyway
GROUP BY products.name
HAVING count(products_tags.tag_id) > 2;

/*
Find all orders that include at least one product with a specific tag (e.g., 'audio'). We just need the ID for the order.
*/
SELECT DISTINCT orders.id
FROM orders
JOIN orders_products ON orders.id = orders_products.order_id
JOIN products ON orders_products.product_id = products.id
JOIN products_tags ON products.id = products_tags.product_id
JOIN tags ON products_tags.tag_id = tags.id
WHERE tags.name = 'audio';

/* For each order, show the order ID, customer name, and total price. */
SELECT
  orders.id AS order_id,
  customers.name AS customer_name,
  sum(orders_products.quantity * products.price) AS total_price
FROM orders
JOIN customers ON orders.customer_id = customers.id
JOIN orders_products ON orders.id = orders_products.order_id
JOIN products ON orders_products.product_id = products.id
GROUP BY orders.id, customers.name
ORDER BY orders.id;

/*
We'd like to see each customer along with how much they've spent in total across all of their orders. List the customers who've spent the most first. We can omit customers who've never placed an order.
*/

SELECT 
  customers.name, 
  sum(orders_products.quantity * products.price) AS total_spent
FROM customers
JOIN orders ON customers.id = orders.customer_id
JOIN orders_products ON orders.id = orders_products.order_id
JOIN products ON orders_products.product_id = products.id
GROUP BY customers.name
ORDER BY total_spent DESC;

/*
For each tag, calculate the total number of products with that tag that have ever been ordered, counting each unit sold. Sort the tags from most to least popular. Products that have multiple tags will be counted multiple times. That's okay, we just want to know what tags are the most popular.
*/

SELECT
  tags.id,
  tags.name,
  sum(orders_products.quantity) AS units_sold
FROM tags
JOIN products_tags ON tags.id = products_tags.tag_id
JOIN orders_products ON products_tags.product_id = orders_products.product_id
GROUP BY tags.id, tags.name
ORDER BY units_sold DESC;