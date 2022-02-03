from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = Quizbrain(question_bank)

while quiz.still_has_questions():  # if quiz still has questions remaining:
    quiz.nexquestion()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")










# class User:
#
#         def __init__(self, user_id, username):
#             self.id = user_id
#             self.username = username
#             self.followers = 0
#             self.following = 0
#
#         def follow(self, user):
#             user.followers += 1
#             user.following += 1
#
#
# user_1 = User("001", "angela")
# user_2 = User("002", "jack")
#
# user_1.follow(user_2)
#
# print(user_1.followers)
# print(user_1.following)
#
# print(user_2.followers)
# print(user_2.following)
