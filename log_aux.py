import os
from datetime import datetime

from faker import Faker

fake = Faker()

class Logs:
    current_session = None
    @staticmethod
    def create_session():
        # create a file with current date and time with a session ID
        session_id = fake.uuid4()
        date_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        file_name = f"session_{date_time}_{session_id}.txt"
        if not os.path.exists('logs'):
            os.mkdir('logs')
        with open(f'logs/{file_name}', 'w') as file:
            file.write(f"Session ID: {session_id}\n")
            file.write(f"Session start: {date_time}\n")
        Logs.current_session = file_name

    @staticmethod
    def final_write(message):
        # log a message to the current session
        with open(f'logs/{Logs.current_session}', 'a') as file:
            file.write(f"{message}\n")

    @staticmethod
    def log(messages, head):
        if type(messages) is not list:
            messages = [messages]
        out_str = "\n\n".join(messages)
        if head is not None:
            out_str = f"{head}\n{out_str}"

        Logs.final_write(out_str)