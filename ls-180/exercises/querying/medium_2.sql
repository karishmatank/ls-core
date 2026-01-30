-- PostgreSQL Schema & Data

-- Tables
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    created_at DATE NOT NULL
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    content TEXT NOT NULL,
    created_at DATE NOT NULL
);

CREATE TABLE follows (
    follower_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    followee_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    PRIMARY KEY (follower_id, followee_id)
);

CREATE TABLE likes (
    post_id INTEGER NOT NULL REFERENCES posts(id) ON DELETE CASCADE,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    PRIMARY KEY (post_id, user_id)
);


-- Users
INSERT INTO users (name, created_at) VALUES
    ('Alice Wong', '2025-07-01'),
    ('Bob Smith', '2025-07-02'),
    ('Charlie Kim', '2025-07-03'),
    ('Dana Rodriguez', '2025-07-04'),
    ('Eve Johnson', '2025-07-05'),
    ('Fatima Ali', '2025-07-06'),
    ('George O''Connor', '2025-07-07'),
    ('Hiro Tanaka', '2025-07-08'),
    ('Isabella Rossi', '2025-07-09'),
    ('Jamal Brown', '2025-07-10'),
    ('Liam Patel', '2025-07-11'),
    ('Maya Singh', '2025-07-12');

-- Follows (who follows whom)
INSERT INTO follows (follower_id, followee_id) VALUES
    (1,2),(1,3),(1,6),(1,7),
    (2,1),(2,3),(2,5),(2,8),
    (3,1),(3,2),(3,4),(3,6),
    (4,3),(4,5),
    (5,2),(5,4),(5,10),
    (6,1),(6,3),(6,7),
    (7,6),(7,8),(7,1),
    (8,7),(8,9),(8,2),
    (9,8),(9,10),
    (10,5),(10,9);

-- Posts
INSERT INTO posts (user_id, content, created_at) VALUES
    (1, 'Just started a new painting, excited to share!', '2025-10-21'),
    (1, 'Morning yoga session complete, feeling great!', '2025-10-25'),
    (1, 'Last month I tried a new recipe for pasta.', '2025-09-15'),
    (2, 'Excited to share my new blog post on sustainable living!', '2025-10-20'),
    (2, 'Morning run in the park was amazing!', '2025-10-28'),
    (2, 'Attended a virtual conference on climate change.', '2025-10-30'),
    (2, 'Started learning guitar last month.', '2025-08-15'),
    (3, 'Just finished a great book on machine learning.', '2025-10-22'),
    (3, 'Cooking some Italian recipes tonight!', '2025-10-27'),
    (3, 'Trying out a new Python project!', '2025-10-24'),
    (3, 'Weekend trip was amazing!', '2025-09-10'),
    (4, 'Started learning the guitar, loving it!', '2025-10-24'),
    (4, 'Attended a local music workshop today.', '2025-10-29'),
    (4, 'Finished reading a book on mindfulness.', '2025-09-18'),
    (5, 'Looking for recommendations for sci-fi novels.', '2025-10-23'),
    (5, 'Joined a book club this weekend.', '2025-10-26'),
    (5, 'Trying out a new cafe in town ☕', '2025-06-10'),
    (6, 'Hiking trip this weekend was breathtaking.', '2025-10-25'),
    (6, 'New sketch added to my portfolio.', '2025-10-27'),
    (6, 'Experimenting with watercolor techniques.', '2025-10-30'),
    (6, 'Visited the art museum last month.', '2025-09-12'),
    (7, 'Attended a fantastic jazz concert yesterday.', '2025-10-22'),
    (7, 'Learning to play the piano.', '2025-10-28'),
    (7, 'Watched a documentary on space exploration.', '2025-08-05'),
    (8, 'Experimenting with plant-based recipes!', '2025-10-21'),
    (8, 'Trying a new cycling route today.', '2025-10-29'),
    (8, 'Weekend hike was amazing.', '2025-09-25'),
    (9, 'Photography session by the lake, amazing sunset.', '2025-10-28'),
    (9, 'Editing my travel photos from Italy.', '2025-10-30'),
    (9, 'Planning next month''s trip.', '2025-09-05'),
    (10, 'Participated in local charity event today!', '2025-10-23'),
    (10, 'Organizing community cleanup for Saturday.', '2025-10-27');

-- Likes
INSERT INTO likes (post_id, user_id) VALUES
    (1,2),(1,3),(1,4),(1,5),(1,6),
    (2,2),(2,3),
    (3,1),(3,4),(3,5),(3,6),
    (4,1),(4,2),(4,3),
    (5,3),(5,6),
    (6,1),(6,2),(6,4),
    (7,1),(7,3),(7,5),(7,6),
    (8,2),(8,5),(8,7),
    (9,1),(9,6),(9,7),(9,8),
    (10,3),(10,5),(10,8),
    (11,1),(11,4),
    (12,2),(12,6),(12,7),
    (13,1),(13,3),(13,5),(13,7),(13,8),
    (14,2),(14,5),
    (15,3),(15,7),
    (16,1),(16,5),(16,6),
    (17,2),(17,6),(17,8),
    (18,1),(18,4),(18,5),
    (19,2),(19,6),(19,9),
    (20,1),(20,3);

