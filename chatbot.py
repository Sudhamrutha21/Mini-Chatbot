from responses import get_response

def start_chatbot():
    print("Chatbot: Hello! Type 'exit' to end the chat.")

    while True:
        user_input = input("You: ")

        response = get_response(user_input)
        print("Chatbot:", response)

        if user_input.lower() in ["exit", "bye", "quit"]:
            break


if __name__ == "__main__":
    start_chatbot()
