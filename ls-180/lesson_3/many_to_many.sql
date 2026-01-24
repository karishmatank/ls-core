/* 
createdb many_to_many
curl 'https://raw.githubusercontent.com/launchschool/sql_course_data/master/sql-and-relational-databases/relational-data-and-joins/many-to-many-relationships/many_to_many.sql' | psql -d many_to_many
*/

/* The books_categories table from this database was created with foreign keys that don't have the NOT NULL and 
ON DELETE CASCADE constraints. Go ahead and add them now.
*/
ALTER TABLE books_categories
ALTER COLUMN book_id SET NOT NULL,
ALTER COLUMN category_id SET NOT NULL,
DROP CONSTRAINT books_categories_book_id_fkey,
DROP CONSTRAINT books_categories_category_id_fkey;

ALTER TABLE books_categories
ADD FOREIGN KEY (book_id) REFERENCES books (id) ON DELETE CASCADE,
ADD FOREIGN KEY (category_id) REFERENCES categories (id) ON DELETE CASCADE;

/* Write a SQL statement that will return the following result:
 id |     author      |           categories
----+-----------------+--------------------------------
  1 | Charles Dickens | Fiction, Classics
  2 | J. K. Rowling   | Fiction, Fantasy
  3 | Walter Isaacson | Nonfiction, Biography, Physics
(3 rows)
*/
SELECT books.id, books.author, string_agg(categories.name, ', ') as categories
FROM books 
INNER JOIN books_categories ON books.id = books_categories.book_id
INNER JOIN categories ON categories.id = books_categories.category_id
GROUP BY books.id, books.author
ORDER BY books.id;

/* Write SQL statements to insert the following new books into the database. 
What do you need to do to ensure this data fits in the database?

Author	Title	Categories
Lynn Sherr	Sally Ride: America's First Woman in Space	Biography, Nonfiction, Space Exploration
Charlotte Brontë	Jane Eyre	Fiction, Classics
Meeru Dhalwala and Vikram Vij	Vij's: Elegant and Inspired Indian Cuisine	Cookbook, Nonfiction, South Asia
*/

-- Title of one book below turns out to be too long, need to alter data type of column
ALTER TABLE books
ALTER COLUMN title TYPE text;

INSERT INTO books (title, author) VALUES
('Sally Ride: America''s First Woman in Space', 'Lynn Sherr'),
('Jane Eyre', 'Charlotte Brontë'),
('Vij''s: Elegant and Inspired Indian Cuisine', 'Meeru Dhalwala and Vikram Vij');

INSERT INTO categories (name) VALUES
('Space Exploration'),
('Cookbook'),
('South Asia');

INSERT INTO books_categories (book_id, category_id) VALUES
(4, 5),
(4, 1),
(4, 7),
(5, 2),
(5, 4),
(6, 8),
(6, 1),
(6, 9);

/* Write a SQL statement to add a uniqueness constraint on the combination of columns book_id and category_id 
of the books_categories table. This constraint should be a table constraint; so, it should check 
for uniqueness on the combination of book_id and category_id across all rows of the books_categories table.
*/

ALTER TABLE books_categories
ADD UNIQUE (book_id, category_id);

/* Write a SQL statement that will return the following result:

      name        | book_count |                                 book_titles
------------------+------------+-----------------------------------------------------------------------------
Biography         |          2 | Einstein: His Life and Universe, Sally Ride: America's First Woman in Space
Classics          |          2 | A Tale of Two Cities, Jane Eyre
Cookbook          |          1 | Vij's: Elegant and Inspired Indian Cuisine
Fantasy           |          1 | Harry Potter
Fiction           |          3 | Jane Eyre, Harry Potter, A Tale of Two Cities
Nonfiction        |          3 | Sally Ride: America's First Woman in Space, Einstein: His Life and Universe, Vij's: Elegant and Inspired Indian Cuisine
Physics           |          1 | Einstein: His Life and Universe
South Asia        |          1 | Vij's: Elegant and Inspired Indian Cuisine
Space Exploration |          1 | Sally Ride: America's First Woman in Space

*/
SELECT categories.name, count(books.id) AS book_count, string_agg(books.title, ', ') AS book_titles
FROM categories
INNER JOIN books_categories ON categories.id = books_categories.category_id
INNER JOIN books ON books.id = books_categories.book_id
GROUP BY categories.name
ORDER BY categories.name;