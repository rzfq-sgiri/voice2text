# MP3 to Text Converter

This project is a Python-based application that converts MP3 audio files into text using AI-based transcription libraries. The application is accessible via a Streamlit interface and is hosted on GitHub for easy collaboration.

---

## Features
- Upload MP3 files and convert them to text.
- Leverages AI-powered transcription models (e.g., OpenAI Whisper).
- Supports additional audio formats (e.g., WAV, FLAC) via conversion.
- Easy-to-use Streamlit interface.
- Deployable on Streamlit Cloud.

---

## Prerequisites

Ensure you have the following installed:

1. Python 3.7 or higher
2. Required libraries:
   - `openai-whisper`
   - `streamlit`
   - `pydub`

Install them using:
```bash
pip install openai-whisper streamlit pydub
```

---

## How It Works

1. User uploads an MP3 file via the Streamlit interface.
2. The MP3 file is converted to WAV format using `pydub`.
3. The WAV file is transcribed into text using the OpenAI Whisper model.
4. The transcribed text is displayed on the Streamlit interface.

---


## Future Improvements

- Add support for more transcription languages.
- Enable saving the transcribed text to `.txt` or `.docx` files.
- Include a progress bar for longer audio files.
- Optimize performance for larger files.

---

## License

This project is licensed under the MIT License. Feel free to use and modify it as needed.

---

## Contact

For questions or feedback, please contact [suriya-kame/riszafiq601@gmail.com].
