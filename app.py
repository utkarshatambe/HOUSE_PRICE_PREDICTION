import joblib
import pandas as pd
import streamlit as st

st.set_page_config(page_icon="",page_title="HOUSE_PRICE_PREDICTION",layout = "wide")

# model
with open("RF_model.joblib","rb") as file:
    model = joblib.load(file)

# datset
df = pd.read_csv("cleaned_df.csv")

st.title("🏠 House Price Prediction")

# sidebar
with st.sidebar:
    st.title("HOUSE PRICE PREDCTION APP")
    st.image("house.jpg",width=300)

def get_encoded_loc(location):
    for loc,encoded in zip(df["location"],df["encoded_loc"]):
        if location == loc:
            return encoded
        
# user input fields
with st.container():
    col1,col2 = st.columns(2)
    with col1:
        location = st.selectbox("location",options = df["location"].unique())
        sqft = st.number_input("sq.ft:",min_value =300)


    with col2:
        bhk = st.selectbox("BHK:",options = sorted(df["bhk"].unique()))
        bath = st.selectbox("No of Bathrooms:",options = sorted(df["bath"].unique()))

  
    encoded_loc = get_encoded_loc(location)



c1,c2,c3 =st.columns([2.2,2,1])
if c2.button("$predict"):
    inp_data = [[sqft,bath,bhk,encoded_loc]]
    pred = model.predict(inp_data)
    pred = float(f"{pred[0]:.2f}")
    st.subheader(f"predicted price is Rs.{pred*100000}")

