import pdfplumber
import docx


def extract_pdf_text(pdf_path):
    text = ""

    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()

                if extracted:
                    text += extracted + "\n"

    except Exception as e:
        print(f"PDF Extraction Error: {e}")

    return text


def extract_docx_text(docx_path):
    text = ""

    try:
        doc = docx.Document(docx_path)

        for para in doc.paragraphs:
            text += para.text + "\n"

    except Exception as e:
        print(f"DOCX Extraction Error: {e}")

    return text