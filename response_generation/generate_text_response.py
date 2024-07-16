import google.generativeai as genai
import os

# Configure the Gemini API with your API key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

class GeminiResponseGenerator:
    def __init__(self):
        self.model_name = "gemini-1.5-pro"  # Use the model you have access to

    def generate_response(self, prompt):
        try:
            response = genai.generate_content(self.model_name, prompt=prompt)
            return response.text.strip()
        except Exception as e:
            print(f"Error during response generation: {e}")
            return "Sorry, I couldn't generate a response."

# Example usage
if __name__ == "__main__":
    generator = GeminiResponseGenerator()
    response = generator.generate_response("What is the meaning of life?")
    print(f"Generated response: {response}")
