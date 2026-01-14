def get_response(user_input):
    user_input = user_input.lower()

    if user_input in ["hi", "hello", "hey"]:
        return "Hello! How can I help you today?"

    elif "how are you" in user_input:
        return "I'm just code, but I'm running perfectly. How about you?"

    elif "your name" in user_input:
        return "I'm a simple rule-based chatbot."

    elif "motivate" in user_input:
        return "Consistency beats talent when talent doesn’t work consistently."

    elif "help" in user_input:
        return "You can ask me simple questions or type 'exit' to quit."
    
    elif "How can you help?" in user_input:
        return "I'm a chatbot! You can chat with me."

    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye! Have a productive day."

    else:
        return "Sorry, I didn’t understand that. Try asking something else."
