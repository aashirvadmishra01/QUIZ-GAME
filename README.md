# QUIZ-GAME
A simple command–line interactive quiz game built using Python.
This project demonstrates the use of three built-in Python modules: random, time, and sys.
The user is presented with multiple-choice questions, and their final score is displayed at the end.

📌 Features

✔ Randomized question order (using random.shuffle())

✔ Accepts user input and validates responses

✔ Introduces delay between questions for better interaction (using time.sleep())

✔ Gracefully ends the program using sys.exit()

✔ Displays the final score after completion

🛠 Modules Used
Module	Purpose
random	Used to shuffle the order of quiz questions
time	Adds a delay to enhance user experience
sys	Exits the program when quiz ends
🚀 How to Run the Project
1️⃣ Install Python

Ensure Python 3.x is installed on your system.

2️⃣ Save the file

Save the code to a file named:

quiz_game.py

3️⃣ Run the program

Open terminal / command prompt and run:

python quiz_game.py

📂 Project Structure
quiz_game.py     # Main program file

💡 How It Works

The quiz questions are stored in a list of dictionaries.

The questions are shuffled randomly.

User answers each question by typing A, B, C, or D.

Score increases when the answer is correct.

Final score is displayed and the program exits.

🧾 Sample Output
--- 🧠  Quiz Game ! ---

Question 1: Which module is used to shuffle items in a list?
  A. sys
  B. math
  C. random
  D. time
Your answer: C
✅ Correct!

--- Quiz Finished! ---
Final Score: 4 out of 4

📍 Future Improvements

Add difficulty levels

Store scores in a file

Add timer per question

Add GUI interface using Tkinter or PyQt

🎯 Purpose of the Project

This project is designed for beginners to understand:

Python user input handling

Working with built-in modules

Control flow and validation  

submitted by : 

Aashirvad Mishra

registration no : 25BAI11488
