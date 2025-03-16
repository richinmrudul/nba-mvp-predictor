import pickle

with open("mvp_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model saved successfully!")
