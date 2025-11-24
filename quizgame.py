import random
import time
import sys

# A list of question dictionaries containing the question, options, and correct answer.
QUIZ_QUESTIONS = [
    {
        "q": "Which module is used to shuffle items in a list?",
        "opts": ["A. sys", "B. math", "C. random", "D. time"],
        "ans": "C"
    },
    {
        "q": "What is the result of '3' + '3' in Python?",
        "opts": ["A. 6", "B. 33", "C. 9", "D. Error"],
        "ans": "B"
    },
    {
        "q": "Which color is NOT a primary color of light?",
        "opts": ["A. Red", "B. Green", "C. Yellow", "D. Blue"],
        "ans": "C"
    },
    {
        "q": "Which built-in module allows you to introduce delays?",
        "opts": ["A. os", "B. datetime", "C. time", "D. math"],
        "ans": "C"
    }
]

def run_quiz():
    """Runs the simple interactive quiz game using 3 modules."""
    score = 0
    
    # 1. Module: random (Shuffling questions)
    random.shuffle(QUIZ_QUESTIONS)
    
    print("\n--- 🧠  Quiz Game ! ---")
    
    for i, q_data in enumerate(QUIZ_QUESTIONS):
        print(f"\nQuestion {i + 1}: {q_data['q']}")
        
        # Display options
        for option in q_data['opts']:
            print(f"  {option}")
            
        valid_answers = ['A', 'B', 'C', 'D']
        
        while True:
            user_answer = input("Your answer (A, B, C, or D): ").upper()
            
            if user_answer in valid_answers:
                break
            else:
                print("❌ Invalid input. Please enter A, B, C, or D.")

        # Check the answer
        if user_answer == q_data['ans'].upper():
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect. The answer was {q_data['ans']}")
        
        # 2. Module: time (Introduce a small delay)
        time.sleep(1.5)

    # Final Score
    print("\n--- Quiz Finished! ---")
    print(f"Final Score: **{score} out of {len(QUIZ_QUESTIONS)}**.")
    
    # 3. Module: sys (Exit the program gracefully)
    sys.exit()

if __name__ == "__main__":
    run_quiz()