import streamlit as st

# Title of the webpage
st.title("Biography of Dianne")

# Display your introduction
st.header("Introduction")
st.write("""
    Hello! I am Dianne L. Anggot, a passionate student pursuing my studies in BSCpE. 
    I am currently studying at Surigao del Norte State University, where I focus on learning about Programming.
    I am highly motivated to expand my knowledge and gain practical experience in Computer Engineering.
""")

# Education
st.header("Education")
st.write("""
    - **2024 - Present School** :Surigao del Norte State University, BSCpE
    - **2023 - Previous School** :St. John's School of Bacuag Inc. , STEM
""")

# Interests and Hobbies
st.header("Interests and Hobbies")
st.write("""
    Outside of my academic studies, I have a variety of interests, including:
    - Interest 1: Reading, Sports
    - Interest 2: Drawing, Coding
    - Interest 3: Music, Writing
""")

# Skills and Achievements
st.header("Achievements")
st.write("""
    Some of the skills I have developed throughout my academic and personal journey include:
    - Achievement 1: Academic Recognition
    - Achievement 2: Projects
""")

# Contact Information (Optional)
st.header("Contact Information")
st.write("""
    You can reach me at:
    - **Email**: iane312005@gmail.com
    - **GitHub**: Your GitHub Profile URL
""")

# You can also include an image of yourself or something relevant to your studies
st.image('your-image.jpg', caption='A photo of me!', use_column_width=True)
