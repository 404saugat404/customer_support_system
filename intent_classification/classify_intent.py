from .model.gemini_model import GeminiModel

gemini_model = GeminiModel()

def classify_intent(text):
    return gemini_model.classify_intent(text)

# Example usage
if __name__ == "__main__":
    intent = classify_intent("I want to check my account balance.")
    print(intent)
