/* Import
https://raw.githubusercontent.com/launchschool/sql_course_data/master/sql-and-relational-databases/relational-data-and-joins/foreign-keys/orders_products1.sql

createdb orders_products1
curl 'https://raw.githubusercontent.com/launchschool/sql_course_data/master/sql-and-relational-databases/relational-data-and-joins/foreign-keys/orders_products1.sql' | psql -d orders_products1
*/

/* Update the orders table so that referential integrity will be preserved for the data between orders and products. */
ALTER TABLE orders
ADD FOREIGN KEY (product_id) REFERENCES products (id);
-- I omitted the name because I don't want to memorize how to name foreign keys

/* Use psql to insert the data shown in the following table into the database:
Quantity	Product
10	small bolt
25	small bolt
15	large bolt 
*/

INSERT INTO products (name) VALUES ('small bolt'), ('large bolt');

-- small bolt has id 1, large bolt has id 2
INSERT INTO orders (product_id, quantity) VALUES
(1, 10),
(1, 25),
(2, 15);

/* Write a SQL statement that returns a result like this:
 quantity |    name
----------+------------
       10 | small bolt
       25 | small bolt
       15 | large bolt
(3 rows) */

SELECT orders.quantity, products.name
FROM orders INNER JOIN products ON orders.product_id = products.id;

/* Can you insert a row into orders without a product_id? Write a SQL statement to prove your answer. */
INSERT INTO orders (quantity) VALUES (5);
-- Yes, we can because there is no not null constraint on the product_id column in the orders table

/* Write a SQL statement that will prevent NULL values from being stored in orders.product_id. 
What happens if you execute that statement? */

DELETE FROM orders
WHERE product_id IS NULL;

ALTER TABLE orders
ALTER COLUMN product_id
SET NOT NULL;

/* Create a new table called reviews to store the data shown below. This table should include a primary key 
and a reference to the products table. 

Product	Review
small bolt	a little small
small bolt	very round!
large bolt	could have been smaller
*/
CREATE TABLE reviews (
  id serial PRIMARY KEY,
  product_id integer REFERENCES products (id),
  body varchar(100) NOT NULL
);
-- Edit: Did not include the not null constraint on body at first

INSERT INTO reviews (product_id, body) VALUES
(1, 'a little small'),
(1, 'very round!'),
(2, 'could have been smaller');