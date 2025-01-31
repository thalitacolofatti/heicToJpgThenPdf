import os
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

input_folder = os.getenv("OUTPUT_JPG_FOLDER")
output_pdf_path = os.path.join(os.getenv("OUTPUT_PDF_FOLDER"), "output_compressed.pdf")

# Defina a resolução para redimensionar as imagens (ex.: 150 DPI ou menos para reduzir o tamanho)
desired_resolution = (600, 800)  # Largura e altura em pixels

# Lista para armazenar as imagens redimensionadas
images = []

for filename in os.listdir(input_folder):
    if filename.lower().endswith(".jpg"):
        image_path = os.path.join(input_folder, filename)
        
        # Abre e redimensiona a imagem
        with Image.open(image_path) as img:
            img = img.convert("RGB")
            img = img.resize(desired_resolution, Image.LANCZOS)  # Usa LANCZOS para redimensionamento de alta qualidade
            images.append(img)

# Salva as imagens redimensionadas em um novo PDF
if images:
    images[0].save(
        output_pdf_path,
        save_all=True,
        append_images=images[1:],
        quality=70,  # Qualidade ajustada para reduzir o tamanho
        optimize=True,
    )

print(f"PDF comprimido salvo!")
