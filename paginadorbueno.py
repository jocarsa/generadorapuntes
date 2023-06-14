from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader

from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader

def replace_page_text(input_path, output_path):
    pdf = PdfReader(input_path)
    total_pages = len(pdf.pages)

    c = canvas.Canvas(output_path)

    for page_number in range(total_pages):
        page = pdf.pages[page_number]
        content = page.extract_text()

        if "[pagina]" in content:
            modified_content = content.replace("[pagina]", f"{page_number + 1} of {total_pages}")
            c.showPage()
            c.setFont("Helvetica", 12)
            c.drawString(50, 50, modified_content)

    c.save()

    print(f"Modified PDF saved to {output_path}")

# Example usage:
input_file = "../seo-doc.html.pdf"  # Path to your input PDF file
output_file = "../seo-doc2.html.pdf"  # Path to the output PDF file
replace_page_text(input_file, output_file)
