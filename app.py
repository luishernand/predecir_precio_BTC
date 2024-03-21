import pandas as pd
import streamlit as st
from PIL import Image
import joblib


# 1 Page configuration and titles
#-------------------------------

#load image
imagen = Image.open('logo.png')
st.image(imagen, use_column_width=True)
#st.title('BTC Prediction')
st.subheader('Close Prices Prediction Using Machine Learning')


# 2 Create User enter
#--------------------
open = st.number_input('Enter Open prices')
volume = st.number_input('Enter Volume')


# 3 create df
ex = pd.DataFrame({'Open': open, 'Volume': volume}, index=[0])

st.write('Your Enter this Data', ex)

#4 load model
#---------------
model = joblib.load('pipeline')

# 5. Predict 
if st.button('Prediction'):
    prediction = model.predict(ex)
    st.write('The Predicted Close Prices is', prediction)
else:
    print('Enter Data')