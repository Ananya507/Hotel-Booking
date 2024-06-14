import streamlit as st
import PyPDF2
import pyttsx3
import os

# Set Streamlit app title and description
st.title("GLIMPSE OF INDIA HERITAGE")

# Upload PDF file
pdf_file =open("monuments.pdf",'rb')

if pdf_file:
    # Read PDF and extract text
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

    # Convert text to speech
    engine = pyttsx3.init()
    # Save the audio file
    audio_file = "output.mp3"
    engine.save_to_file(text, audio_file)
    engine.runAndWait()

    # Provide download link to the audiobook
    st.audio(audio_file, format="audio/mp3")
    
    # Remove the audio file after it's played
    os.remove(audio_file)

