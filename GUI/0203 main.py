import streamlit as st
import pandas as pd
import streamlit as st

st.title("XXXX --QQQAAAXXX  Pico_W 0203專案建置")
st.header("雞舍:red[溫度]和:blue[光線]狀態")
st.subheader('This is a subheader with a divider', divider='rainbow')

st.subheader('_Streamlit_ is :blue[cool] :sunglasses:')

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
st.divider()
