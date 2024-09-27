import pyttsx3

def init_tts_engine(rate=150, volume=1.0, voice_gender='female'):
    engine = pyttsx3.init()
    
    # Set properties
    engine.setProperty('rate', rate)  # Speed
    engine.setProperty('volume', volume)  # Volume

    # Set voice gender
    voices = engine.getProperty('voices')
    if voice_gender == 'female':
        engine.setProperty('voice', voices[1].id)
    else:
        engine.setProperty('voice', voices[0].id)
    
    return engine

def save_as_audio(engine, text, output_file):
    engine.save_to_file(text, output_file)
    engine.runAndWait()
