# Hypothetical Gemini library usage for demonstration purposes
from gemini import Gemini

class GeminiModel:
    def __init__(self):
        self.model = Gemini.load_pretrained('gemini-base-intent')

    def classify_intent(self, text):
        intent = self.model.classify(text)
        return intent

# Example usage
if __name__ == "__main__":
    gemini_model = GeminiModel()
    intent = gemini_model.classify_intent("I want to check my account balance.")
    print(intent)
