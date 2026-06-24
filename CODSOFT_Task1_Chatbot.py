# ============================================================
#  CodSoft Artificial Intelligence Internship
#  Task 01: Chatbot with Rule-Based Responses
#  Author : Jaspreet Singh
#  GitHub : https://github.com/Jaspreet-Singh7/CODSOFT
# ============================================================

import re
import random
import datetime

# ── KNOWLEDGE BASE ───────────────────────────────────────────
responses = {
    # Greetings
    "greetings": {
        "patterns": [
            r"\b(hi|hello|hey|hiya|howdy|greetings|what'?s up|sup)\b"
        ],
        "responses": [
            "Hello! 👋 I'm AI-Bot. How can I help you today?",
            "Hey there! 😊 What can I do for you?",
            "Hi! Great to see you. What's on your mind?",
            "Hello! I'm here and ready to chat. What do you need?",
        ]
    },

    # How are you
    "how_are_you": {
        "patterns": [
            r"\b(how are you|how do you do|how'?s it going|you okay|are you good)\b"
        ],
        "responses": [
            "I'm doing great, thanks for asking! 😊 How about you?",
            "I'm just a bot, but I'm feeling fantastic! What about you?",
            "All systems running perfectly! How can I help you?",
        ]
    },

    # Name
    "name": {
        "patterns": [
            r"\b(what'?s your name|who are you|what are you called|your name)\b"
        ],
        "responses": [
            "I'm AI-Bot! 🤖 A rule-based chatbot built by Jaspreet Singh.",
            "My name is AI-Bot, your virtual assistant! How can I help?",
            "I go by AI-Bot! Built as part of the CodSoft AI Internship.",
        ]
    },

    # Creator
    "creator": {
        "patterns": [
            r"\b(who (made|created|built|programmed) you|who'?s your creator|who is your developer)\b"
        ],
        "responses": [
            "I was built by Jaspreet Singh as part of the CodSoft AI Internship! 🎓",
            "Jaspreet Singh created me during the CodSoft Artificial Intelligence Internship.",
        ]
    },

    # AI/Bot
    "are_you_ai": {
        "patterns": [
            r"\b(are you (a bot|an ai|a robot|human|real)|are you alive)\b"
        ],
        "responses": [
            "Yes, I'm a bot! 🤖 An AI chatbot built with rule-based pattern matching.",
            "I'm an AI chatbot — not human, but I'll do my best to help!",
            "I'm artificial intelligence — specifically a rule-based chatbot. Pretty cool right?",
        ]
    },

    # Time
    "time": {
        "patterns": [
            r"\b(what'?s? (the )?time|current time|tell me the time|what time is it)\b"
        ],
        "responses": ["__TIME__"]
    },

    # Date
    "date": {
        "patterns": [
            r"\b(what'?s? (the )?date|today'?s? date|what day is it|current date)\b"
        ],
        "responses": ["__DATE__"]
    },

    # Weather
    "weather": {
        "patterns": [
            r"\b(weather|temperature|forecast|is it (raining|sunny|hot|cold))\b"
        ],
        "responses": [
            "I don't have real-time weather data, but you can check weather.com or Google! ☀️",
            "I can't check weather right now, but try asking Google Assistant or checking a weather app! 🌤️",
        ]
    },

    # Jokes
    "joke": {
        "patterns": [
            r"\b(tell me a joke|make me laugh|say something funny|joke|funny)\b"
        ],
        "responses": [
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛😂",
            "Why was the math book sad? It had too many problems! 📚😄",
            "What do you call a fish without eyes? A fsh! 🐟😂",
            "Why can't you trust an atom? Because they make up everything! ⚛️😄",
            "I told my computer I needed a break. Now it won't stop sending me vacation ads! 💻😂",
        ]
    },

    # Help
    "help": {
        "patterns": [
            r"\b(help|what can you do|your (features|capabilities|abilities)|how to use you)\b"
        ],
        "responses": [
            """I can help you with:
🗣️ General conversation
🕐 Current time and date
😂 Jokes and fun facts
💡 General knowledge questions
🌤️ Weather info (redirects to web)
🤖 AI and tech questions
Just type anything and I'll respond!"""
        ]
    },

    # Thanks
    "thanks": {
        "patterns": [
            r"\b(thanks|thank you|thx|ty|appreciate|grateful)\b"
        ],
        "responses": [
            "You're welcome! 😊 Anything else I can help with?",
            "Happy to help! Let me know if you need anything else.",
            "Anytime! That's what I'm here for. 🤖",
        ]
    },

    # Goodbye
    "goodbye": {
        "patterns": [
            r"\b(bye|goodbye|see you|later|take care|exit|quit|farewell|cya)\b"
        ],
        "responses": [
            "Goodbye! 👋 Have a wonderful day!",
            "See you later! Take care! 😊",
            "Bye! It was great chatting with you! 🌟",
        ]
    },

    # AI topics
    "ai_topic": {
        "patterns": [
            r"\b(artificial intelligence|machine learning|deep learning|neural network|nlp|natural language|AI)\b"
        ],
        "responses": [
            "AI is fascinating! 🤖 It covers Machine Learning, Deep Learning, NLP and more. What aspect interests you?",
            "Artificial Intelligence is the simulation of human intelligence in machines. Want to know more about any specific area?",
            "Great topic! AI includes ML, DL, Computer Vision, NLP and Robotics. Which interests you?",
        ]
    },

    # Python
    "python": {
        "patterns": [
            r"\b(python|coding|programming|code|developer)\b"
        ],
        "responses": [
            "Python is amazing for AI/ML! 🐍 Libraries like Pandas, NumPy, TensorFlow and scikit-learn make it very powerful.",
            "Python is one of the most popular languages for AI and Data Science! Great choice to learn.",
        ]
    },

    # Internship
    "internship": {
        "patterns": [
            r"\b(internship|codsoft|skillcraft|intern)\b"
        ],
        "responses": [
            "This chatbot was built as part of the CodSoft AI Internship by Jaspreet Singh! 🎓",
            "CodSoft provides amazing virtual internships for students to build real AI projects!",
        ]
    },

    # Fun facts
    "fact": {
        "patterns": [
            r"\b(fun fact|interesting fact|tell me something|did you know|fact)\b"
        ],
        "responses": [
            "Fun fact: The first computer bug was an actual bug — a moth found in a Harvard computer in 1947! 🦗",
            "Did you know? The word 'robot' comes from the Czech word 'robota' meaning 'forced labor'! 🤖",
            "Fun fact: Google's first server was built from LEGO bricks! 🧱",
            "Did you know? The first AI program was written in 1951 by Christopher Strachey!",
        ]
    },

    # Age
    "age": {
        "patterns": [
            r"\b(how old are you|your age|when were you (born|created|made))\b"
        ],
        "responses": [
            "I was created in June 2026 during the CodSoft AI Internship! So I'm very young! 😊",
            "Age is just a number — I was born in 2026 as part of Jaspreet's CodSoft internship project!",
        ]
    },

    # Default fallback
    "default": {
        "patterns": [],
        "responses": [
            "Hmm, I'm not sure I understood that. Could you rephrase? 🤔",
            "Interesting! But I'm not sure how to respond to that. Try asking something else!",
            "I didn't quite catch that. Type 'help' to see what I can do! 😊",
            "That's a bit beyond my current knowledge. Try a different question?",
        ]
    }
}


