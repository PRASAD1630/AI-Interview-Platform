import pdfplumber

def extract_text(pdf_path):

    text = ""

    with pdfplumber.open(pdf_path) as pdf:

        print("Pages:", len(pdf.pages))

        for page_num, page in enumerate(pdf.pages):

            page_text = page.extract_text()

            print("Page", page_num + 1)
            print(page_text)

            if page_text:
                text += page_text + "\n"

    return text