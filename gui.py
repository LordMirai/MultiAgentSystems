import tkinter as tk

from RequestorAgent import RequestorAgent
from ResponderAgent import ResponderAgent
from log_aux import Logs


class GUI:
    def __init__(self):
        """
        Initialize the GUI. This is a simple GUI, which has a text area for displaying the conversation.
        The conversation is between two agents, the Requestor and the Responder.
        The user controls the conversation by clicking the 'Make conversation' button.
        """
        self.convo_index = 1
        # conversation index ("age"). If < 5, the requestor will not include 'exit' in the request pool.

        self.root = tk.Tk()
        self.root.title("Gemini AI. Conversation between agents with internal tool call")
        self.root.geometry("800x600")

        self.root.iconbitmap('icon.ico')

        self.root.bind("<Escape>", lambda _: self.root.quit())

        self.inst = tk.StringVar()
        self.inst.set("Press 'Make conversation' to start")
        self.instructions = tk.Label(self.root, textvariable=self.inst)
        self.instructions.pack()

        self.rich_text = tk.Text(self.root)
        self.rich_text.pack(fill=tk.BOTH, expand=True)

        self.make_conversation_btn = tk.Button(self.root, text="Make conversation", command=self.make_conversation)
        self.make_conversation_btn.pack()

        self.requestor = RequestorAgent()
        self.responder = ResponderAgent()

    def make_conversation(self):
        """
        Make a conversation between the agents. This is a four-step process:
        1. Requestor makes a request
            e.g. "Hello, responder. Search for the word 'apple' in the files"
        2. Responder receives the request and processes it
            e.g. "Searching for: apple"
            This is also where the responder will call the tools to execute the command.
            In console, it's printed like <<SEARCH>> apple - which is the command to be executed.
        3. Responder responds to the request. Also known as acknowledgement
            e.g. "Found in files/file.txt at line 10: This is an apple"
        4. Requestor acknowledges the response. The result is analyzed and acknowledged in a natural way.
            e.g. "Ah I see. You found an apple in the file. Thanks for the information."
        :return:
        """

        head = f"------Conversation {self.convo_index}-----"
        self.rich_text.insert(tk.END, head + "\n")

        query = self.requestor.go_ahead(self.convo_index)
        self.rich_text.insert(tk.END, f"Requestor query: {query}\n")

        response = self.responder.receive(query)
        self.rich_text.insert(tk.END, f"Responder response: {response}\n")

        ack = self.responder.acknowledge(response)
        self.rich_text.insert(tk.END, f"Acknowledgement: {ack}\n")

        req_ack = self.requestor.acknowledge(ack)
        self.rich_text.insert(tk.END, f"Requestor Acknowledgement: {req_ack}\n")

        batch = [query, response, ack, req_ack]
        Logs.log(batch, head)

        self.requestor.initialized = False
        self.responder.initialized = False
        # we want to reset them so that the next conversation is fresh.
        # If we don't reset, it might quickly degenerate into something unusable.

        self.convo_index += 1

    def open(self):
        """
        Actually opens the GUI.
        :return:
        """
        self.root.mainloop()