/* Draw an ERD that shows all tables and their relationships. Be sure to use crow’s foot notation to indicate both cardinality and modality. */

-- See medium_2_erd.png

/* We want to work on an initiative where we try to promote users who aren't following anyone yet. People tend to engage more when they follow people! Can you help us figure out what users aren’t following anyone? */

SELECT users.name
FROM users
LEFT JOIN follows ON users.id = follows.follower_id
WHERE follows.follower_id IS NULL; -- Either column will be NULL

/* We’re doing a report on engagement. We need a query that shows us, for each user, how many likes they’ve made. */
SELECT users.name, count(likes.post_id)
FROM users
LEFT JOIN likes ON users.id = likes.user_id
GROUP BY users.name
ORDER BY count(likes.post_id) DESC;

/* We’re working on a report and we need all of the posts along with how many likes each has, with the most popular posts first, please. We would like posts with no likes to also be included. */
SELECT posts.id, posts.content, count(likes.user_id) AS num_likes
FROM posts
LEFT JOIN likes ON posts.id = likes.post_id
GROUP BY posts.id, posts.content
ORDER BY num_likes DESC;

/* Oh, sorry, we forgot to tell you that we want the users id and name as well. So we need all posts, their like count, who authored them, and the user’s id, with the most popular posts coming first. */
SELECT 
  posts.content, 
  users.name AS author, 
  users.id AS user_id, 
  count(likes.user_id) AS num_likes
FROM posts
LEFT JOIN likes ON posts.id = likes.post_id
LEFT JOIN users ON posts.user_id = users.id
GROUP BY posts.content, author, users.id
ORDER BY num_likes DESC;

/* We want to highlight the top three most liked posts from October 2025 so far for the homepage. Sent on October 7th, 2025. */
SELECT posts.id, posts.content, count(likes.user_id) as num_likes
FROM posts
JOIN likes ON posts.id = likes.post_id
WHERE posts.created_at BETWEEN '2025-10-01' AND '2026-10-07'
GROUP BY posts.id, posts.content
ORDER BY num_likes DESC
LIMIT 3;

/* Find users who haven’t posted in the last 30 days so we can send them a reminder email. Sent on November 28th, 2025. */

SELECT name
FROM users
WHERE id NOT IN (
  SELECT user_id
  FROM posts
  WHERE created_at BETWEEN '2025-10-29' AND '2025-11-28'
);

-- Using a join instead
SELECT users.name
FROM users
LEFT JOIN posts ON users.id = posts.user_id
GROUP BY users.name
HAVING max(posts.created_at) < '2025-10-29' OR max(posts.created_at) IS NULL;

/* We’d like to identify influencers, or users with the most followers. Can you show us the 5 users with the most followers, along with the number of followers they have? */
SELECT users.name, count(follows.follower_id) as follower_count
FROM users
JOIN follows ON users.id = follows.followee_id
GROUP BY users.name
ORDER BY follower_count DESC
LIMIT 5;

/* We’re doing a data analysis project and we need to be able to find the most active user that a specific user follows. For example, if I give you an ID of 2 that’s associated with Bob Smith, I want to get back the user that Bob Smith follows that has the most posts out of all of the users that Bob Smith follows. */

SELECT follows.followee_id, uf.name, count(posts.id) AS num_posts
FROM users
JOIN follows ON users.id = follows.follower_id
JOIN posts ON posts.user_id = follows.followee_id
JOIN users uf ON follows.followee_id = uf.id
WHERE users.id = 2
GROUP BY follows.followee_id, uf.name
ORDER BY num_posts DESC
LIMIT 1;

-- We can clean this up- we didn't need the final join if joined on the other ID column in follows:
SELECT users.name, count(posts.id) AS num_posts
FROM users
JOIN follows ON users.id = follows.followee_id
JOIN posts ON posts.user_id = users.id
WHERE follows.follower_id = 2
GROUP BY users.name
ORDER BY num_posts DESC
LIMIT 1;

-- To recap the different approaches:
-- - Follower-centered (your query):
--     - “Start with Bob (follower), then ask: who does he follow, and how many posts do they have?”
-- - Followee-centered (official):
--     - “Start with all possible followees and ask: which of these are followed by Bob, and how many posts does each have?”

/* 
We want to implement a “suggested for you” feature.

Given a user’s ID, find all users that:

The user does not already follow.
Are followed by at least one user that the given user already follows (i.e., friends of friends).
Return each user once, even if multiple mutual connections exist.
*/

-- Assume we are building the feature for user ID 1

SELECT name -- Don't need DISTINCT because users will be unique in the users table anyway
FROM users
WHERE 
  id NOT IN (
    SELECT followee_id
    FROM follows
    WHERE follower_id = 1
  ) AND
  id IN (
    SELECT f_removed.followee_id
    FROM follows f_immediate
    JOIN follows f_removed ON f_immediate.followee_id = f_removed.follower_id
    WHERE f_immediate.follower_id = 1
  ) AND
  id != 1; -- Forgot to exclude the user themselves