import tkinter as tk
from time import sleep

turn_order = [0, 1, 2, 3, 4]
current_turn = 0  # 0 is the human's turn


def finish_turn():
    global current_turn
    current_turn = (current_turn + 1) % len(turn_order)


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gemini AI. Conversation between agents")
        self.root.geometry("800x600")

        self.root.bind("<Escape>", lambda _: self.root.quit())

        self.inst = tk.StringVar()
        self.inst.set("Type a message and press Enter to send")
        self.instructions = tk.Label(self.root, textvariable=self.inst)
        self.instructions.pack()

        self.rich_text = tk.Text(self.root)
        self.rich_text.pack(fill=tk.BOTH, expand=True)

        self.entry = tk.Entry(self.root)
        self.entry.pack(fill=tk.X)
        self.entry.bind("<Return>", self.on_enter)

        self.advance_btn = tk.Button(self.root, text="Advance", command=self.progress)
        self.advance_btn.pack()

        self.agents = []

        self.command_queue = []
        self.last_prompt = ""

    def on_enter(self, _):
        text = self.entry.get()
        self.entry.delete(0, tk.END)
        self.command_queue.append(("You", text))
        self.last_prompt = text

        finish_turn()
        self.progress()

    def update(self):
        if self.command_queue:
            command = self.command_queue.pop(0)
            if command[0] == "<<INST>>":
                self.inst.set(command[1])
            else:
                self.rich_text.insert(tk.END, f"{command[0]}: {command[1]}\n")
        self.root.after(50, self.update)

    def open(self):
        self.root.after(50, self.update)
        self.root.mainloop()

    def progress(self):
        # progress the conversation
        if current_turn == 0:
            self.command_queue.append(("<<INST>>", f"It's your turn!"))

        if self.last_prompt != "":
            self.command_queue.append(("<<INST>>", f"It's {self.agents[turn_order[current_turn]].name}'s turn!"))
            response = self.agents[turn_order[current_turn]].respond(self.last_prompt)
            self.command_queue.append((self.agents[turn_order[current_turn]].name, response))
            self.last_prompt = response
            finish_turn()
