from gemini import Gemini

class GeminiResponseGenerator:
    def __init__(self):
        self.model = Gemini.load_pretrained('gemini-base-response')

    def generate_response(self, prompt):
        response = self.model.generate(prompt)
        return response

# Example usage
if __name__ == "__main__":
    generator = GeminiResponseGenerator()
    response = generator.generate_response("User asks for account balance.")
    print(response)
