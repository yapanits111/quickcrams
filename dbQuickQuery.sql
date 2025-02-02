-- Create Database
CREATE DATABASE cramsdb;

-- Use the newly created database
USE cramsdb;

CREATE TABLE User (
    userId BIGINT AUTO_INCREMENT PRIMARY KEY,
    firstName VARCHAR(255) NOT NULL,
    lastName VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE Quiz (
    quizId BIGINT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    question TEXT NOT NULL,
    choices JSON NOT NULL,
    correctOption VARCHAR(255) NOT NULL,
    userId BIGINT,
    FOREIGN KEY (userId) REFERENCES User(userId)
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

