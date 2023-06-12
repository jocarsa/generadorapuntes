import PyPDF2

def replace_selector_with_page_number(pdf_path, selector):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()

        num_pages = len(reader.pages)
        for page_number in range(num_pages):
            page = reader.pages[page_number]
            text = page.extract_text()

            if selector in text:
                # Replace the selector with the page number
                modified_text = text.replace(selector, str(page_number + 1))
                page = page.extract_text(modified_text)

            writer.add_page(page)

        output_pdf_path = '../seo-doc2.html.pdf'  # Path to the modified PDF file
        with open(output_pdf_path, 'wb') as output_file:
            writer.write(output_file)

        print(f"Selector '{selector}' replaced with page numbers in the PDF.")

# Usage
pdf_path = '../seo-doc.html.pdf'
selector = '[pagina]'

replace_selector_with_page_number(pdf_path, selector)
