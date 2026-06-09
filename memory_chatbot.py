from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="gpt2"
)

chat_history = []

print("Memory Chatbot Started")
print("Type 'exit' to quit")

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    # Save user message
    chat_history.append(f"User: {user_input}")

    # Build conversation context
    conversation = "\n".join(chat_history)

    prompt = f"""
You are a helpful AI assistant.

{conversation}

Assistant:
"""

    response = generator(
        prompt,
        max_new_tokens=80,
        do_sample=True,
        temperature=0.7,
        pad_token_id=50256
    )

    full_text = response[0]["generated_text"]

    # Extract only newly generated part
    bot_reply = full_text[len(prompt):].strip()

    print("\nBot:", bot_reply)

    # Save bot response
    chat_history.append(f"Assistant: {bot_reply}")