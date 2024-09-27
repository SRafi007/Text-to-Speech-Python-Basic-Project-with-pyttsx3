import PyPDF2

def read_text_file(file_path: str) -> str:
    with open(file_path, 'r') as f:
        return f.read()

def read_pdf_file(file_path: str) -> str:
    text = ""
    with open(file_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text()
    return text
