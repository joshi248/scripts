from docx2pdf import convert
from PyPDF2 import PdfReader, PdfWriter
import os
import zipfile

def extract_page_range(pdf_file, start_page, end_page):
    output_pdf = PdfWriter()
    for page_num in range(start_page - 1, end_page):
        output_pdf.add_page(pdf_file.pages[page_num])
    return output_pdf

def create_pdf_zip(docx_file, chapter_page_ranges):
    pdf_dir = 'pdfs'
    os.makedirs(pdf_dir, exist_ok=True)

    # Convert the entire docx to PDF
    convert(docx_file, pdf_dir)

    # Open the converted PDF file
    pdf_file_path = os.path.join(pdf_dir, os.path.splitext(os.path.basename(docx_file))[0] + '.pdf')
    pdf_file = PdfReader(pdf_file_path)

    # Create PDFs for each chapter
    chapter_pdfs = []
    for chapter, (start_page, end_page) in chapter_page_ranges.items():
        chapter_pdf = extract_page_range(pdf_file, start_page, end_page)
        chapter_pdf_path = os.path.join(pdf_dir, f'{chapter}.pdf')
        with open(chapter_pdf_path, 'wb') as output_file:
            chapter_pdf.write(output_file)
        chapter_pdfs.append(chapter_pdf_path)

    # Create a zip file containing all the chapter PDFs
    zip_file = 'first_flight.zip'
    with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zf:
        for chapter_pdf in chapter_pdfs:
            zf.write(chapter_pdf, os.path.basename(chapter_pdf))

    return zip_file

def main():
    docx_file = 'F:/first_flight.docx'
    chapter_page_ranges = {
        'A letter to god': (1, 4),  # Define the page range for each chapter
        'Nelson Mandela': (5, 8),
        'Two stories about flying': (9, 13),
        'From the diary of Anne frank': (14, 18),
        'Hundred Dresses 1': (19, 22),
        'Hundred Dresses 2': (23, 26),
        'Glimpses of India': (27, 34),
        'Mijbil the otter': (35, 40),
        'Madam rides the bus': (41, 45),
        'The sermon at Benares': (46, 48),
        'The proposal': (49, 53),
        'Dust of Snow': (55, 56),
        'Fire and Ice': (58, 59),
        'A tiger in the zoo': (60, 62),
        'How to tell wild animals': (63, 65),
        'The ball poem': (66, 68),
        'Amanda': (69, 71),
        'Animals': (72, 74),
        'The trees': (75, 77),
        'Fog': (78, 80),
        'Custard the dragon': (81, 83),
        'For anne gregory': (84, 87)




        # Add more chapters and their respective page ranges here
    }

    zip_file = create_pdf_zip(docx_file, chapter_page_ranges)
    print(f'Created {zip_file}')

if __name__ == '__main__':
    main()
