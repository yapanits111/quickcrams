package com.quickcrams.quickcrams.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import com.quickcrams.quickcrams.models.Quiz;
import com.quickcrams.quickcrams.models.QuizResult;
import com.quickcrams.quickcrams.repositories.QuizRepository;
import com.quickcrams.quickcrams.repositories.QuizResultRepository;

@RestController
@RequestMapping("/api/quiz")
@CrossOrigin(origins = "http://localhost:8501") // Allow specific frontend origin
public class QuizController {

    @Autowired
    private QuizRepository quizRepository;

    @Autowired
    private QuizResultRepository quizResultRepository;

    // Create a new quiz
    @PostMapping
    public ResponseEntity<Quiz> createQuiz(@RequestBody Quiz quiz) {
        Quiz savedQuiz = quizRepository.save(quiz);
        return ResponseEntity.ok(savedQuiz);
    }

    // Get all quizzes
    @GetMapping
    public ResponseEntity<List<Quiz>> getAllQuizzes() {
        List<Quiz> quizzes = quizRepository.findAll();
        return ResponseEntity.ok(quizzes);
    }

    // Submit quiz results
    @PostMapping("/results")
    public ResponseEntity<QuizResult> submitQuizResults(@RequestBody QuizResult quizResult) {
        QuizResult savedResult = quizResultRepository.save(quizResult);
        return ResponseEntity.ok(savedResult);
    }

    // Get all quiz results
    @GetMapping("/results")
    public ResponseEntity<List<QuizResult>> getQuizResults() {
        List<QuizResult> results = quizResultRepository.findAll();
        return ResponseEntity.ok(results);
    }
}
