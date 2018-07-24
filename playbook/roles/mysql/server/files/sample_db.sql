CREATE DATABASE IF NOT EXISTS SampleDB;
CREATE TABLE IF NOT EXISTS SampleDB.User(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255)
);
INSERT INTO SampleDB.User (username, email) VALUES ('user1', 'user1@sample.com');
INSERT INTO SampleDB.User (username, email) VALUES ('user2', 'user2@sample.com');