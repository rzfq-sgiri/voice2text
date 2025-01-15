import streamlit as st
import whisper
from pydub import AudioSegment

def convert_audio_to_text(audio_file, format):
    """
    Convert audio file to text using Whisper.
    
    Args:
        audio_file: Uploaded audio file.
        format: The format of the audio file (e.g., 'mp3', 'm4a').
        
    Returns:
        Transcribed text.
    """
    # Load the Whisper model
    model = whisper.load_model("base")
    
    # Convert audio to WAV format using pydub
    audio = AudioSegment.from_file(audio_file, format=format)
    wav_file = "temp_audio.wav"
    audio.export(wav_file, format="wav")
    
    # Transcribe audio
    result = model.transcribe(wav_file)
    return result['text']

# Streamlit UI
st.title("Audio to Text Converter")
st.subheader("Upload an MP3 or M4A file to convert it to text")

uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "m4a"])

if uploaded_file is not None:
    file_format = uploaded_file.name.split('.')[-1]  # Extract file format from file name
    
    st.info(f"File format detected: {file_format.upper()}")
    
    with st.spinner("Converting... Please wait!"):
        try:
            transcription = convert_audio_to_text(uploaded_file, file_format)
            st.success("Conversion complete!")
            st.text_area("Transcribed Text", transcription, height=300)
        except Exception as e:
            st.error(f"An error occurred: {e}")
