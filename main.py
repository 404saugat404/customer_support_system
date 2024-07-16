from input_handling import audio_to_text, get_text_input
from intent_classification import classify_intent
from response_generation import GeminiResponseGenerator, text_to_audio
from context_management import ContextManager
from backend_integration import fetch_account_balance
from error_handling import handle_error
import os

def main():
    context_manager = ContextManager()
    response_generator = GeminiResponseGenerator()

    # Simulate input handling
    input_type = input("Enter input type (text/audio): ").strip().lower()
    print(f"Received input type: '{input_type}'")  # Debugging statement

    if input_type not in ["text", "audio"]:
        print("Invalid input type. Please enter 'text' or 'audio'.")
        return

    if input_type == "text":
        user_input = get_text_input()
    elif input_type == "audio":
        audio_file_path = input("Enter the path to the audio file: ").strip()
        user_input = audio_to_text(audio_file_path)

    # Print the user input for debugging
    print(f"User input: '{user_input}'")

    # Intent classification
    try:
        intent = classify_intent(user_input)
        print(f"Classified intent: '{intent}'")  # Debugging statement
    except Exception as e:
        print(handle_error(e))
        return

    # Context update
    user_id = "user123"
    context_manager.update_context(user_id, "last_intent", intent)

    # Fetch data from backend if needed
    if intent == "account_balance":
        try:
            account_balance = fetch_account_balance(user_id)
            response_text = f"Your account balance is {account_balance}."
        except Exception as e:
            response_text = handle_error(e)
    else:
        response_text = response_generator.generate_response(user_input)

    # Print response for debugging
    print(f"Response text: '{response_text}'")

    # Generate response in the same modality as the input
    if input_type == "text":
        print(response_text)
    elif input_type == "audio":
        text_to_audio(response_text, "response_audio.mp3")
        os.system("start response_audio.mp3")

if __name__ == "__main__":
    main()
