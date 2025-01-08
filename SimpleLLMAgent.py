import os

import google.generativeai as gemini
from google.ai.generativelanguage_v1beta import GenerateContentResponse


class SimpleLLMAgent:
    def __init__(self, name, index, self_description=""):
        self.name = name
        self.index = index
        self.self_description = self_description

        self.initialized = False

        gemini.configure(api_key=os.environ['GOOGLE_API_KEY'])
        self.model = gemini.GenerativeModel('gemini-1.5-flash')

        self.last_response = ""

    def respond(self, prompt):
        if not self.initialized:
            prompt = f"[[[{self.self_description}]]]\n {prompt}"
        response: GenerateContentResponse = self.model.generate_content(prompt)
        # print(response.prompt_feedback, response)

        self.initialized = True
        self.last_response = response.text
        return response.text
