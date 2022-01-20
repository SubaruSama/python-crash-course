from tkinter.messagebox import QUESTION


class AnonymousSurvey():

    def __init__(self, question) -> None:
        """Store a question, and prepare to store responses"""
        self.question = question
        self.responses = []

    def show_question(self) -> None:
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response: str) -> None:
        """Stores a single response to the survey"""
        self.responses.append(new_response)

    def show_results(self) -> None:
        print('Survey results:')
        for response in self.responses:
            print(f'- {response}')