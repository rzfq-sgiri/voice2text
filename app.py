import streamlit as st
import whisper
from pydub import AudioSegment

def convert_mp3_to_text(mp3_file):
    # Load the Whisper model
    model = whisper.load_model("base")
    
    # Convert MP3 to WAV format using pydub
    audio = AudioSegment.from_file(mp3_file)
    wav_file = "temp_audio.wav"
    audio.export(wav_file, format="wav")
    
    # Transcribe audio
    result = model.transcribe(wav_file)
    return result['text']

# Streamlit UI
st.title("MP3 to Text Converter")
uploaded_file = st.file_uploader("Upload an MP3 file", type=["mp3"])

if uploaded_file is not None:
    with st.spinner("Converting..."):
        transcription = convert_mp3_to_text(uploaded_file)
    st.success("Conversion complete!")
    st.text_area("Transcribed Text", transcription, height=300)
