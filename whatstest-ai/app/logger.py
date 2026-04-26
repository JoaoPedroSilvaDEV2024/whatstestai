import json

class Logger:
    def log(self, data):
        with open("logs.json", "a") as f:
            f.write(json.dumps(data) + "\n")