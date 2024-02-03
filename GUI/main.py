import streamlit as st
import pandas as pd

st.title("XXXX --QQQAAAXXX  Pico_W 0203專案建置")
st.header("雞舍:red[溫度]和:blue[光線]狀態")
st.subheader('This is a subheader with a divider', divider='rainbow')

st.subheader('_Streamlit_ is :blue[cool] :sunglasses:')
st.divider()
import streamlit as st
import graphviz

# Create a graphlib graph object
graph = graphviz.Digraph()
graph.edge('run', 'intr')
graph.edge('intr', 'runbl')
graph.edge('runbl', 'run')
graph.edge('run', 'kernel')
graph.edge('kernel', 'zombie')
graph.edge('kernel', 'sleep')
graph.edge('kernel', 'runmem')
graph.edge('sleep', 'swap')
graph.edge('swap', 'runswap')
graph.edge('runswap', 'new')
graph.edge('runswap', 'runmem')
graph.edge('new', 'runmem')
graph.edge('sleep', 'runmem')

st.graphviz_chart(graph)