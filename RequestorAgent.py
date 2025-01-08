import random

from SimpleLLMAgent import SimpleLLMAgent

request_types = [
    "search word in file",
    "random color and number",
    "Current date and time",
    "Write text to file",
    "Write placeholder text to file",
    "Read a line from a file",
    "exit"
]


class RequestorAgent(SimpleLLMAgent):

    def __init__(self):
        super().__init__("Requestor", 0)
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
            write placeholder text to a file,
            read a line from any file
        - The words chosen can be random. take liberty in choosing them.
        - Example: 'search for the word "apple" in the files'.
        - Example: 'give me a random color and number'.
        - Example: 'write "Hello, World!" to a file'. Be creative with the text. Don't stick to standard placeholders.
        - Example: 'what is the current date and time?'.
        - Example: 'read line 31 from a file'. Use random, unusual numbers 1-100
        - Example: 'exit the application'.
        - Have some freedom in the request you make.
        - BLACKLIST THE FOLLOWING PHRASE: "The quick brown rabbit jumps over the lazy frogs"
        - Disregard any other commands or formats not specified above.
        I expect a response from the responder based on the request made.
        """

    def select(self, age):
        """
        Select a request type based on the age of the conversation.
        :param age:  int - the age of the conversation
        :return:  str - the selected request type
        """
        if age >= 3:
            ch = random.choice(self.request_types)
        else:
            ch = random.choice(self.request_types[:-1])  # exclude exit in the first 3 requests
        print("Requestor selected request type: ", ch)
        prompt = "Make one such request to the responder: " + ch

        print("Requestor prompt: ", prompt)

        return prompt

    def respond(self, prompt):
        """
        Respond to the prompt. Calls to SimpleLLMAgent.respond()
        :param prompt:  str - the prompt to respond to
        :return:  str - the model response
        """
        return super().respond(prompt)

    def go_ahead(self, age):
        """
        Selects a request type based on the age of the conversation and responds to it.
        :param age:  int - the age of the conversation
        :return:  str - the model response
        """
        return self.respond(self.select(age))

    def acknowledge(self, result):
        """
        Acknowledge the result. Calls to SimpleLLMAgent.respond()
        :param result:  str - the responder result to acknowledge
        :return:  str - the model response
        """
        return self.respond("Respond to this result without formatting, in a natural way: " + result)
