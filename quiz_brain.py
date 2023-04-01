import html

import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.high_score = self.see_high_score()
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text} (True/False): "

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            self.update_high_score(self.score)
            return True
        else:
            return False

    def see_high_score(self):
        with open("highest_score.txt", mode="r") as high_score:
            current_high_score = high_score.read()
            return int(current_high_score)

    def update_high_score(self, score):
        if score > self.see_high_score():
            with open("highest_score.txt", "w") as write_high_score:
                write_high_score.write(str(score))
