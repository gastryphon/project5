
import streamlit as st
import pandas as pd
st.title("Welcome to Streamlit!")
st.write("Our first DataFrame")
st.write( pd.DataFrame({ 'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8] }) )

selectbox = st.selectbox( "Select yes or no", ["Yes", "No"] )
st.write(f"You selected {selectbox}")

if selectbox=="Yes":
    st.write("good choice")
else: st.write("bad choice")

checkbox_one = st.checkbox("Yes")
checkbox_two = st.checkbox("No")
if checkbox_one: value = "Yes"
elif checkbox_two: value = "No"
else: value = "No value selected"
st.write(f"You selected: {value}") 