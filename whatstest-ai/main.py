from app.agent import WhatsAppAgent
from app.simulator import WhatsAppSimulator
from app.validator import Validator
from app.scenarios import scenarios

agent = WhatsAppAgent()
simulator = WhatsAppSimulator(agent)
validator = Validator()

results = []

for s in scenarios:
    response = simulator.send_message(s["input"])
    result = validator.check(s["expected"], response)

    results.append({
        "input": s["input"],
        "expected": s["expected"],
        "actual": response,
        "status": "PASS" if result else "FAIL"
    })

for r in results:
    print(r)