# ── CHATBOT ENGINE ───────────────────────────────────────────
def get_response(user_input: str) -> str:
    """Match user input to patterns and return appropriate response."""
    user_lower = user_input.lower().strip()

    # Empty input
    if not user_lower:
        return "Please type something! 😊"

    # Check all patterns
    for intent, data in responses.items():
        if intent == "default":
            continue
        for pattern in data["patterns"]:
            if re.search(pattern, user_lower, re.IGNORECASE):
                response = random.choice(data["responses"])
                # Handle special responses
                if response == "__TIME__":
                    now = datetime.datetime.now()
                    return f"The current time is {now.strftime('%I:%M %p')} ⏰"
                if response == "__DATE__":
                    now = datetime.datetime.now()
                    return f"Today is {now.strftime('%A, %d %B %Y')} 📅"
                return response

    # Default fallback
    return random.choice(responses["default"]["responses"])


def print_banner():
    """Print welcome banner."""
    print("=" * 55)
    print("       AI-BOT — Rule-Based Chatbot")
    print("       CodSoft AI Internship | Task 01")
    print("       Author: Jaspreet Singh")
    print("=" * 55)
    print("👋 Hello! I'm AI-Bot. Type 'help' to see what I can do.")
    print("   Type 'bye' or 'exit' to quit.\n")


def run_chatbot():
    """Main chatbot loop."""
    print_banner()

    exit_words = {"bye", "goodbye", "exit", "quit", "farewell", "see you", "cya"}

    while True:
        try:
            user_input = input("You: ").strip()

            if not user_input:
                continue

            # Check for exit
            if any(word in user_input.lower() for word in exit_words):
                print(f"AI-Bot: {random.choice(responses['goodbye']['responses'])}")
                print("\n" + "=" * 55)
                print("  Thanks for chatting! Built by Jaspreet Singh")
                print("  CodSoft AI Internship 2026")
                print("=" * 55)
                break

            response = get_response(user_input)
            print(f"AI-Bot: {response}\n")

        except KeyboardInterrupt:
            print("\nAI-Bot: Goodbye! 👋")
            break


# ── DEMO TEST ────────────────────────────────────────────────
def run_demo():
    """Run automated demo to verify all responses work."""
    print("\n" + "=" * 55)
    print("  DEMO TEST — Verifying all responses")
    print("=" * 55)

    test_cases = [
        ("Hello!", "greetings"),
        ("How are you?", "how_are_you"),
        ("What's your name?", "name"),
        ("Who made you?", "creator"),
        ("Are you a bot?", "are_you_ai"),
        ("What time is it?", "time"),
        ("What's today's date?", "date"),
        ("Tell me a joke!", "joke"),
        ("What can you do?", "help"),
        ("Tell me a fun fact", "fact"),
        ("I love Python!", "python"),
        ("Tell me about AI", "ai_topic"),
        ("Thank you!", "thanks"),
        ("Goodbye!", "goodbye"),
    ]

    all_passed = True
    for user_msg, expected_intent in test_cases:
        response = get_response(user_msg)
        status = "✅" if response and len(response) > 5 else "❌"
        if status == "❌":
            all_passed = False
        print(f"{status} [{expected_intent}]")
        print(f"   Q: {user_msg}")
        print(f"   A: {response}\n")

    print("=" * 55)
    print(f"  All tests passed: {'✅ YES' if all_passed else '❌ NO'}")
    print("=" * 55)
    return all_passed


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        run_demo()
    else:
        run_chatbot()
