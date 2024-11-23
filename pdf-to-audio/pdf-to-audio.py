import pyttsx3
import PyPDF2
import os


def list_voices(engine):
    """List available voices for selection."""
    voices = engine.getProperty('voices')
    print("Available Voices:")
    for i, voice in enumerate(voices):
        print(f"{i}: {voice.name} ({voice.languages})")


def pdf_to_audio(pdf_path, voice_rate=150, voice_index=0, start_page=0, end_page=None):
    """
    Convert PDF text to speech.
    :param pdf_path: Path to the PDF file.
    :param voice_rate: Reading speed in words per minute.
    :param voice_index: Index of the voice to use.
    :param start_page: Page to start reading from (0-indexed).
    :param end_page: Page to stop reading at (None for last page).
    """
    # Check if file exists
    if not os.path.exists(pdf_path):
        print("Error: File not found!")
        return

    try:
        # Initialize PDF Reader
        pdf_reader = PyPDF2.PdfReader(pdf_path)
        total_pages = len(pdf_reader.pages)
        end_page = end_page if end_page is not None else total_pages

        if start_page >= total_pages or start_page < 0:
            print("Error: Start page is out of range.")
            return

        if end_page > total_pages or end_page <= start_page:
            print("Error: End page is out of range or invalid.")
            return

        # Initialize TTS engine
        engine = pyttsx3.init()
        engine.setProperty('rate', voice_rate)

        # Set voice
        voices = engine.getProperty('voices')
        if 0 <= voice_index < len(voices):
            engine.setProperty('voice', voices[voice_index].id)
        else:
            print("Invalid voice index. Using default voice.")

        # Convert pages to speech
        print(f"Reading pages {start_page + 1} to {end_page}...")
        for page_num in range(start_page, end_page):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            if text.strip():
                print(f"Reading page {page_num + 1}...")
                engine.say(text)
            else:
                print(f"Page {page_num + 1} is empty or unreadable.")

        engine.runAndWait()
        print("Finished reading the PDF!")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    import argparse

    # Argument parsing
    parser = argparse.ArgumentParser(description="Convert a PDF file to audio.")
    parser.add_argument("pdf_path", help="Path to the PDF file.")
    parser.add_argument("--voice_rate", type=int, default=150, help="Reading speed (default: 150).")
    parser.add_argument("--voice_index", type=int, default=0, help="Index of the voice to use (default: 0).")
    parser.add_argument("--start_page", type=int, default=0, help="Page number to start from (default: 0).")
    parser.add_argument("--end_page", type=int, default=None, help="Page number to stop at (default: last page).")

    args = parser.parse_args()

    pdf_to_audio(
        pdf_path=args.pdf_path,
        voice_rate=args.voice_rate,
        voice_index=args.voice_index,
        start_page=args.start_page,
        end_page=args.end_page,
    )