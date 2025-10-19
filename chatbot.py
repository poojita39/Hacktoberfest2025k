import random

pairs = {
    "hello": ["Hi!", "Hello!", "Hey there!"],
    "how are you": ["I'm doing great!", "All good!", "Fantastic, thanks!"],
    "bye": ["Goodbye!", "See you soon!", "Take care!"]
}

def chatbot():
    print("Chatbot ready (type 'bye' to exit)")
    while True:
        msg = input("You: ").lower()
        if msg == "bye":
            print("Bot:", random.choice(pairs["bye"]))
            break
        found = False
        for k in pairs:
            if k in msg:
                print("Bot:", random.choice(pairs[k]))
                found = True
                break
        if not found:
            print("Bot: I didn’t understand that.")

chatbot()
