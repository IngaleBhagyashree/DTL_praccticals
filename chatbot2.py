import random
import re

def simple_chatbot():
    """A basic chatbot using fundamental Python concepts."""

    # 1. Define responses in a dictionary
    responses = {
        "hello": ["Hi there!", "Hello!", "Greetings!"],
        "hi": ["Hi there!", "Hello!", "Greetings!"],
        "how are you": ["I'm a bot, I'm doing great!", "I'm functioning optimally."],
        "thank u":["welcomme","visit agai"],
        "what is your name": ["You can call me PyBot.", "I don't have a name, but I respond to 'Hey you!'"],
        "bye": ["Goodbye!", "See you later!", "Have a great day!"],
        "exit": ["Goodbye!", "See you later!", "Have a great day!"]
    }

    # Default responses
    default_responses = [
        "Sorry, I didn't understand that.",
        "Could you please rephrase that?",
        "I'm not sure how to respond to that."
    ]

    print("PyBot: Hi! I'm a simple chatbot. Type 'bye' or 'exit' to end the conversation.")

    # 2. Main conversation loop
    while True:
        user_input = input("You: ").lower()

        # 3. Remove punctuation
        user_input = re.sub(r'[^\w\s]', '', user_input)

        # 4. Exit condition
        if user_input in ["bye", "exit"]:
            print(f"PyBot: {random.choice(responses[user_input])}")
            break

        # 5. Keyword matching
        matched = False
        for key in responses:
            if key in user_input:
                print(f"PyBot: {random.choice(responses[key])}")
                matched = True
                break

        # 6. Default response
        if not matched:
            print(f"PyBot: {random.choice(default_responses)}")

# Run the chatbot
if __name__ == "__main__":
    simple_chatbot()
