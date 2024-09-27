# 🎧 Audiobook Generator with `pyttsx3`

Welcome to the **Audiobook Generator**! This Python project converts text from `.txt` or `.pdf` files into audiobooks using the offline text-to-speech engine, [`pyttsx3`](https://pypi.org/project/pyttsx3/). The program reads text, converts it to speech, and saves it as an audio file (like `.mp3` or `.wav`), making it easy for you to create your own audiobooks!

---

## 📝 **Features**
- Convert `.txt` or `.pdf` files into audio formats.
- Customize voice speed, volume, and gender (male/female).
- Save generated speech as `.mp3` or `.wav` files.
- Fully offline using `pyttsx3`, no internet connection needed.

---

## 🛠️ **Project Structure**

Here's an initial project structure to give you an overview:

```bash
audiobook_generator/
├── app/
│   ├── __init__.py
│   ├── text_processor.py       # Functions to read text from files
│   ├── tts_engine.py           # pyttsx3-based TTS functions
│   ├── audiobook_generator.py  # Main logic for generating audiobooks
│   └── config.py               # Configuration settings for TTS
├── resources/                  # Folder for input/output files
│   ├── example.txt             # Example text file for testing
│   └── output/
│       └── audiobook.mp3       # Output audiobook
├── main.py                     # Entry point for running the program
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
