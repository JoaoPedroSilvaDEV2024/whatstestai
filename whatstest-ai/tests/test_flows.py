from app.agent import WhatsAppAgent

def test_basic_flow():
    agent = WhatsAppAgent()

    assert agent.respond("oi") == "Olá! Como posso te ajudar?"