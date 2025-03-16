from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

# Load updated dataset
df = pd.read_csv("data/processed/cleaned_data_with_team_wins.csv")

# Select new features including team wins
features = ["PTS", "REB", "AST", "STL", "BLK", "EFF", "GP", "MIN", "FG_PCT", "FT_PCT", "Wins"]
X = df[features]
y = df["MVP"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression(max_iter=1000, solver="liblinear")
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Improved Model Accuracy: {accuracy:.2f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))
