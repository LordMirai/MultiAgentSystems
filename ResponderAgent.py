from SimpleLLMAgent import SimpleLLMAgent
from tools import Tools


class ResponderAgent(SimpleLLMAgent):
    def __init__(self):
        super().__init__("Responder", 1)
        self.initialize()

    def initialize(self):
        self.self_description = """
        I am a responder. I respond to requests from the requestor.
        I must recognize and extract commands given.
        From my prompt, I will look for one of the following commands:
        - search for a word in the files,
        - get a random color and number,
        - exit the application,
        - get the current date and time,
        - write some text to a file,
        - read a line from any file
        
        Understand and simplify the prompt so that it can be executed. 
        For example 'read line 10 from a file' can be simplified to 'read line 10' => '<<READLINE>> 10'.
        
        They must then be formatted as follows:
        
        <<SEARCH>> <word>
        <<RANDCOLNUM>>
        <<DATETIME>>
        <<WRITE>> <text>
        <<READLINE>> <line number>
        <<EXIT>>
        
        Disregard any other commands.
        """

    def execute(self, prompt):
        # Utilize tools based on the prompt
        success = Tools.parse(prompt)
        if success:
            return success
        else:
            return self.respond(prompt)

    def receive(self, prompt):
        processed = self.respond(prompt)
        print("Processed: ", processed)
        return self.execute(processed)

    def acknowledge(self, result):
        return self.respond("Acknowledge this result without formatting, in a natural way: " + result)