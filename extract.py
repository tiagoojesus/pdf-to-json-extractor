import fitz  # PyMuPDF
import os
import json

# Define file paths
pdf_path = "./database-exams/rel_3_condutores.pdf"  # Change to your PDF file
output_folder = "extracted_images"
output_json = "output.json"

# Create folder for images
os.makedirs(output_folder, exist_ok=True)

# Open PDF
doc = fitz.open(pdf_path)
data = {"pages": []}

for i, page in enumerate(doc):
    page_data = {
        "text": page.get_text("text"),  # Extract text
        "images": []
    }

    for img_index, img in enumerate(page.get_images(full=True)):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]

        # Save image
        image_filename = f"image_{i+1}_{img_index+1}.{image_ext}"
        image_path = os.path.join(output_folder, image_filename)
        with open(image_path, "wb") as img_file:
            img_file.write(image_bytes)

        page_data["images"].append(image_filename)

    data["pages"].append(page_data)

# Save everything in JSON
with open(output_json, "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)

print(f"Text and images extracted! Check '{output_json}' and '{output_folder}'")
