CREATE DATABASE IF NOT EXISTS health_records_db;

USE health_records_db;

-- A+
CREATE TABLE IF NOT EXISTS patients_a_pos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(50) NOT NULL,
    medical_history TEXT
);

-- A-
CREATE TABLE IF NOT EXISTS patients_a_neg (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(50) NOT NULL,
    medical_history TEXT
);

-- B+
CREATE TABLE IF NOT EXISTS patients_b_pos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(50) NOT NULL,
    medical_history TEXT
);

-- B-
CREATE TABLE IF NOT EXISTS patients_b_neg (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(50) NOT NULL,
    medical_history TEXT
);

-- AB+
CREATE TABLE IF NOT EXISTS patients_ab_pos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(50) NOT NULL,
    medical_history TEXT
);

-- AB-
CREATE TABLE IF NOT EXISTS patients_ab_neg (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(50) NOT NULL,
    medical_history TEXT
);

-- O+
CREATE TABLE IF NOT EXISTS patients_o_pos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(50) NOT NULL,
    medical_history TEXT
);

--  O-
CREATE TABLE IF NOT EXISTS patients_o_neg (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(50) NOT NULL,
    medical_history TEXT
);
