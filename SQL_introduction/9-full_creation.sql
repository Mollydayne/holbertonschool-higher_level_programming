-- script that creates a table second_table in the database hbtn_0c_0 - task 9. Full creation

CREATE TABLE IF NOT EXISTS second_table
(
    id INT PRIMARY KEY,
    name VARCHAR(256),
    score INT PRIMARY KEY
);

INSERT INTO second_table(ID, name, score)
VALUES('1', 'John', '10');
VALUES('2', 'Alex', '3');
VALUES('3', 'Bob', '14');
VALUES('4', 'George', '8');
