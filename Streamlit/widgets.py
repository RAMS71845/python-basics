import streamlit as st
st.title("Widgets: input you can read")
st.header("Tell me about you!!")
name=st.text_input("What is your name??","")
age=st.slider("How old are you?",0,100,20)
city=st.selectbox("Which city",
["Delhi","Mumbai","Lucknow","Pune"])
blood_group=st.selectbox("Select your blood group:",
["A+","B+","C+","O+"])
st.write(f"Hi **{name or 'friend'}**,  age: {age},  city:{city}")
st.divider()
st.header("Live TIP calculator")
bill=st.number_input("Bill Amount (Rs)",
min_value=0.0,value=500.0,step=50.0)
tip_percent=st.slider("TIP%",0,30,10)
tip=bill*tip_percent/100
total=bill+tip
st.metric("Total To Pay",f"Rs{total:.2f}")
