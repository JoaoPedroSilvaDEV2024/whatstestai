class WhatsAppSimulator:
    def __init__(self, agent):
        self.agent = agent

    def send_message(self, message):
        response = self.agent.respond(message)
        return response