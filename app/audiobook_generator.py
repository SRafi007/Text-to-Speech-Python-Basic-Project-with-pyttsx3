from app.text_processor import read_text_file,read_pdf_file
from app.tts_engine import init_tts_engine, save_as_audio
import os

def generate_audiobook(input_file: str, output_file: str, rate=150, volume=1.0, voice_gender='female'):
    # Determine file type
    _, file_extension = os.path.splitext(input_file)

    # Extract text based on file type
    if file_extension == '.txt':
        text = read_text_file(input_file)
    elif file_extension == '.pdf':
        text = read_pdf_file(input_file)
    else:
        raise ValueError("Unsupported file format")

    # Initialize TTS engine
    engine = init_tts_engine(rate, volume, voice_gender)

    # Convert and save as audiobook
    save_as_audio(engine, text, output_file)
