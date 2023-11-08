class AdvancedChatbot:
    def __init__(self):
        self.responses = {
            "hello": "Hello! How can I assist you today?",
            "problem": "I'm sorry to hear you're facing an issue. Please describe it, and I'll do my best to help.",
            "goodbye": "Goodbye! If you have more questions, feel free to ask.",
            "help": "I can assist with a variety of tasks. You can ask about common issues, software features, or even tell a joke.",
            "joke": "Sure, here's a joke: Why did the software developer go broke? Because he used up all his cache!",
            "features": "Our software includes features like automated code reviews, predictive analytics, NLP analysis, and chatbot integration.",
            "default": "I'm not sure how to respond to that. Feel free to ask anything else."
        }
        self.conversations = []

    def get_response(self, user_input):
        user_input = user_input.lower()
        response = self.responses.get(user_input, self.responses["default"])
        self.conversations.append({"user": user_input, "chatbot": response})
        return response

    def get_conversation_history(self):
        return self.conversations

    def add_custom_response(self, keyword, custom_response):
        self.responses[keyword] = custom_response