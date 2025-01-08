from time import sleep
from gui import GUI
from threading import Thread

from google.ai.generativelanguage_v1beta import GenerateContentResponse

if not __name__ == '__main__':
    print("SCRIPT RAN EXTERNALLY. TERMINATED")
    exit(0)

api_key = r'AIzaSyDw8UetLAzcVE4o9olvekJwwmWKB6hGwVI'

import os
import google.generativeai as gemini

# Set your Google Gemini API key
os.environ['GOOGLE_API_KEY'] = api_key

# Initialize the Google Gemini LLM
gemini.configure(api_key=os.environ['GOOGLE_API_KEY'])


# Define a simple agent
class SimpleLLMAgent:
    def __init__(self, name, index, self_description):
        self.name = name
        self.index = index
        self.self_description = self_description

        self.initialized = False

        self.model = gemini.GenerativeModel('gemini-1.5-flash')

    def respond(self, prompt):
        if not self.initialized:
            prompt = "[[[You are an AI assistant. This is how you act normally: " + self.self_description + "]]]\n" + prompt
        response: GenerateContentResponse = self.model.generate_content(prompt)
        # print(response.prompt_feedback, response)
        return response.text


desc1 = "Professional, serious, unemotional. Your responses are clinical"
desc2 = "Bright, happy, cheerful. Your responses are upbeat and positive"
desc3 = "Sarcastic, snarky, witty. Your responses are clever and funny"
desc4 = "Silient, antisocial. You don't like talking to people."

agents = [
    SimpleLLMAgent("Professional", 1, desc1),
    SimpleLLMAgent("Bright", 2, desc2),
    SimpleLLMAgent("Sarcastic", 3, desc3),
    SimpleLLMAgent("Silent", 4, desc4)
]






gui = GUI()
gui.agents = agents

gui.open()