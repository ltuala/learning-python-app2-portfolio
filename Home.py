import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/github_dp.png")
    st.write("Lyndon Tuala")
with col2:
    st.title("A Glimpse into my Python Learning Journey")
    content = """
    Hi!
    Here are some of the hands-on projects I created while learning Python through this  [Udemy course](https://www.udemy.com/course/the-python-mega-course/?course_id=692188).
    Each project reflects the skills and concepts I explored along the way!
    """
    st.info(content)

st.write("Below you can find some of the apps I have built in Python. \
         Feel free to contact me!")

df = pd.read_csv("data.csv", sep=';')

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
        if row['url'] != 'na':
            st.write(f"[Demo]({row['demo']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
        if row['url'] != 'na':
            st.write(f"[Demo]({row['demo']})")
