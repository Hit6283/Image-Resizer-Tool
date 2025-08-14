import os
from PIL import Image

input_folder = "input_images"
output_folder = "output_images"
new_size = (800, 800)
output_format = "JPEG"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp", ".bmp")):
        img_path = os.path.join(input_folder, filename)

        with Image.open(img_path) as img:
            img_resized = img.resize(new_size)

            # RGBA/P mode → RGB convert
            if img_resized.mode in ("RGBA", "P"):
                img_resized = img_resized.convert("RGB")

            base_name = os.path.splitext(filename)[0]
            output_path = os.path.join(output_folder, f"{base_name}.{output_format.lower()}")
            img_resized.save(output_path, output_format, quality=95)

        print(f"Resized & Saved: {output_path}")

print("All images resized successfully!")
