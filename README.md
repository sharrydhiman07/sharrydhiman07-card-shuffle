
# 🌫️ Air Quality Prediction using ML + IoT (NodeMCU)

This project predicts the **Benzene level (C6H6)** in the air using sensor data (CO, Temp, Humidity) from NodeMCU and visualizes live results using a trained ML model.

---

## 🧠 Features

- 📈 Trains a Random Forest model on UCI Air Quality dataset  
- 🧪 Predicts C6H6 (Benzene) concentration using:  
  - CO(GT)  
  - NO2(GT)  
  - Temperature (T)  
  - Relative Humidity (RH)  
- 📡 Real-time predictions using serial data from NodeMCU  
- 📊 Live graph plot of AQI + sensor values  
- 💾 Saves the trained model for future use  

---

## 🛠️ Tech Stack

- Python (Pandas, Scikit-learn, Matplotlib, Joblib)  
- C++ (Arduino with MQ-5, DHT22 on NodeMCU)  
- Hardware: NodeMCU ESP8266, MQ5, DHT22  
- IDE: Arduino + Jupyter or VS Code  

---

## 📂 Project Structure

```
air-quality-iot-ml/
├── sketch_apr12a.ino         # Arduino code for NodeMCU
├── main.py                   # Model training and saving (offline)
├── predict_realtime.py       # Live prediction & graph from NodeMCU
├── AirQuality.csv            # UCI Air Quality dataset (semicolon delimited)
├── aqi_model_rf.joblib       # Saved model (after running main.py)
```

---

## 🧪 Step-by-Step Usage

### 1. Train Model on UCI Dataset

```bash
python main.py
```

This will:
- Clean the dataset (`AirQuality.csv`)
- Train a Random Forest Regressor to predict `C6H6(GT)`
- Save the model as `aqi_model_rf.joblib`

---

### 2. Run Live Prediction

- Connect NodeMCU to COM port  
- Run the real-time script:

```bash
python predict_realtime.py
```

This will:
- Read CO, Temp, Humidity from serial
- Predict AQI (C6H6 level)
- Show real-time graph of all sensor values

---

### 3. Flash Arduino Code

- Upload `sketch_apr12a.ino` to NodeMCU using Arduino IDE  
- Ensure correct port (e.g., COM5)  
- DHT22 connected to D4, MQ-5 to A0  
- Use serial monitor to check if data is printing in format:

```
435.0,31.2,54.0
```

---

## 📈 Example Output

- CO: 435.0 ppm  
- Temp: 31.2 °C  
- Humidity: 54.0 %  
- **Predicted AQI (C6H6): 18.35 µg/m³**

---

## 🧠 Model Performance

- 🔥 R² Score: ~0.89  
- 🎯 MSE: ~6.32  
- Model used: `RandomForestRegressor(n_estimators=150, max_depth=12)`

---

## 🚀 Future Scope

- Deploy live data to Firebase / ThingSpeak  
- Add mobile dashboard via Streamlit / Flutter  
- Extend support for more pollutants (PM2.5, VOC)

---

## 📜 License

MIT © 2025 Sharry Dhiman
