import os

from gui import GUI

if not __name__ == '__main__':
    print("SCRIPT RAN EXTERNALLY. TERMINATED")
    exit(0)

api_key = 'AIzaSyDw8UetLAzcVE4o9olvekJwwmWKB6hGwVI'  # I'm not gonna bother hiding this. Steal it if you want :D

os.environ['GOOGLE_API_KEY'] = api_key

from log_aux import Logs

Logs.create_session()

# requestor = RequestorAgent()
# responder = ResponderAgent()
#
# query = requestor.go_ahead()
# print("Requestor query: ", query)
#
# response = responder.receive(query)
# print("Responder response: ", response)
#
# ack = responder.acknowledge(response)
# print("Acknowledgement: ", ack)
#
# req_ack = requestor.acknowledge(ack)
# print("Requestor Acknowledgement: ", req_ack)

gui = GUI()
gui.open()
