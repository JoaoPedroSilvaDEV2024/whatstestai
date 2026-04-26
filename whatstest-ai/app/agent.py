class WhatsAppAgent:
    def respond(self, message: str):
        message = message.lower()

        if "preço" in message:
            return "Nosso plano custa R$ 49,90"
        elif "suporte" in message:
            return "Vou te ajudar com isso"
        elif "oi" in message:
            return "Olá! Como posso te ajudar?"
        else:
            return "Não entendi, pode reformular?"