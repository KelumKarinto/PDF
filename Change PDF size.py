from PIL import Image
import fitz
import io

def compress_pdf(input_pdf, output_pdf):
    try:
        doc = fitz.open(input_pdf)

        for page_num in range(len(doc)):
            page = doc[page_num]
            images = page.get_images(full=True)

            for img_index, img in enumerate(images):
                xref = img[0]  # Reference number of the image
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]

                # Use Pillow to process the image
                with Image.open(io.BytesIO(image_bytes)) as img:
                    img = img.convert("RGB")  # Ensure compatibility
                    img.thumbnail((1024, 1024))  # Resize to a smaller resolution
                    compressed_image_io = io.BytesIO()
                    img.save(compressed_image_io, format="JPEG", quality=1)  # Lower quality
                    compressed_image_bytes = compressed_image_io.getvalue()

                # Replace the image in the PDF
                page.replace_image(xref, pixmap=fitz.Pixmap(compressed_image_bytes))

        # Save the output PDF
        doc.save(output_pdf, garbage=4, deflate=True)
        print(f"PDF compressed and saved to: {output_pdf}")
    except Exception as e:
        print(f"Error compressing PDF: {e}")

# Example usage
input_pdf = "/home/kelum/Downloads/Papers for read/s42247-024-00678-1.pdf"
output_pdf = "/home/kelum/Downloads/Papers for read/Compressed_s42247-024-00678-1.pdf"
compress_pdf(input_pdf, output_pdf)
