# Project 3 - Python Functions and Methods

## Description

This step covers Python Functions and Methods.

The project in this section applies the concepts learned from both topics in a practical command-line text analysis application.

The main goal of this project is to understand how multiple small functions can work together to build a larger and more organized program.

I chose this project because it allowed me to move beyond writing isolated functions and practice building a complete application where each function has a specific responsibility.

---

## Topics Covered

* Functions
* Function Parameters
* Arguments
* Return Values
* Built-in Functions
* String Methods
* `len()`
* `split()`
* `isupper()`
* `islower()`
* `isdigit()`
* Lists
* Dictionaries
* `for` Loops
* `if` Statements
* `in` Operator
* List Methods
* Function Reuse
* Function Composition

---

## Project

### Text Analyzer

A command-line text analysis application that analyzes user-provided text and generates useful information about its content.

Features include:

* Count total characters
* Count uppercase letters
* Count lowercase letters
* Count digits
* Count total words
* Find unique words
* Count word frequency

The project is structured using multiple functions, where each function is responsible for one specific task.

The `analyze_text()` function acts as the main coordinator and uses the other functions to generate the final analysis report.

---

## Why I Chose This Project

I chose this project because I wanted to understand how individual functions can be combined to create a complete application.

Instead of writing all the logic inside one large block of code, I divided the program into several smaller functions.

For example:

* `count_characters()` is responsible for counting characters.
* `count_uppercase()` is responsible for counting uppercase letters.
* `count_lowercase()` is responsible for counting lowercase letters.
* `count_digits()` is responsible for counting numeric characters.
* `count_words()` is responsible for counting words.
* `get_unique_words()` is responsible for finding unique words.
* `count_word_frequency()` is responsible for counting how many times each word appears.
* `analyze_text()` coordinates all the functions and displays the final report.

This project helped me understand the importance of:

* Reusable code
* Single responsibility
* Function composition
* Returning values from functions
* Organizing a program into smaller logical components

---

## Example

### Input

```text
Hello. My name is Erfan and 35 years old. What is your name?

---

## Author

Erfan Nemati
