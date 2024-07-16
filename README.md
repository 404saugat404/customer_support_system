# Customer Support System

This project is a sophisticated customer support system capable of handling both audio and text inputs from users. The system processes the input, classifies it into different intents, and provides appropriate responses in the same modality as the input (i.e., audio response for audio input, and text response for text input). The system is designed for a specific domain, such as e-commerce, banking, or telecommunications.

## Features

- **Multimodal Input Handling**: Accepts both audio and text inputs.
- **Intent Classification**: Accurately identifies the user's intent using advanced NLP techniques.
- **Response Generation**: Generates appropriate responses based on the identified intent.
- **Contextual Understanding**: Maintains the context of the conversation across multiple interactions.
- **Backend Integration**: Interfaces with relevant backend systems.
- **Error Handling**: Robust mechanisms to handle errors and escalate unresolved queries.

## Requirements

Install the required Python libraries:

```bash
pip install -r requirements.txt


Set the Google API key as an environment variable:
export GOOGLE_API_KEY=your_api_key
