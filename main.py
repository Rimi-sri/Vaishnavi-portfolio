import streamlit as st
from streamlit_lottie import st_lottie
import requests
import pandas as pd
from datetime import datetime

# Load Lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_yr6zz3wv.json")

# Page config
st.set_page_config(page_title="Vaishnavi's Portfolio", page_icon="💻", layout="wide")

# Hero section
col1, col2 = st.columns([1, 2])
with col1:
    st.image("IMG_20240717_075534_047.jpg", width=180)
with col2:
    st.title("Vaishnavi Srivastava")
    st.markdown("**Python Developer | Automation Enthusiast | Game Dev Explorer**")
    st.write("Welcome to my portfolio! I love building tools that make life easier and exploring new technologies.")

# Lottie animation
st_lottie(lottie_coding, height=250, key="coding")

# Skills
st.subheader("🛠️ Skills")
st.markdown("""
- Python 🐍  
- Web Scraping (BeautifulSoup, Selenium)  
- API Integration (Twilio, OpenWeather, Spotify)  
- Git & GitHub  
- Game Development (Unity, itch.io)  
""")

st.divider()

# Projects
st.subheader("🚀 Projects")
project_cols = st.columns(3)

with project_cols[0]:
    st.markdown("### 🎵 Spotify Playlist Generator")
    st.write("Automatically creates playlists using Spotipy and Billboard data.")
with project_cols[1]:
    st.markdown("### 🌦️ Weather Alert System")
    st.write("Sends SMS alerts using OpenWeather API and Twilio.")
with project_cols[2]:
    st.markdown("### 📈 Stock Market Tracker")
    st.write("Scrapes stock data and news headlines for daily updates.")

st.divider()

# About Me
st.subheader("📚 About Me")
st.write("""
I'm passionate about Python and automation. I enjoy solving real-world problems with code, 
and I'm currently diving into game development and cloud computing. 
In my free time, I explore APIs, build bots, and participate in game jams.
""")

# Education
st.subheader("🎓 Education")
edu_col1, edu_col2 = st.columns([1, 5])
with edu_col1:
    st.image("https://img.icons8.com/ios-filled/100/graduation-cap.png", width=50)
with edu_col2:
    st.markdown("""
**Bachelor of Technology (B.Tech)**  
*Computer Science & Engineering*  
📍 Maharishi University, Lucknow, Uttar Pradesh, India  
📅 **Expected Completion:** 2026  

**Current Status:** 4th Year, 1st Semester  



**Semester-wise Performance:**
- 1st Sem: 586 / 700
- 2nd Sem: 608 / 700
- 3rd Sem: 587 / 700
- 4th Sem: 575 / 700
- 5th Sem: 627 / 700
- 6th Sem: 597 / 700
""")
st.subheader("🎯 CGPA Progress")
st.progress(0.897)  # 8.97 out of 10
# Achievements
st.subheader("🏆 Achievements")
st.markdown("""
            -**Hackathon**: Participated in multiple hackathons
            -**Bug hunting runner-up**: Recognized for finding critical bugs in software,
            """)
st.divider()

# Resume Download
st.subheader("📄 Resume")
try:
    with open("Vaishnavi_Resume.pdf", "rb") as file:
        st.download_button(
            label="📥 Download My Resume",
            data=file,
            file_name="Vaishnavi_Resume.pdf",
            mime="application/pdf"
        )
except FileNotFoundError:
    st.warning("Resume file not found. Please add 'Vaishnavi_Resume.pdf' to your project folder.")

# Contact
st.subheader("📫 Contact Me")
st.markdown("""
- [LinkedIn](https://www.linkedin.com/in/vaishnavi-s-178951299)  
- [GitHub](https://github.com/Rimi-sri)  
""")

# Contact Form
st.subheader("📬 Send Me a Message")
with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Send")

    if submitted:
        new_message = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "name": name,
            "email": email,
            "message": message
        }

        try:
            df = pd.read_csv("messages.csv")
            df = pd.concat([df, pd.DataFrame([new_message])], ignore_index=True)
        except FileNotFoundError:
            df = pd.DataFrame([new_message])

        df.to_csv("messages.csv", index=False)
        st.success("Thanks for your message! It has been saved.")

# Footer
st.markdown("---")
st.markdown("© 2025 Vaishnavi Srivastava | Made with ❤️ using Streamlit", unsafe_allow_html=True)
