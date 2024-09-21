import streamlit as st
import pandas as pd
import pickle

model=pickle.load(open('nbmod.pkl','rb'))
vector=pickle.load(open('vector.pkl','rb'))

def predicto(message):
    msg=vector.transform([message])
    pred=model.predict(msg)[0]
    return 'spam' if pred==1 else 'not spam'

st.title("SMS Spam Detection")

# Input text box for user to input an SMS message
user_input = st.text_area("Enter an SMS message:")

# Button to classify the message
if st.button("Check"):
    if user_input:
        prediction = predicto(user_input)
        st.write(f"The message is: **{prediction}**")
    else:
        st.write("Please enter a message.")