import serial
import joblib
import time
import pandas as pd
import matplotlib.pyplot as plt
from collections import deque

# === Load model ===
model = joblib.load("aqi_model_rf.joblib")

# === Serial port ===
ser = serial.Serial('COM5', 9600)
time.sleep(2)
print("📡 Listening to NodeMCU...")

# === Graph setup ===
plt.ion()
fig, ax = plt.subplots()
max_len = 50

# Rolling data
timestamps = deque(maxlen=max_len)
aqi_vals = deque(maxlen=max_len)
gas_vals = deque(maxlen=max_len)
temp_vals = deque(maxlen=max_len)
hum_vals = deque(maxlen=max_len)

# Plot lines
line_aqi, = ax.plot([], [], label="Predicted AQI", color="red")
line_gas, = ax.plot([], [], label="CO (MQ-5)", color="blue")
line_temp, = ax.plot([], [], label="Temp (°C)", color="orange")
line_hum, = ax.plot([], [], label="Humidity (%)", color="green")

ax.set_ylim(0, 150)
ax.set_title("Real-Time AQI & Sensor Readings")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Sensor Values")
ax.legend(loc="upper left")

start_time = time.time()

while True:
    try:
        line_data = ser.readline().decode(errors="ignore").strip()
        print("📥 Raw:", line_data)

        gas, temp, hum = map(float, line_data.split(','))

        features = pd.DataFrame([[gas, 40, temp, hum]], columns=["CO(GT)", "NO2(GT)", "T", "RH"])
        prediction = model.predict(features)[0]

        print(f"CO: {gas} | Temp: {temp}°C | Hum: {hum}% → AQI: {prediction:.2f}")

        # Append to graph data
        now = round(time.time() - start_time, 1)
        timestamps.append(now)
        aqi_vals.append(prediction)
        gas_vals.append(gas)
        temp_vals.append(temp)
        hum_vals.append(hum)

        # Update graph
        line_aqi.set_xdata(timestamps)
        line_aqi.set_ydata(aqi_vals)

        line_gas.set_xdata(timestamps)
        line_gas.set_ydata(gas_vals)

        line_temp.set_xdata(timestamps)
        line_temp.set_ydata(temp_vals)

        line_hum.set_xdata(timestamps)
        line_hum.set_ydata(hum_vals)

        ax.set_xlim(max(0, now - 60), now + 5)
        ax.relim()
        ax.autoscale_view(True, True, True)
        plt.draw()
        plt.pause(0.01)

    except Exception as e:
        print("⚠️ Error:", e)
        continue
