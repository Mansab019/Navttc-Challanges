# Task 62 - Text Analysis
# Reference: https://medium.com/towards-artificial-intelligence/natural-language-processing-nlp-with-python-tutorial-for-beginners

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Sample documents
docs = [
    "I love machine learning",
    "Machine learning is amazing",
    "Deep learning is a part of machine learning",
    "Natural language processing is fun"
]

# Bag of Words
cv = CountVectorizer()
bow = cv.fit_transform(docs)
print("Vocabulary:", cv.get_feature_names_out())
print("\nBoW Matrix:\n", bow.toarray())

# TF-IDF
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(docs)
print("\nTF-IDF Features:", tfidf.get_feature_names_out())
print("\nTF-IDF Matrix:\n", tfidf_matrix.toarray().round(2))
