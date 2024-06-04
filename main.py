import streamlit as st
from langchain_helper import generate_name
import json

st.title('Restaurant Name Generator with GEMINI')

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Chinese", "Mexican", "American"))

if cuisine:
    response = generate_name(cuisine)
    response_dict = json.loads(response)
    

    st.header(response_dict['restaurant_name'])

    st.write("Menu Items:")
    for item in response_dict['menu_items']:
        st.write(f"- {item}")