import streamlit as st
st.title("Hello world! I am Ram Srivastava")
st.header("I am a web page written in Python using Streamlit")
st.subheader("I am a subheader")
st.write("Gotcha!! friends")
st.write("two plus two is:",2+2)

st.markdown("Streamlit understand **Markdown** syntax")
st.button("Press me")
if st.button("Press Here"):
    st.success("Button was clicked!!")