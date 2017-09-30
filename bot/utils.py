from config import CLIENT, BAD_WORDS

class MessageHandler:
    """ Handles User Messages """

    def __init__(self, message_event):
        print(message_event)
        self.sentence = message_event.get('text')
        self.channel = message_event.get("channel")
        self.sender = message_event.get("user")

        bad_words = self.filter_bad_words()
        self.handle_bad_words() if bad_words else self.parse_message()

    def parse_message(self):
        """ come up a reasonable answer to user message """
        # @todo: fetch response from api.ai

        ### Case A
        
        bot_tagged = True # @todo: validate that bot is tagged
        if bot_tagged: # echo message
            reply = self.sentence 
            CLIENT.api_call("chat.postMessage", channel=self.channel, text=reply, 
                    username='sensei', icon_emoji=':robot_face:')
    
    def filter_bad_words(self):
        sentence_tokens = self.sentence.split(" ")
        return BAD_WORDS.intersection(set(sentence_tokens))

    def handle_bad_words(self):
        reply = "Careful <@%s>, your last message contained banned words!" % self.sender
        
        CLIENT.api_call("chat.postMessage", channel=self.channel, text=reply, 
                    username='sensei', icon_emoji=':robot_face:')
        
