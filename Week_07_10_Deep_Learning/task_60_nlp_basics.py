# Task 60 - NLP with Python
# Reference: https://medium.com/towards-artificial-intelligence/natural-language-processing-nlp-with-python-tutorial-for-beginners

try:
    import nltk
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
    nltk.download('averaged_perceptron_tagger', quiet=True)

    from nltk.tokenize import word_tokenize, sent_tokenize
    from nltk.corpus import stopwords
    from nltk.stem import PorterStemmer

    text = "Natural Language Processing is a field of Artificial Intelligence. It helps computers understand human language."

    # Sentence tokenization
    sentences = sent_tokenize(text)
    print("Sentences:", sentences)

    # Word tokenization
    words = word_tokenize(text)
    print("\nWords:", words)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered = [w for w in words if w.lower() not in stop_words]
    print("\nFiltered:", filtered)

    # Stemming
    stemmer = PorterStemmer()
    stemmed = [stemmer.stem(w) for w in filtered]
    print("\nStemmed:", stemmed)

except ImportError:
    print("NLTK not installed. Run: pip install nltk")
