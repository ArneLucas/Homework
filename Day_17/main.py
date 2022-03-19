from question_model import Question
from quiz_brain import QuizBrain

category = ""
difficulty = ""

# LATER: use https://opentdb.com/api_category.php to find all categories & corresponding category-numbers

category_choice = input("Music/sports? ").lower
if category_choice == "music":
    category = "12"
if category_choice == "sports":
    category = "21"

difficulty_choice = input("Easy/medium/hard? ").lower
if difficulty_choice == "easy":
    difficulty = "easy"
if difficulty_choice == "medium":
    difficulty = "medium"
if difficulty_choice == "hard":
    difficulty = "hard"

number_of_questions = input("How many questions do you want to play? ") # LATER: https://opentdb.com/api_count.php?category=CATEGORY_ID_HERE shows max number available questions

import urllib.request, json 
with urllib.request.urlopen(f"https://opentdb.com/api.php?amount={number_of_questions}&category={category}&difficulty={difficulty}&type=boolean") as url:
    data = json.loads(url.read().decode())

opentdb_results = data["results"]

question_bank = []

for question in opentdb_results:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()
else:
    print("\n")
    print("You've completed the quiz")
    print(f"Your final score was {quiz.score}/{len(quiz.question_list)}")