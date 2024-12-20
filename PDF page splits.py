import os
from PyPDF2 import PdfReader, PdfWriter

def extract_pdf_pages(input_pdf, output_folder, page_numbers):
    try:
        # Ensure output folder exists
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Load the PDF file
        reader = PdfReader(input_pdf)

        # Validate page numbers
        max_pages = len(reader.pages)
        for page_num in page_numbers:
            if page_num < 1 or page_num > max_pages:
                raise ValueError(f"Invalid page number: {page_num}. PDF has {max_pages} pages.")

        # Extract specified pages
        for page_num in page_numbers:
            writer = PdfWriter()
            writer.add_page(reader.pages[page_num - 1])  # Pages are 0-indexed in PyPDF2

            output_file = os.path.join(output_folder, f"Page_{page_num}.pdf")
            with open(output_file, "wb") as output_pdf:
                writer.write(output_pdf)
            print(f"Extracted Page {page_num} to {output_file}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Define file paths and parameters directly in the script
    input_pdf = "/home/kelum/Downloads/Papers for read/s42247-024-00678-1.pdf"  # Replace with the path to your input PDF file
    output_folder = "/home/kelum/Desktop/Repos/PDF Editing"  # Replace with the desired output folder path
    page_numbers = [1, 2, 5]  # Replace with the list of pages you want to extract

    # Call the function
    extract_pdf_pages(input_pdf, output_folder, page_numbers)
