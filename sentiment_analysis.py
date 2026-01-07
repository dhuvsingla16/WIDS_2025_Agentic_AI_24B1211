from transformers import pipeline

# 1. Initialize the sentiment analysis pipeline
# This uses the default 'distilbert-base-uncased-finetuned-sst-2-english' model
classifier = pipeline("sentiment-analysis")

# 2. Define a list of five movie reviews
reviews = [
    "This movie was an absolute masterpiece with stunning visuals!",
    "I found the plot to be quite boring and predictable.",
    "The acting was top-notch, though the ending felt a bit rushed.",
    "Worst experience ever; I walked out after thirty minutes.",
    "A solid film that delivers exactly what the trailer promised."
]

# 3. Pass the entire list into the pipeline in one call
results = classifier(reviews)

# 4. Print each review with its predicted label and confidence score
print(f"{'REVIEW':<60} | {'LABEL':<10} | {'SCORE'}")
print("-" * 85)

for review, result in zip(reviews, results):
    label = result['label']
    score = round(result['score'], 4)  # Rounding for readability
    print(f"{review[:57] + '...':<60} | {label:<10} | {score}")
