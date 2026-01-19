print("🤖 Chatbot: Hello! I am a simple chatbot.")
print("Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("🤖 Chatbot: Hello! How can I help you?")

    elif "how are you" in user_input:
        print("🤖 Chatbot: I am fine. Thank you for asking!")

    elif "your name" in user_input:
        print("🤖 Chatbot: My name is PythonBot.")

    elif "help" in user_input:
        print("🤖 Chatbot: I can answer simple questions like greetings and my name.")

    elif user_input == "bye":
        print("🤖 Chatbot: Goodbye! Have a nice day 😊")
        break

    else:
        print("🤖 Chatbot: Sorry, I don't understand that.")
