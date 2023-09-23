import random

class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def load_questions(self):

        self.questions = [
            {
                'question': 'What is the capital of France?',
                'choices': ['A. London', 'B. Paris', 'C. Rome'],
                'answer': 'B'
            },
            {
                'question': 'What is 7 + 3?',
                'choices': ['A. 10', 'B. 12', 'C. 14'],
                'answer': 'A'
            },

        ]

    def display_welcome_message(self):
        print("Welcome to the Quiz Game!")
        print("Answer the following questions. Let's see how well you know!")

    def ask_question(self, question):
        print(question['question'])
        for choice in question['choices']:
            print(choice)

        user_answer = input("Enter your answer (A/B/C): ").upper()
        return user_answer

    def evaluate_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {correct_answer}.")

    def play_again(self):
        play_again = input("Do you want to play again? (yes/no): ").lower()
        return play_again == 'yes'

    def start_game(self):
        self.load_questions()
        self.display_welcome_message()

        while True:
            random.shuffle(self.questions)

            for question in self.questions:
                user_answer = self.ask_question(question)
                self.evaluate_answer(user_answer, question['answer'])

            print(f"Your final score is: {self.score}/{len(self.questions)}")

            if not self.play_again():
                break

if __name__ == "__main__":
    quiz = Quiz()
    quiz.start_game()
