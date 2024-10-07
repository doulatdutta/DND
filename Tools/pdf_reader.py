import os
import PyPDF2

class PDFReader:
    def __init__(self, pdf_folder="input/pdfs"):
        self.pdf_folder = pdf_folder
        self.pdf_path = self.get_latest_pdf()

    def get_latest_pdf(self):
        """
        Retrieves the latest PDF file from the specified folder.
        """
        pdf_files = [f for f in os.listdir(self.pdf_folder) if f.endswith('.pdf')]
        if pdf_files:
            latest_pdf = max(pdf_files, key=lambda f: os.path.getctime(os.path.join(self.pdf_folder, f)))
            return os.path.join(self.pdf_folder, latest_pdf)
        else:
            print("No PDF files found in the specified folder.")
            return None

    def extract_text(self):
        """
        Extracts and returns text from the provided PDF.
        """
        if self.pdf_path is None:
            print("No PDF to extract text from.")
            return None
        
        try:
            with open(self.pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ''
                for page_num in range(len(reader.pages)):
                    text += reader.pages[page_num].extract_text()
            print(f"Text extracted from {self.pdf_path}.")
            return text
        except FileNotFoundError:
            print(f"File {self.pdf_path} not found.")
            return None

    def analyze_pdf(self):
        """
        Analyze, learn from the PDF, and memorize learning.
        """
        text = self.extract_text()
        if text:
            # Add your custom analysis logic here
            print(f"Analyzing PDF content: {text[:100]}...")  # Display a preview of extracted text
        else:
            print("Failed to extract text from PDF.")
