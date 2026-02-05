import psycopg2
from psycopg2 import extras

connection = psycopg2.connect(dbname='films')

cursor = connection.cursor()

## Use a select query to get rows
# cursor.execute('SELECT * FROM directors;')
# rows = cursor.fetchall()

## Insert data into the database
# cursor.execute(
#     """
#     INSERT INTO directors (name) VALUES ('Stanley Kubrick')
#     """
# )

cursor.close()
connection.commit()
connection.close()

# Using context managers:
try:
    with psycopg2.connect(dbname='films') as connection:
        with connection.cursor(cursor_factory=extras.DictCursor) as cursor:
            cursor.execute('SELECT * FROM directors;')
            rows = cursor.fetchall()
finally:
    # Using the context manager doesn't automatically close the connection though
    # It only ensures that the cursor is closed and the updates are committed
    connection.close()

print(f"Connection is closed: {connection.closed == 1}")

print("**********")

for row in rows:
    print(row['name'])

print("**********")

# Print the title of the film directed by Sidney Lumet
try:
    with psycopg2.connect(dbname='films') as connection:
        with connection.cursor(cursor_factory=extras.DictCursor) as cursor:
            cursor.execute("""
                SELECT * FROM films JOIN directors
                ON films.director_id = directors.id
                WHERE name = 'Sidney Lumet';
            """)
            films = cursor.fetchall()
finally:
    connection.close()

for film in films:
    print(film['title'])

print("**********")

"""
Write a Python program that uses the films database in such a way that the following code will print 113:

print(films[1]['duration'])
"""

try:
    with psycopg2.connect(dbname='films') as connection:
        with connection.cursor(cursor_factory=extras.DictCursor) as cursor:
            cursor.execute("""
                SELECT *
                FROM films
                JOIN directors on films.director_id = directors.id
                WHERE directors.name = 'Francis Ford Coppola'
                ORDER BY duration DESC;
            """)
            films = cursor.fetchall()
finally:
    connection.close()

print(films[1]['duration'])

print("**********")

"""
Write a Python application with psycopg2 that executes the following query. Use the results from this query to output each genre along with the number of films in that group.

SELECT genre, count(id) FROM films
  WHERE duration < 110
  GROUP BY genre;
"""

try:
    with psycopg2.connect(dbname='films') as connection:
        with connection.cursor(cursor_factory=extras.DictCursor) as cursor:
            cursor.execute("""
                SELECT genre, count(id) FROM films
                WHERE duration < 110
                GROUP BY genre;
            """)
            rows = cursor.fetchall()
finally:
    connection.close()

for row in rows:
    print(f"{row['genre']}: {row['count']}")