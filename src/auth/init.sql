CREATE DATABASE auth;

GRANT ALL PRIVILEGES ON auth.* TO 'root'@'localhost';

USE auth;

CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

INSERT INTO users (email, password) VALUES ('allan.zf.tan@gmail.com', 'Admin123')