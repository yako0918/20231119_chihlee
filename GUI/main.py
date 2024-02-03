import streamlit as st
import pandas as pd
import requests
from streamlit_autorefresh import st_autorefresh
import dotenv
import os

#streamlit run main.py 重啟服務

dotenv.load_dotenv

st_autorefresh(interval=5000)

st.title("Pico_W_職能發展協會專案")
st.header("雞舍:red[溫度]和:blue[光線]狀態")
st.divider()

url = f 'https://blynk.cloud/external/api/get?token={os.environ["API_KEY"]}&v0&v1'

response = requests.request("GET",url)
if response.status_code == 200:
    all_data = response.json()
    st.info(f'光線:{all_data["v0"]}')
    st.warning(f'可變電阻:{all_data["v1"]}')
else:
    st.write("連線失敗,請等一下再試")