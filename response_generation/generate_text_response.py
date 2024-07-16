import google.generativeai as genai
import os

# Configure the Gemini API with your API key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

class GeminiResponseGenerator:
    def __init__(self):
        self.model_name = "gemini-1.5-pro"

    def generate_response(self, prompt):
        response = genai.generate_content(self.model_name, prompt=prompt)
        return response.text

# Example usage
if __name__ == "__main__":
    generator = GeminiResponseGenerator()
    response = generator.generate_response("User asks for account balance.")
    print(response)
