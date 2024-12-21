import fitz  # PyMuPDF
from PIL import Image
import os


def compress_pdf(input_pdf_path, output_pdf_path, image_quality=75):
    try:
        # Open the original PDF
        pdf_document = fitz.open(input_pdf_path)

        # Create a new PDF document
        new_pdf = fitz.open()

        # Iterate through pages and compress images
        for page_num in range(len(pdf_document)):
            page = pdf_document[page_num]
            new_page = new_pdf.new_page(width=page.rect.width, height=page.rect.height)

            # Extract and compress images
            images = page.get_images(full=True)
            for img_index, img in enumerate(images):
                xref = img[0]
                base_image = pdf_document.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]

                # Save the image to a temporary file
                image_file = f"temp_image.{image_ext}"
                with open(image_file, "wb") as img_file:
                    img_file.write(image_bytes)

                # Compress the image
                compressed_image_file = f"compressed_temp_image.{image_ext}"
                with Image.open(image_file) as img:
                    img.save(compressed_image_file, quality=image_quality, optimize=True)

                # Create a Pixmap for the compressed image
                pixmap = fitz.Pixmap(compressed_image_file)

                # Insert the compressed image into the new PDF
                new_page.insert_image(page.rect, pixmap=pixmap)

                # Remove temporary files safely
                if os.path.isfile(image_file):
                    os.remove(image_file)
                if os.path.isfile(compressed_image_file):
                    os.remove(compressed_image_file)

            # Copy text, vectors, etc., from the original page
            new_page.show_pdf_page(page.rect, pdf_document, page_num)

        # Save the compressed PDF
        new_pdf.save(output_pdf_path, garbage=4, deflate=True)
        new_pdf.close()
        pdf_document.close()

        print(f"Compressed PDF saved as: {output_pdf_path}")

    except Exception as e:
        print(f"Error compressing PDF: {e}")


if __name__ == "__main__":
    input_pdf = "/home/kelum/Downloads/Papers for read/s42247-024-00678-1.pdf"  # Replace with your input PDF path
    output_pdf = "/home/kelum/Downloads/Papers for read/Compressed PDF"  # Replace with desired output PDF path
    compress_pdf(input_pdf, output_pdf)
