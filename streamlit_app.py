import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title= 'IRIS FLOWER DASHBOARD')
st.title('IRIS FLOWER DASHBOARD')
with st.sidebar:
    st.header('Description')
    st.write('The Iris dataset was used in R.A. Fishers classic 1936 paper, The Use of Multiple Measurements in Taxonomic Problems, and can also be found on the UCI Machine Learning Repository. It includes three iris species with 50 samples each as well as some properties about each flower. One flower species is linearly separable from the other two, but the other two are not linearly separable from each other.')
my_dataset = "C:/Users/User38/Desktop/Deployment/data/Iris.csv"
df = pd.read_csv(my_dataset)
df
if st.checkbox("Preview DataFrame"):
	
	if st.button("Head"):
		st.write(my_dataset.head())
	if st.button("Tail"):
		st.write(my_dataset.tail())
	else:
		st.write(my_dataset.head(2))

if st.checkbox("Show All DataFrame"):
	st.dataframe(my_dataset)
