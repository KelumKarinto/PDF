from PyPDF2 import PdfReader, PdfWriter

def add_password_to_pdf(input_pdf, output_pdf, password):
    try:
        # Read the input PDF
        reader = PdfReader(input_pdf)
        writer = PdfWriter()

        # Copy all pages to the writer
        for page in reader.pages:
            writer.add_page(page)

        # Set the password for the output PDF
        writer.encrypt(password)

        # Write the encrypted PDF to the output file
        with open(output_pdf, "wb") as output_file:
            writer.write(output_file)
        
        print(f"Password-protected PDF saved at: {output_pdf}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Input parameters
    input_pdf = "/home/kelum/Downloads/Papers for read/s42247-024-00678-1.pdf"  # Replace with your input PDF file
    output_pdf = "/home/kelum/Downloads/Papers for read/s42247-024-00678-1_protected"  # Replace with your desired output file path
    password = "sakailab"  # Replace with your desired password

    # Call the function
    add_password_to_pdf(input_pdf, output_pdf, password)
