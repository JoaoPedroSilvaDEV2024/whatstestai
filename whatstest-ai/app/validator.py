class Validator:
    def check(self, expected, actual):
        return expected.strip().lower() == actual.strip().lower()