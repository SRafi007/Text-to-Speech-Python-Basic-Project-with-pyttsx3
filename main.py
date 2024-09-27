from app.audiobook_generator import generate_audiobook
from app.file_utils import create_output_directory
from app.config import OUTPUT_DIRECTORY

if __name__ == '__main__':
    input_file = 'resources/example.txt'  # Path to the text or PDF file
    output_file = OUTPUT_DIRECTORY + 'audiobook.mp3'
    
    # Ensure output directory exists
    create_output_directory(OUTPUT_DIRECTORY)

    # Generate audiobook
    generate_audiobook(input_file, output_file)
