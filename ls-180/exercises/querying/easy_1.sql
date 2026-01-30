/* Set up given to us */
-- Postgres Schema & Data

-- Tables
CREATE TABLE authors (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  country TEXT
);

CREATE TABLE publishers (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  founded_year INTEGER
);

CREATE TABLE books (
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  published_year INTEGER,
  price NUMERIC(6,2),
  author_id INTEGER NOT NULL REFERENCES authors(id) ON DELETE CASCADE,
  publisher_id INTEGER NOT NULL REFERENCES publishers(id) ON DELETE CASCADE
);

-- Data
-- Authors
INSERT INTO authors (name, country) VALUES
  ('Haruki Murakami',          'Japan'),
  ('Toni Morrison',            'USA'),
  ('Chimamanda Ngozi Adichie', 'Nigeria'),
  ('George Orwell',            'UK'),
  ('Jane Austen',              'UK'),
  ('Kazuo Ishiguro',           'UK'),
  ('Margaret Atwood',          'Canada'),
  ('Gabriel García Márquez',   'Colombia'),
  ('Jhumpa Lahiri',            'USA'),
  ('Colson Whitehead',         'USA');

-- Publishers
INSERT INTO publishers (name, founded_year) VALUES
  ('Vintage Books',    1954),
  ('Penguin Classics', 1946),
  ('Knopf',            1915),
  ('HarperCollins',    1989),
  ('Random House',     1927);

-- Books
INSERT INTO books (title, published_year, price, author_id, publisher_id) VALUES
  ('Norwegian Wood',                1987, 14.99, 1, 1),
  ('Kafka on the Shore',            2002, 17.50, 1, 1),
  ('The Wind-Up Bird Chronicle',    1994, 18.50, 1, 3),
  ('Beloved',                       1987, 13.95, 2, 3),
  ('Song of Solomon',               1977, 12.99, 2, 3),
  ('Half of a Yellow Sun',          2006, 15.99, 3, 3),
  ('Americanah',                    2013, 16.50, 3, 1),
  ('1984',                          1949, 12.50, 4,  2),
  ('Animal Farm',                   1945, 10.99, 4,  2),
  ('Pride and Prejudice',           1813, 9.99,  5,  2),
  ('Emma',                          1815, 10.50, 5,  2),
  ('Never Let Me Go',               2005, 14.25, 6,  1),
  ('The Remains of the Day',        1989, 13.75, 6,  3),
  ('The Handmaid''s Tale',          1985, 13.95, 7,  4),
  ('Oryx and Crake',                2003, 14.95, 7,  4),
  ('One Hundred Years of Solitude', 1967, 15.50, 8,  5),
  ('Love in the Time of Cholera',   1985, 14.75, 8,  5),
  ('The Namesake',                  2003, 13.50, 9,  1),
  ('Interpreter of Maladies',       1999, 11.99, 9,  1),
  ('The Underground Railroad',      2016, 16.99, 10, 5),
  ('The Nickel Boys',               2019, 15.25, 10, 5);

/* Draw an ERD that shows all tables and their relationships. Be sure to use crow’s foot notation to indicate both cardinality and modality.

Hard to draw ERD in code, but essentially:
- There is a relationship between authors and books (one to many):
  - An author can write zero or many books (cardinality = many, modality = 0)
  - A single book must only be written, as modelled above, by one author (cardinality = 1, modality = 1 because of the NOT NULL constraint on author_id in the books table)
- Similarly, there is a one-to-many relationship between books and publishers
  - A publisher can publish zero or many books (cardinality = many, modality = 0)
  - A single book must be published by one publisher (cardinality = 1, modality = 1)
*/

/* Write a query to find all books published after 2000. */
SELECT title
FROM books
WHERE published_year > 2000;

/* Write a query to find the title and publication year of the oldest book in the database. */
SELECT title, published_year
FROM books
ORDER BY published_year ASC
LIMIT 1;

/* Find the 3 most expensive books, sorted from most to least expensive. Again, it’s up to you to confirm that your query produces the correct results. */
SELECT title, price
FROM books
ORDER BY price DESC
LIMIT 3;

/* Show each book’s title alongside the author’s name. */
/* We already know from the schema exploration exercise that every book must have an author. If that weren’t true, we’d have to decide how to interpret the request ourselves. With this schema, an INNER JOIN is sufficient. */

SELECT books.title, authors.name
FROM books
JOIN authors ON books.author_id = authors.id;

/* For each publisher, show how many books they’ve published. */
-- NOTE: LEFT JOIN matters here! We might have a publisher with no books, given modality of 0
SELECT publishers.name, count(books.id)
FROM publishers
LEFT JOIN books on publishers.id = books.publisher_id
GROUP BY publishers.name;

/* Show each author’s name and the average price of their books, sorted by most to least expensive average. */
SELECT authors.name, round(avg(books.price), 2) as average_price
FROM authors
LEFT JOIN books ON authors.id = books.author_id
GROUP BY authors.name
ORDER BY  average_price DESC;

/* List authors who have published more than one book, along with the number of books they’ve published. */
SELECT authors.name, count(books.id)
FROM authors
JOIN books ON authors.id = books.author_id
GROUP BY authors.name
HAVING count(books.id) > 1;

/* Find all books that cost more than the average price of all books. */
SELECT title
FROM books
WHERE price > (
  SELECT avg(price) FROM books
);

/* List the names of all UK authors along with the publishers that have released their books. If an author has books with multiple publishers, include each author–publisher pair. However, if an author has multiple books with the same publisher, show that pair only once. */
SELECT DISTINCT a.name AS author, p.name AS publisher
FROM authors a
JOIN books b ON a.id = b.author_id
JOIN publishers p ON b.publisher_id = p.id
WHERE a.country = 'UK';