-- Create Database
CREATE DATABASE cramsdb;

-- Use the newly created database
USE cramsdb;

-- Create User Table
CREATE TABLE User (
    userId BIGINT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

-- Create Quiz Table
CREATE TABLE Quiz (
    quizId BIGINT AUTO_INCREMENT PRIMARY KEY,
    question TEXT NOT NULL,
    option1 TEXT,
    option2 TEXT,
    option3 TEXT,
    option4 TEXT
);

-- Create QuizResult Table
CREATE TABLE QuizResult (
    quizResultId BIGINT AUTO_INCREMENT PRIMARY KEY,
    quizId BIGINT NOT NULL,
    userId BIGINT NOT NULL,
    score INT NOT NULL,
    FOREIGN KEY (quizId) REFERENCES Quiz(quizId),
    FOREIGN KEY (userId) REFERENCES User(userId)
);

-- Create Flashcard Table
CREATE TABLE Flashcard (
    flashcardId BIGINT AUTO_INCREMENT PRIMARY KEY,
    front TEXT NOT NULL,
    back TEXT NOT NULL
);

-- Create Note Table
CREATE TABLE Note (
    noteId BIGINT AUTO_INCREMENT PRIMARY KEY,
    content TEXT NOT NULL,
    noteTitle VARCHAR(255) NOT NULL
);

CREATE TABLE Role (
    roleId BIGINT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE UserRoles (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    role_id BIGINT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(userId) ON DELETE CASCADE,
    FOREIGN KEY (role_id) REFERENCES Role(roleId) ON DELETE CASCADE,
    CONSTRAINT user_role_unique UNIQUE (user_id, role_id) -- Prevents duplicate entries
);