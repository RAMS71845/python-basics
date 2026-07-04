import streamlit as st
st.title("Layout a page")
st.sidebar.header("Settings")

model=st.sidebar.selectbox("Model",
["llama","OpenAI","Gemini"])
temperature=st.sidebar.slider("Temperature",0.0,1.0,0.2)

st.header("Welcome To New Page")
st.write(f"You picked **{model}** at temp : {temperature}")
# st.header("Welcomne to the next page")

st.header("Cols put things side by side")
col1,col2,col3=st.columns(3)

with col1:
    st.write("Col 1 Content")
    st.metric("Users",1290,"+120")
with col2:
    st.write("Col 2 Content")
    st.metric("Active Today",342,"-8")
with col3:
    st.write("Col 3 Content")
    st.metric("Signups",23,"+15")

st.divider()
st.header("Tabs Act like mini page")
tab_summary,tab_details=st.tabs(["Summary","Details"])
with tab_summary:
    st.write("These summaries are particularly useful for saving time, improving clarity, and creating elevator pitches or study notes, and they can be customized for length, style, or focus depending on the user’s needs")
with tab_details:
    st.write("This is a details tab.")

st.header("Expander hide long or optional content")
with st.expander("Click to see content"):
    st.code(
        "You are a helpful assistant",
        language="text"
    )
show_debug=st.sidebar.checkbox("Show debug info")
if show_debug:
    st.warning("Debug mode is ON")
    st.json({"mode":model,"temperature":temperature})

