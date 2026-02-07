DROP TABLE expenses;

CREATE TABLE expenses (
  id serial PRIMARY KEY,
  amount numeric(6,2) NOT NULL CHECK (amount >= 0.01),
  memo text NOT NULL,
  created_on date NOT NULL DEFAULT NOW()
);

INSERT INTO expenses (amount, memo) VALUES
(14.56, 'Pencils'),
(3.29, 'Coffee'),
(49.99, 'Text Editor');