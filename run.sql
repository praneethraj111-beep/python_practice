USE my_first_db;

-- This removes the 7 extra names
DELETE FROM test;

-- This adds your name back once
INSERT INTO test (manish)
VALUES('MANISH');

-- This show the final result
SELECT * FROM test;
INSERT INTO test (manish)
VALUES ('VASAVI');

INSERT INTO test (manish)
VALUES ('LEKHANA');
ALTER TABLE test MODIFY COLUMN manish VARCHAR(255);
ALTER TABLE test ADD UNIQUE (manish);
-- Adds a column for whole numbers
ALTER TABLE test ADD COLUMN age INT;

-- Adds a column for text (Male/Female)
ALTER TABLE test ADD COLUMN gender VARCHAR(10);
UPDATE test SET age = 30,gender = 'Male' WHERE manish = 'MANISH';
UPDATE test SET age = 29,gender = 'Female' WHERE manish = 'VASAVI';
UPDATE test SET age = 3,gender = 'Female' WHERE manish = 'LEKHANA';
SELECT * FROM test ORDER BY age ASC;
SELECT AVG(age) FROM test;