def generate_response(user_input, tone):
    
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        if tone == "Professional":
            response = "Good day. How may I assist you today?"
            explanation = "Professional tone uses polite and formal greetings."
        else:
            response = "Hey! What's up? 😊"
            explanation = "Personal tone is casual and friendly."

    elif "how are you" in user_input:
        if tone == "Professional":
            response = "I am doing well, thank you. How may I help you?"
            explanation = "Professional tone is respectful and structured."
        else:
            response = "I'm good! How about you 😄"
            explanation = "Personal tone feels natural and relaxed."

    elif "bye" in user_input:
        if tone == "Professional":
            response = "Goodbye. Have a great day ahead."
            explanation = "Professional tone ends conversations politely."
        else:
            response = "Bye! Take care 😄"
            explanation = "Personal tone is warm and informal."

    else:
        if tone == "Professional":
            response = f"I understand your message: '{user_input}'. Let me assist you further."
            explanation = "Professional tone is clear, polite, and structured."
        else:
            response = f"Ohh got it! You said: '{user_input}' 😄"
            explanation = "Personal tone feels friendly and conversational."

    return response, explanation
