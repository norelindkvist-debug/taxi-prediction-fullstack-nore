import streamlit as st
import pandas as pd
import httpx

BASE_URL = "http://127.0.0.1:8000"
DATA_URL = f"{BASE_URL}/taxi/"
PREDICT_URL = f"{DATA_URL}predict"

data = httpx.get(DATA_URL)
df = pd.DataFrame(data.json())


def main():
    page = st.sidebar.radio("Pages", ["Predict taxi price", "Raw data"])
    if page == "Predict taxi price":
        st.markdown("# Taxi prediction app")
        st.markdown("App to predict taxi prices, type in your trip distance")
        with st.form("taxi_data"):
            trip_distance = st.number_input(
                "Trip Distance (km)", min_value=1, max_value=60
            )
            day_of_week = st.selectbox("Day_of_Week", ["Weekday", "Weekend"])
            passanger_count = st.selectbox("Passenger_Count", [1, 2, 3, 4])
            traffic_conditions = st.selectbox(
                "Traffic_Conditions", ["Low", "High", "Medium"]
            )
            weather = st.selectbox("Weather", ["Clear", "Rain", "Snow"])

            submitted = st.form_submit_button("PREDICT")

        if submitted:
            payload = {
                "Trip_Distance_km": float(trip_distance),
                "Day_of_Week": day_of_week,
                "Passenger_Count": passanger_count,
                "Traffic_Conditions": traffic_conditions,
                "Weather": weather,
            }
            response = httpx.post(PREDICT_URL, json=payload)
            prediction = response.json().get("predicted_price")
            st.markdown(f"**Predicted price:** {prediction:.2f}")

    if page == "Raw data":
        st.markdown("## Raw data")
        st.dataframe(df)


if __name__ == "__main__":
    main()
