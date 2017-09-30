# local
from config import SLACK_EVENTS_ADAPTER
from utils import MessageHandler


# Example responder to greetings
@SLACK_EVENTS_ADAPTER.on("message")
def handle_message(event_data):
    message = event_data["event"]
    if message.get("subtype") is None:
        MessageHandler(message)


SLACK_EVENTS_ADAPTER.start(port=3000)
