from transformers import pipeline

# Load model
generator = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0"
)

print("Chatbot Started")
print("Type 'exit' to quit")

# Conversation memory
history = """
You are a helpful AI assistant.
"""

while True:
    user = input("\nYou: ")

    if user.lower() == "exit":
        print("Goodbye!")
        break

    # Add user message to memory
    history += f"\nUser: {user}\nAssistant:"

    # Generate response
    response = generator(
        history,
        max_new_tokens=100,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        return_full_text=False
    )

    answer = response[0]["generated_text"].strip()

    # Sometimes models generate extra User: tags
    if "User:" in answer:
        answer = answer.split("User:")[0].strip()

    print(f"\nBot: {answer}")

    # Save assistant response to memory
    history += f" {answer}"
    