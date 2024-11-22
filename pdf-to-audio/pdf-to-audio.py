import pyttsx3
import PyPDF2
import sys

def pdf_to_audio(pdf_path, voice_rate=150, start_page=0, end_page=None):
    try:
        # Initialize PDF Reader and TTS engine
        pdf_reader = PyPDF2.PdfReader(pdf_path)
        engine = pyttsx3.init()

        # Set voice rate
        engine.setProperty('rate', voice_rate)

        # Define page range
        end_page = end_page if end_page else len(pdf_reader.pages)

        # Extract and read text
        for page_num in range(start_page, end_page):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            engine.say(text)

        engine.runAndWait()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    pdf_path = sys.argv[1]  # Example: python pdf_to_audio.py sample.pdf
    pdf_to_audio(pdf_path)
