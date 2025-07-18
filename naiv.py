# Import libraries
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# 1. Sample dataset
texts = [
    "Congratulations! You've won a free ticket!",
    "Hello, how are you doing today?",
    "Win money now, click here!",
    "Are we still meeting for lunch?",
    "Exclusive deal just for you, claim now!",
    "Can you send me the report?",
    "Get a free entry to the contest now!",
    "Let's catch up later today.",
    "Special promotion just for you!",
    "Don't forget about the meeting tomorrow."
]
labels = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]  # 1 = spam, 0 = not spam

# 2. Convert text data to numeric vectors
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# 3. Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.3, random_state=42)

# 4. Train Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train, y_train)

# 5. Predict on test data
y_pred = model.predict(X_test)

# 6. Show results
print("Predicted labels:", y_pred)
print("Actual labels:", y_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# 7. Test custom messages
sample_messages = [
    "Congratulations, you have won a free prize!",
    "Hey, are we meeting tomorrow?"
]
sample_vectors = vectorizer.transform(sample_messages)
predictions = model.predict(sample_vectors)

print("\nCustom predictions:")
for msg, label in zip(sample_messages, predictions):
    print(f"Message: {msg} => {'Spam' if label == 1 else 'Not Spam'}")
