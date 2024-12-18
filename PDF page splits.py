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
    # User input for the file path and output folder
    input_pdf = input("Enter the path to the PDF file: ").strip()
    output_folder = input("Enter the output folder path: ").strip()

    # User input for specific page numbers
    try:
        pages = input("Enter the page numbers to extract (comma-separated): ").strip()
        page_numbers = list(map(int, pages.split(",")))

        extract_pdf_pages(input_pdf, output_folder, page_numbers)
    except ValueError:
        print("Invalid input. Please enter page numbers as comma-separated integers.")
