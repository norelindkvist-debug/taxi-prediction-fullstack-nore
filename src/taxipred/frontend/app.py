import streamlit as st
import pandas as pd
import httpx 

BASE_URL = "http://127.0.0.1:8000"

data = httpx.get(f"{BASE_URL}/taxi")

df = pd.DataFrame(data.json())

def main():
    st.markdown("# Taxi prediction app")

    st.dataframe(df)

if __name__ == "__main__":
    main()