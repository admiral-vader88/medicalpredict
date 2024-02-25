import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the datasets
train_df = pd.read_csv('patients_dataset.csv')
test_df = pd.read_csv('newdataset.csv')

# Preprocess the training data
X_train = train_df['Symptom']
y_train = train_df['Disease']

# Preprocess the testing data
X_test = test_df['Symptom']
y_test = test_df['Disease']

# Vectorize the text data
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train a Support Vector Machine classifier
clf = SVC(kernel='linear', probability=True)  # Use linear kernel for SVM
clf.fit(X_train_vec, y_train)

# Test the model
y_pred = clf.predict(X_test_vec)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print("Model Accuracy:", accuracy * 100)
print("Confusion Matrix:\n", conf_matrix)
print("Classification Report:\n", class_report)

# Prompt for new disease input by user
new_symptoms = input("Enter new symptoms: ")

# Predict if new disease is related to previous diseases
predicted_disease = clf.predict(vectorizer.transform([new_symptoms]))[0]

# Calculate the probability of previous disease linked to current disease
probabilities = clf.predict_proba(vectorizer.transform([new_symptoms]))
previous_disease_prob = probabilities[0][list(clf.classes_).index(predicted_disease)]

print("Predicted Disease:", predicted_disease)
print("Probability of Previous Disease Linked to Current Disease:", previous_disease_prob)
    