import os
from dotenv import load_dotenv
from PIL import Image
import pillow_heif

# Load the .env variables
load_dotenv()

input_folder = os.getenv("INPUT_HEIC_FOLDER")
output_folder = os.getenv("OUTPUT_JPG_FOLDER")

def convert_heic_to_jpg(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        # Checks the file extension in lowercase to handle .HEIC, .heic, .Heic, etc.
        if filename.lower().endswith(".heic"):
            heic_path = os.path.join(input_folder, filename)
            jpg_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.jpg")

            try:
                heif_file = pillow_heif.read_heif(heic_path)
                image = Image.frombytes(
                    heif_file.mode, heif_file.size, heif_file.data, "raw"
                )
                image.save(jpg_path, "JPEG")
                print(f"Converted {filename} to JPG.")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

convert_heic_to_jpg(input_folder, output_folder)
