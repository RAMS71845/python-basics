import streamlit as st
import pandas as pd
st.title("Ways to show content")
st.header("1.Text")
st.write("st.write prints plain text and supports **Markdown ** Syntax")
st.code("def greet(name):\n return f'Hello,{name}'",language="python")
st.divider()
st.header("2.DATA and TABLES")
students=pd.DataFrame(
    {
        "Name":["Ram","Shikha","Cheeku"],
        "City":["Lko","Delhi","Mumbai"],
        "Score":[99,98,97]
    }
)
st.dataframe(students,width="stretch")
st.success("SUCCESS")
st.info("INFO")
st.warning("WARNING")
st.error("ERROR")
