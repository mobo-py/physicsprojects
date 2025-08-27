import os
from PIL import Image

# Path to your folder
folder = "gravity/planets/surface"

# Remove everything in the folder
for f in os.listdir(folder):
    file_path = os.path.join(folder, f)
    if os.path.isfile(file_path):
        os.remove(file_path)
    elif os.path.isdir(file_path):
        # optional: remove subfolders if any
        import shutil
        shutil.rmtree(file_path)

# Now, process and save images from the original source folder
source_folder = folder  # assuming original images are still in memory or elsewhere

# If your original images are elsewhere, set source_folder to that path
# e.g., source_folder = "gravity/planets/originals"

# Loop through all files in the source folder
for filename in os.listdir(source_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff")):
        filepath = os.path.join(source_folder, filename)

        try:
            # Open image
            img = Image.open(filepath)

            # Resize
            img_resized = img.resize((800, 600), Image.LANCZOS)

            # Ensure RGB (for JPG)
            if img_resized.mode in ("RGBA", "P"):
                img_resized = img_resized.convert("RGB")

            # Save as JPG, overwriting folder
            new_filename = os.path.splitext(filename)[0] + ".jpg"
            new_filepath = os.path.join(folder, new_filename)
            img_resized.save(new_filepath, "JPEG", quality=95)
            print(f"✅ Saved: {new_filepath}")

        except Exception as e:
            print(f"⚠️ Error processing {filename}: {e}")
