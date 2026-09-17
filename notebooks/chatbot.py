# Create chatbot.py as described in Exercise 4.
import ollama

messages = []

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = ollama.chat(
        model="llama3.2:1b",
        messages=messages
    )

    bot_reply = response["message"]["content"]

    print("Bot:", bot_reply)

    messages.append({
        "role": "assistant",
        "content": bot_reply
    })