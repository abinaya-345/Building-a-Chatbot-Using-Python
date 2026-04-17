print("Smart Chatbot Started")
print("Type 'bye' anytime to exit.\n")

name = ""

while True:
    user = input("You: ").lower()

    # EXIT
    if user == "bye":
        print("Bot: Goodbye! Have a great day.")
        break

    # GREETING
    elif user in ["hi", "hello", "hey"]:
        print("Bot: Hello.")
        name = input("Bot: What is your name?\nYou: ")
        print("Bot: Nice to meet you,", name)
        print("Bot: How can I help you today?")

    # ABOUT BOT
    elif "your name" in user or "who are you" in user:
        print("Bot: I am a smart AI chatbot created using Python.")

    # AI TOPIC
    elif "ai" in user:
        print("Bot: AI stands for Artificial Intelligence.")
        more = input("Bot: Do you want more details? (yes/no)\nYou: ")
        if more == "yes":
            print("Bot: AI enables machines to learn, think, and make decisions.")
        else:
            print("Bot: Okay.")

    # PYTHON
    elif "python" in user:
        print("Bot: Python is a powerful programming language.")
        learn = input("Bot: Do you want to learn Python? (yes/no)\nYou: ")
        if learn == "yes":
            print("Bot: Start with basics and then practice projects.")
        else:
            print("Bot: No problem.")

    # HEALTH
    elif "fever" in user or "sick" in user or "headache" in user:
        print("Bot: I am sorry to hear that.")
        symptoms = input("Bot: Can you describe your symptoms?\nYou: ")
        print("Bot: Please consult a doctor if symptoms continue.")
        print("Bot: Drink water and take rest.")

    # STUDY
    elif "study" in user or "exam" in user:
        print("Bot: Studying regularly is important.")
        subject = input("Bot: Which subject are you studying?\nYou: ")
        print("Bot: Focus on", subject, "and revise daily.")

    # MOTIVATION
    elif "sad" in user or "tired" in user or "motivate" in user:
        print("Bot: Do not worry, everything will be fine.")
        choice = input("Bot: Do you want a motivational quote? (yes/no)\nYou: ")
        if choice == "yes":
            print("Bot: Success starts with self-discipline.")
        else:
            print("Bot: Stay positive.")

    # PROJECT
    elif "project" in user:
        print("Bot: I can suggest some project ideas.")
        domain = input("Bot: Choose domain (AI / IoT / Web):\nYou: ").lower()

        if domain == "ai":
            print("Bot: Build AI chatbot, recommendation system, or healthcare assistant.")
        elif domain == "iot":
            print("Bot: Build smart home system or smart city model.")
        elif domain == "web":
            print("Bot: Build portfolio website or e-commerce application.")
        else:
            print("Bot: Invalid choice.")

    # JOKES
    elif "joke" in user:
        print("Bot: Why did the computer go to the doctor? Because it caught a virus.")
        again = input("Bot: Want another joke? (yes/no)\nYou: ")
        if again == "yes":
            print("Bot: Why was the computer cold? It forgot to close Windows.")
        else:
            print("Bot: Okay.")

    # WEATHER
    elif "weather" in user:
        print("Bot: I cannot check live weather, but it is good to stay prepared.")

    # TIME
    elif "time" in user:
        import datetime
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current_time)

    # DEFAULT
    else:
        print("Bot: I did not understand that.")
        help_choice = input("Bot: Do you need help? (yes/no)\nYou: ")
        if help_choice == "yes":
            print("Bot: You can ask about AI, Python, health, study, project, jokes, etc.")
        else:
            print("Bot: Okay.")