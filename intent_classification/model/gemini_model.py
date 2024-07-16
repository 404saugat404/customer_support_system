import google.generativeai as genai
import os

# Configure the Gemini API with your API key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

class GeminiModel:
    def __init__(self):
        self.model_name = "gemini-1.5-pro"  # Use the model you have access to

    def classify_intent(self, text):
        try:
            response = genai.generate_content(self.model_name, prompt=text)
            intent = response.text.strip()
            return intent
        except Exception as e:
            print(f"Error during intent classification: {e}")
            return "unknown_intent"

# Example usage
if __name__ == "__main__":
    gemini_model = GeminiModel()
    intent = gemini_model.classify_intent("I want to check my account balance.")
    print(f"Classified intent: {intent}")
