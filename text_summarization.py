from transformers import pipeline

# Using 'facebook/bart-large-cnn' provides much better rephrasing
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

original_text = (
    "Artificial Intelligence has transformed the way we interact with technology on a daily basis. "
    "From personalized recommendations on streaming platforms to advanced diagnostic tools in healthcare, "
    "the applications of machine learning are vast and ever-expanding. However, this rapid growth "
    "also brings about significant ethical concerns regarding data privacy and algorithmic bias. "
    "Developers and policymakers must work together to ensure that AI systems are transparent, "
    "fair, and beneficial to all of society. As we move forward, the balance between innovation "
    "and regulation will be crucial for the sustainable development of these powerful tools."
)

# Adjusted parameters for better summarization:
# 1. num_beams=4: Helps the model look ahead to find better word sequences.
# 2. length_penalty=2.0: A higher value encourages the model to generate shorter summaries.
# 3. early_stopping=True: Ensures it stops once a sentence is finished.
summary_result = summarizer(
    original_text, 
    max_length=60, 
    min_length=25, 
    num_beams=4,
    length_penalty=2.0,
    early_stopping=True
)

generated_summary = summary_result[0]['summary_text']

print("-" * 50)
print(f"ORIGINAL ({len(original_text.split())} words):")
print(original_text)
print("-" * 50)
print(f"AI SUMMARY ({len(generated_summary.split())} words):")
print(generated_summary)
print("-" * 50)
