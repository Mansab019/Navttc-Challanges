# Task 61 - Text Processing with NLTK
# Reference: https://pythonspot.com/category/nltk/

try:
    import nltk
    nltk.download('wordnet', quiet=True)
    nltk.download('punkt', quiet=True)
    nltk.download('averaged_perceptron_tagger', quiet=True)

    from nltk.stem import WordNetLemmatizer
    from nltk.tokenize import word_tokenize
    import re

    text = "The children are running and eating while the dogs are barking loudly."

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    words = word_tokenize(text)
    lemmatized = [lemmatizer.lemmatize(w) for w in words]
    print("Lemmatized:", lemmatized)

    # POS Tagging
    pos_tags = nltk.pos_tag(words)
    print("\nPOS Tags:", pos_tags)

    # Regex - remove punctuation
    clean = re.sub(r'[^\w\s]', '', text)
    print("\nCleaned text:", clean)

    # Regex - find all words
    all_words = re.findall(r'\b\w+\b', text)
    print("\nAll words:", all_words)

except ImportError:
    print("NLTK not installed. Run: pip install nltk")
