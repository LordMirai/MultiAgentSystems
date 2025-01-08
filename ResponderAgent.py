from SimpleLLMAgent import SimpleLLMAgent
from tools import Tools


class ResponderAgent(SimpleLLMAgent):
    def __init__(self):
        """
        Initialize the responder agent. Set the instructions for the agent.
        This is also where we tell the agent what to look for in the prompt.
        :return:
        """
        super().__init__("Responder", 1)

        self.self_description = """
        I am a responder. I respond to requests from the requestor.
        I must recognize and extract commands given.
        From my prompt, I will look for one of the following commands:
        - search for a word in the files,
        - get a random color and number,
        - exit the application,
        - get the current date and time,
        - write some text to a file OR write placeholder text to a file,
        - read a line from any file
        
        Understand and simplify the prompt so that it can be executed. 
        For example 'read line 10 from a file' can be simplified to 'read line 10' => '<<READLINE>> 10'.
        
        They must then be formatted as follows:
        
        <<SEARCH>> <word>
        <<RANDCOLNUM>>
        <<DATETIME>>
        <<WRITE>> <text>
        <<WRITEPLACEHOLDER>>
        <<READLINE>> <line number>
        <<EXIT>>
        
        Disregard any other commands.
        """

    def execute(self, prompt):
        """
        Execute the command in the prompt.
        This calls to Tools methods.
        :param prompt:  str - the prompt to execute (plain text)
        :return:  str - the result of the execution
        """
        success = Tools.parse(prompt)
        if success:
            return success
        else:
            return self.respond(prompt)

    def receive(self, prompt):
        """
        The initial response to the request. This is where the responder first tries to understand the request.
        :param prompt: str - the prompt from the requestor
        :return:  str - the response to the requestor
        """
        processed = self.respond(prompt)
        print("Processed: ", processed)
        return self.execute(processed)

    def acknowledge(self, result):
        """
        Acknowledge the result of the execution. This is the final response to the requestor.
        :param result:  str - the result of the execution
        :return:  str - the acknowledgment of the result in a natural way
        """
        return self.respond("Acknowledge this result without formatting, in a natural way: " + result)
