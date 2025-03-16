from fastapi import FastAPI
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open("mvp_model.pkl", "rb"))

# Define FastAPI app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "NBA MVP Predictor API is running!"}

@app.post("/predict")
def predict(player_stats: dict):
    # Convert input data into numpy array
    stats = np.array([list(player_stats.values())]).reshape(1, -1)
    
    # Predict MVP probability
    prediction = model.predict_proba(stats)[0][1]
    
    return {"MVP Probability": round(prediction, 2)}
