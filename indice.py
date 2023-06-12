import PyPDF2

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
                    lines_with_number_dot.append((line.strip(), page_number + 1))  # Store line and page number

    return lines_with_number_dot

# Usage
pdf_path = '../seo-doc.html.pdf'

lines = find_lines_with_number_dot(pdf_path)
if lines:
    print("Lines starting with a number and a dot found in the PDF:")
    for line, page_number in lines:
        print(f"Page {page_number}: {line}")
else:
    print("No lines starting with a number and a dot found in the PDF.")
