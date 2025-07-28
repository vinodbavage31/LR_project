import numpy as np
import pickle
from sklearn.linear_model import LinearRegression


np.random.seed(42)
X = np.random.rand(100, 1) * 10 
y = 5 * X + 3 + np.random.randn(100, 1)  

# Train model
model = LinearRegression()
model.fit(X, y)

# Save the model
with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved at model/model.pkl")
