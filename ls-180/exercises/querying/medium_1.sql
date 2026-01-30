/* Set up given to us */
-- PostgreSQL Schema & Data

-- Customers table
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT,
    created_at TEXT
);

-- Orders table
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER,
    total_amount REAL,
    status TEXT,
    order_date TEXT
);

-- Customers
INSERT INTO customers (id, name, email, created_at) VALUES
    (1, 'Alice Wong', 'alice@acme.com', '2025-01-10'),
    (2, 'Bob Smith', 'bob@acme.com', '2025-01-12'),
    (3, 'Alice Wong', 'alice.wong@acme.com', '2025-01-10'),
    (4, 'Charlie Kim', 'charlie@lumos.com', '2025-02-15'),
    (5, 'Dana Rodriguez', 'dana@lumos.com', '2025-02-17'),
    (6, 'Eve Johnson', 'unknown@domain.com', '2025-5-01'),
    (7, 'Frank Brown', 'unknown@domain.com', '2025-05-05'),
    (8, 'Grace Chen', NULL, '2025-02-18'),
    (9, 'Hannah Lee', 'hannah@zenith.com', 'Feb 30 2025'),
    (10, 'Ian Kim', 'ian@zenith.com', 'january'),
    (11, 'Malik Johnson', 'malik.johnson@example.com', '2025-06-01'),
    (12, 'Malcolm Johnson', 'malik.johnson@example.com', '2025-11-04');

-- Orders
INSERT INTO orders (id, customer_id, total_amount, status, order_date) VALUES
    (1, 1, 100.50, 'pending', '2025-09-01'),
    (2, 2, 200.00, 'PENDING', '2025-09-02'),
    (3, 3, 150.00, 'Pending ', '2025/09/03'),
    (4, 4, -50.00, 'closed', '2025-09-04'),
    (5, 5, 0, 'open', '09-05-2025'),
    (6, NULL, 75.00, 'pending', '2025-09-06'),
    (7, 6, 120.00, 'Pending ', '2025-09-07'),
    (8, 7, 90.00, 'completed', '2025-09-08'),
    (9, 8, 50.00, 'OPEN', '2025-09-09'),
    (10, 9, 110.00, 'closed', '2025-09-10'),
    (11, 10, NULL, 'pending', '2025-09-11'),
    (12, 10, NULL, 'pending', '2025-09-11'),
    (13, 999, 60.00, 'pending', '2025-09-12'),
    (14, 31, 603.00, 'PENDING', '2025-09-12');

/* Draw an ERD that shows all tables and their relationships. Be sure to use crow’s foot notation to indicate both cardinality and modality.

Hard to draw ERD in code, but essentially:
- There is a relationship between customers and orders (one to many):
  - A customer can have zero or many orders (cardinality = many, modality = 0)
  - An order can only have one customer, however, this column is nullable!!! 
    - So effectively, while an order can have at most one customer, it is optional (cardinality = 1, modality = 0)
*/

/* To get started, let's just take a look at what we're working with. Let's look at all orders along with the customers who placed them. Since we know things are messy, let's include all orders even if they don't have an associated customer. */

SELECT 
  orders.id, 
  orders.customer_id,
  orders.total_amount, 
  orders.status,
  orders.order_date,
  customers.name
FROM orders
LEFT JOIN customers ON orders.customer_id = customers.id;

/* Find all orders where the customer_id does not match any existing customer. */
-- Need to remember to look for NULL as well, as that won't come through in the NOT IN part.
SELECT *
FROM orders
WHERE customer_id NOT IN (
  SELECT id
  FROM customers
) OR customer_id IS NULL;

/* Identify emails that are shared between multiple customers, along with the number of customers that use that email. */

SELECT email, count(id)
FROM customers
GROUP BY email
HAVING count(id) > 1
ORDER BY count(id) DESC;

/*
We’ve just realized that we have been making decisions based on incorrect data. We’ve been using this query to see how many orders have a status of pending:

SELECT COUNT(*) AS pending_orders
FROM orders
WHERE status = 'pending';

But someone just pointed out that there’s some other values for pending, like PENDING and other similar, but not quite right, versions. Could you try to create a query that will give us accurate results for what orders are pending and which aren't?
*/

SELECT count(*) AS pending_orders
FROM orders
WHERE status ilike '%pending%';

-- The above works for our use case, but it will also match 'not pending' and other unrelated statuses, so we should instead do:
SELECT count(*) AS pending_orders
FROM orders
WHERE lower(trim(status)) = 'pending';

/* List each order status and how many orders have that status. As you might remember, the statuses are a bit messy. Group these sensibly without changing data. */

SELECT
  lower(trim(status)) AS clean_order,
  count(id)
FROM orders
GROUP BY clean_order;

/*
We’ve been using this query to sort orders by total_amount, but the first few rows in the results seem to be broken or invalid. Update this query so that it sorts the orders by total_amount while ignoring invalid values.

SELECT *
FROM orders
ORDER BY total_amount;
*/

SELECT *
FROM orders
WHERE 
  total_amount IS NOT NULL AND
  total_amount > 0
ORDER BY total_amount;

/* Part 2- How could we modify this query to include only orders with a valid total_amount that also have a valid customer? */

SELECT *
FROM orders
WHERE 
  total_amount IS NOT NULL AND
  total_amount > 0 AND
  customer_id IS NOT NULL AND
  customer_id IN (
    SELECT id FROM customers
  )
ORDER BY total_amount;

/* We want the total revenue from all orders, regardless of status, but some orders have negative or zero total_amount, and some aren't linked to a valid customer. Write a query that sums orders with a valid customer_id and a positive total_amount. */

SELECT sum(total_amount)
FROM orders
WHERE
  total_amount > 0 AND -- This won't include NULLs, which is what we want
  customer_id IS NOT NULL AND
  customer_id IN (
    SELECT id FROM customers
  );

/* Calculate the average total of all valid orders. Valid orders are any order where the total_amount is present and positive. */
SELECT avg(total_amount)
FROM orders
WHERE
  total_amount > 0; -- This already won't include NULLs, which is what we want. We can still include IS NOT NULL on a separate line if we want

/* Someone has reported that there are some invalid dates. They didn’t say what they were. Can you produce a query that shows us all of the values for created_at that don’t fit the expected format?

In PostgreSQL, you match a regular expression with ~. 
PostgreSQL: my_column ~ 'pattern'
*/

SELECT order_date
FROM orders
WHERE NOT order_date ~ '([0-9]{4})-([0-9]{2})-([0-9]{2})';

SELECT created_at
FROM customers
WHERE NOT created_at ~ '^([0-9]{4})-([0-9]{2})-([0-9]{2})$';

/* Some customers appear to have multiple entries. Can you provide a list of all customer entries who appear to have the same name or email as another account? Make sure it’s case in-sensitive. */

-- NOTE: Remember to standardize to one case (lowercase)

SELECT *
FROM customers
WHERE 
  lower(name) IN (
    SELECT lower(name)
    FROM customers
    GROUP BY lower(name)
    HAVING count(id) > 1
  ) OR 
  lower(email) IN (
    SELECT lower(email)
    FROM customers
    GROUP BY lower(email)
    HAVING count(id) > 1
  );

