import os
from rembg import remove

input_folder = "hadi/Camera"
output_folder = "hadi/Camera/rmbg"

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    if file.lower().endswith((".jpg", ".jpeg", ".png")):
        with open(os.path.join(input_folder, file), "rb") as inp:
            with open(os.path.join(output_folder, file + ".png"), "wb") as out:
                out.write(remove(inp.read()))
