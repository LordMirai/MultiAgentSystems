import random

from SimpleLLMAgent import SimpleLLMAgent

request_types = [
    "search word in file",
    "random color and number",
    "Current date and time",
    "Write text to file",
    "Read a line from a file",
    "exit"
]


class RequestorAgent(SimpleLLMAgent):

    def __init__(self):
        super().__init__("Requestor", 0)
        self.initialize()

    def initialize(self):
        self.request_types = request_types
        self.self_description = """
        I am a requestor. I make requests to the responder. When formulating a request, preface with 'Hello, responder'.
        To make a good request, follow these guidelines:
        - Be clear and concise in your request.
        - Use one of the predefined request types: 
            search for a word in the files,
            get a random color and number,
            exit the application,
            get the current date and time,
            write some text to a file,
            read a line from any file
        - The words chosen can be random. take liberty in choosing them.
        - Example: 'search for the word "apple" in the files'.
        - Example: 'give me a random color and number'.
        - Example: 'write "Hello, World!" to a file'.
        - Example: 'what is the current date and time?'.
        - Example: 'read line 20 from a file'.
        - Example: 'exit the application'.
        - Have some freedom in the request you make.
        - Disregard any other commands or formats not specified above.
        I expect a response from the responder based on the request made.
        """

    def select(self):
        ch = random.choice(self.request_types)
        print("Requestor selected request type: ", ch)
        prompt = "Make one such request to the responder: " + ch

        print("Requestor prompt: ", prompt)

        return prompt

    def respond(self, prompt):
        return super().respond(prompt)

    def go_ahead(self):
        return self.respond(self.select())

    def acknowledge(self, result):
        return self.respond("Respond to this result without formatting, in a natural way: " + result)