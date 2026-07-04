import streamlit as st
# count=0
# if st.button("Add One"):
#     count=count+1
# st.write("Count",count)

#st.session_State->yeh is liye use kr rhe jisse page waps reload hoke zero pai na ajaye

if "count"not in st.session_state:
    st.session_state.count=0
if st.button("Add One"):
    st.session_state.count+=1
st.write("Count Value: ",st.session_state.count)
