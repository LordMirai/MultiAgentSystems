# Gemini AI Conversation Agents

**Author**: Mezdrea Constantin

**Alias**: Mirai

**GitHub**: [LordMirai](https://github.com/LordMirai)

---

## Project Overview

This project implements a conversation between two AI agents, the Requestor and the Responder, using a simple GUI. The agents communicate by making and responding to requests, which are processed using internal tools.
The requestor is given a pool of requests to choose from, and the responder is given a pool of responses to choose from.
The responder then executes the evaluated prompt (internal tools) and returns the result to the requestor.


## Project Structure

- `driver.py`: The main entry point of the application. It initializes the GUI and sets up the environment.
- `gui.py`: Defines the GUI for the application using Tkinter. It manages the conversation between the Requestor and Responder agents.
- `RequestorAgent.py`: Defines the Requestor agent, which makes requests to the Responder.
- `ResponderAgent.py`: Defines the Responder agent, which processes requests from the Requestor.
- `SimpleLLMAgent.py`: A base class for the Requestor and Responder agents, implementing the core functionality using Gemini AI.
- `tools.py`: Contains utility functions for parsing and executing commands.
- `auxiliaries.py`: Contains setup and testing utilities.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/LordMirai/MultiAgentSystems.git
    cd MultiAgentSystems
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Set up the environment variable for the Google API key:
    ```sh
    export GOOGLE_API_KEY='your_api_key_here'
    ```

## Usage

Environment: Python 3.13.1 (venv)

To run the application, execute the `driver.py` script from within virtual environment or through PyCharm:
```sh
py driver.py