import requests
import os
from dotenv import load_dotenv

api_endpoint = "https://api.openai.com/v1/chat/completions"

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Start the conversation history
conversation = [
    {"role": "system", "content": "You are a helpful assistant."}
]

print("💬 Type 'exit' to end the chat.\n")

while True:
    user_input = input("🧑 You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    # Add user input to conversation
    conversation.append({"role": "user", "content": user_input})

    # Create the request
    data = {
        "model": "gpt-3.5-turbo",
        "messages": conversation,
        "max_tokens": 150,
        "temperature": 0.7,
    }

    response = requests.post(api_endpoint, headers=headers, json=data)

    if response.status_code == 200:
        response_data = response.json()
        reply = response_data['choices'][0]['message']['content'].strip()
        print(f"\n🤖 GPT: {reply}\n")

        # Add GPT's response to the conversation
        conversation.append({"role": "assistant", "content": reply})
    else:
        print(f"❌ Error: {response.status_code}")
        print(response.text)
        break