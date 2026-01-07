from transformers import pipeline

generator = pipeline("text-generation", model="Qwen/Qwen2.5-0.5B")


prompt = "In 2030, AI systems will"


# max_new_tokens=50: Generates up to 50 additional words/tokens
# num_return_sequences=2: Tells the model to give us two different variations
# do_sample=True: Adds randomness so the two versions aren't identical
results = generator(
    prompt, 
    num_return_sequences=2, 
    max_new_tokens=50, 
    do_sample=True
)


print("PROMPT:", prompt)
print("-" * 50)

for i, output in enumerate(results):
    print(f"GENERATION {i+1}:")
    print(output['generated_text'])
    print(f"Length: {len(output['generated_text'])} characters")
    print("-" * 50)
