package com.quickcrams.quickcrams;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import com.quickcrams.quickcrams.models.User;
import com.quickcrams.quickcrams.repositories.UserRepository;

@SpringBootApplication
public class UserTest implements CommandLineRunner {

    @Autowired
    private UserRepository userRepository;

    public static void main(String[] args) {
        SpringApplication.run(UserTest.class, args);
    }

    @Override
    public void run(String... args) throws Exception {
        User user = new User();
        user.setUsername("Daniel");
        user.setPassword("Alex123");
        userRepository.save(user);
        System.out.println("User saved successfully!");
    }
}