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
                modified_text = text.replace(selector, f'{page_number + 1} of {num_pages}')
                page = page.extract_text(modified_text)

            writer.add_page(page)

        output_pdf_path = 'output.pdf'
        with open(output_pdf_path, 'wb') as output_file:
            writer.write(output_file)

        print(f"Selector '{selector}' replaced with page numbers in the PDF.")

def find_lines_with_number_dot(pdf_path):
    lines_with_number_dot = []

    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        for page_number in range(num_pages):
            page = reader.pages[page_number]
            text = page.extract_text()

            lines = text.split("\n")
            for line in lines:
                if line.strip().startswith(('0.', '1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.')):
                    lines_with_number_dot.append((line.strip(), page_number + 1))

    return lines_with_number_dot

# Usage
pdf_path = '../seo-doc.html.pdf'
selector = '[pagina]'

replace_selector_with_page_number(pdf_path, selector)

lines = find_lines_with_number_dot(pdf_path)
if lines:
    print("Lines starting with a number and a dot found in the PDF:")
    for line, page_number in lines:
        print(f"Page {page_number}: {line}")
else:
    print("No lines starting with a number and a dot found in the PDF.")
