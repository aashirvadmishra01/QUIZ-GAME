# QUIZ GAME

**Project Title**

Interactive Command-Line Quiz Game Using Python

**Objective**

The purpose of this BYOP project is to design and develop a Python-based interactive quiz application that tests user knowledge through multiple-choice questions. The project showcases the use of essential programming concepts such as loops, conditional statements, input validation, and the implementation of Python built-in modules (random, time, and sys).

**Problem statement **

Many beginners struggle to understand how Python modules can be applied practically in real coding situations. Traditional theoretical learning does not provide enough hands-on experience.
This project addresses that problem by building a functional quiz system that:

Randomizes question order,

Accepts user answers via input,

Validates responses,

Displays scores dynamically,

Gives an interactive feel using delays,

Exits the program safely after execution.

**Scope**

This quiz program:

Displays a set of multiple-choice questions one by one.

Allows users to answer using options A, B, C, or D.

Uses real-time feedback (Correct/Incorrect).

Calculates and displays the final score.

Utilizes three different built-in Python modules.

This project can be expanded with features like a graphical interface, additional question categories, timers, and score saving capability.

**Modules Used**

Module	Use
random	Randomizes quiz question order
time	Adds delay between questions for better experience
sys	Terminates the program gracefully after completion

**Technology Used**

Language: Python 3.x

Programming Paradigm: Procedural

Platform: Command-line terminal

**Working Logic (Summary)**

 1. A list of question dictionaries is predefined.

2. The random.shuffle() function randomizes their order.

3. The program displays each question and accepts user input.

4. The score increases for each correct answer.

5. time.sleep() adds a pause between questions.

6. After finishing all questions, final score is displayed.

7. Program terminates using sys.exit().

**Expected Output**

Interactive quiz interface

Printed questions and choices

Score result in format:
Final Score: X out of Y

**Conclusion**

The BYOP Quiz Game project successfully demonstrates the real-world application of Python programming fundamentals and built-in modules. It enhances logical thinking, user interaction skills, and structured programming ability. This project represents the foundation for building more advanced quiz or assessment-based applications.
