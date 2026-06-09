from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0"
)

print("Chatbot Started")
print("Type 'exit' to quit")

while True:
    user = input("\nYou: ")

    if user.lower() == "exit":
        break

    prompt = f"<|user|>\n{user}\n<|assistant|>\n"

    response = generator(
        prompt,
        max_new_tokens=100,
        do_sample=True,
        temperature=0.7,
        return_full_text=False
    )

    print("\nBot:", response[0]["generated_text"])