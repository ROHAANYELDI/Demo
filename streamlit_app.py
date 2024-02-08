import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title= 'IRIS FLOWER DASHBOARD')
st.title('IRIS FLOWER DASHBOARD')
with st.sidebar:
    st.header('Description')
    st.write('The Iris dataset was used in R.A. Fishers classic 1936 paper, The Use of Multiple Measurements in Taxonomic Problems, and can also be found on the UCI Machine Learning Repository. It includes three iris species with 50 samples each as well as some properties about each flower. One flower species is linearly separable from the other two, but the other two are not linearly separable from each other.')
my_dataset = "Iris.csv"
df = pd.read_csv(my_dataset)
df
if st.checkbox("Preview DataFrame"):
	
	if st.button("Head"):
		st.write(df.head())
	if st.button("Tail"):
		st.write(df.tail())
	else:
		st.write(df.head(2))

# Show Entire dataframe
if st.checkbox("Show all DataFrame"):
	st.dataframe(df)

# Show Description
if st.checkbox("Show All Column Name"):
	st.text("Columns:")
	st.write(df.columns)
st.divider()

