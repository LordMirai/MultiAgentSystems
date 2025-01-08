import os

import google.generativeai as gemini
from google.ai.generativelanguage_v1beta import GenerateContentResponse


class SimpleLLMAgent:
    def __init__(self, name, index, self_description=""):
        """
        Initialize the agent. This is a Gemini AI implementation.
        This class is used as skeleton for the Requestor and Responder agents.
        :param name:  str - the name of the agent
        :param index:  int - the index of the agent (0 for Requestor, 1 for Responder)
        :param self_description:  str - the description of the agent - what it does
        """
        self.name = name
        self.index = index
        self.self_description = self_description

        self.initialized = False

        gemini.configure(api_key=os.environ['GOOGLE_API_KEY'])
        self.model = gemini.GenerativeModel('gemini-1.5-flash')

        self.last_response = ""

    def respond(self, prompt):
        """
        Respond to the prompt. This is a generic response method.
        It calls model.generate_content() to generate a response.
        If the agent is not initialized, it will preface the response with the self_description.
        :param prompt:  str - the prompt to respond to
        :return:
        """
        if not self.initialized:
            prompt = f"[[[{self.self_description}]]]\n {prompt}"
        response: GenerateContentResponse = self.model.generate_content(prompt)
        # print(response.prompt_feedback, response)

        self.initialized = True
        self.last_response = response.text
        return response.text
