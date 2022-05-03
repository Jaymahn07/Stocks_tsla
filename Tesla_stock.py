import requests
import pickle
import yfinance as yf
import streamlit as st
from streamlit_lottie import st_lottie  
from PIL import Image
pickle_in = open("stocks.pkl", "rb")
tsl = pickle.load(pickle_in)

@st.cache()


def stocks(Open,high,low,volume):
    prediction = tsl.predict([[Open,high,low,volume]])[0]
    report = "The Closing Price is"+ " " +  str(round(prediction,3))
    return report
     
def load_lottie(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

lottie_coding =load_lottie("https://assets5.lottiefiles.com/packages/lf20_ky2ondsa.json")
def main():
    
    image = Image.open('Tesla.jpg')
    st.image(image, use_column_width =True)
    
    st.write("""
    # TESLA STOCK PRICE APP
    
    Helps to predict the Closing price after adjustments for all applicable splits and dividend distributions.
    
    \n The closing price is the reference point used by investors to compare a stock's performance over a period of time.
    """)
    st_lottie(lottie_coding,height =300, key="coding")
    Open = st.number_input("Open")
    
    high = st.number_input("High")
    
    low = st.number_input("Low")
     
    volume = st.number_input("Volume")
    
    
    output = ""
    
    if st.button("Make Prediction"):
        output = stocks(Open,high,low,volume)
        with st.spinner('Wait for it...'):
            print("The Closing Price is likely to be")
            
        st.success(output)
        


    
if __name__ == "__main__":
    main()
    
        
html = """ <h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://twitter.com/jaymahn_07" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="jaymahn_07" height="30" width="40" /></a>
<a href="https://linkedin.com/in/joshua-pereira-25b516237" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="joshua-pereira-25b516237" height="30" width="40" /></a>
<a href="https://kaggle.com/jaymahn07" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/kaggle.svg" alt="jaymahn07" height="30" width="40" /></a

</p>"""

st.markdown(html, unsafe_allow_html = True)
    
