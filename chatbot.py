from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="gpt2"
)

print("Chatbot Started")
print("Type 'exit' to quit")

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    response = generator(
        user_input,
        max_new_tokens=100,
        do_sample=True,
        temperature=0.7
    )

    print("\nBot:")
    print(response[0]["generated_text"])