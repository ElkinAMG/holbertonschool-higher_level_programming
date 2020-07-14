-- Creates a new DATABASE called <hbtn_0d_usa> and the TABLE called <states>.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256));
