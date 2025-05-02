import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# === STEP 1: Load the dataset ===
csv_file = "AirQuality.csv"
df = pd.read_csv(csv_file, sep=';', decimal=',')

print("📊 Original shape:", df.shape)

# === STEP 2: Replace -200 with NaN ===
df.replace(-200, np.nan, inplace=True)

# === STEP 3: Fill missing values with column means ===
df.fillna(df.mean(numeric_only=True), inplace=True)
print("✅ After filling missing values:", df.shape)

# === STEP 4: Select features and target ===
features = ["CO(GT)", "NO2(GT)", "T", "RH"]
target = "C6H6(GT)"

X = df[features]
y = df[target]

# === STEP 5: Split data ===
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# === STEP 6: Train the model ===
model = RandomForestRegressor(n_estimators=150, max_depth=12, random_state=42)
model.fit(X_train, y_train)

# === STEP 7: Evaluate ===
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"🎯 Improved MSE: {mse:.2f}")
print(f"📈 R² Score: {r2:.4f}")

# === STEP 8: Save the model ===
joblib.dump(model, "aqi_model_rf.joblib")
print("💾 Model saved as 'aqi_model_rf.joblib'")

# === STEP 9: Simulate a prediction ===
example_input = [[2.5, 40, 21.3, 48.0]]
predicted_aqi = model.predict(example_input)[0]
print(f"🧠 Example Prediction: AQI (C6H6) ≈ {predicted_aqi:.2f}")
