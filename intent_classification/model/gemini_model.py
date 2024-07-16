import google.generativeai as genai
import os

# Configure the Gemini API with your API key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

class GeminiModel:
    def __init__(self):
        self.model_name = "gemini-1.5-pro"

    def classify_intent(self, text):
        response = genai.generate_content(self.model_name, prompt=text)
        intent = response.text
        return intent

# Example usage
if __name__ == "__main__":
    gemini_model = GeminiModel()
    intent = gemini_model.classify_intent("I want to check my account balance.")
    print(intent)
