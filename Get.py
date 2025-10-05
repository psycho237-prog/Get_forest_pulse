import requests, imageio, os
from PIL import Image, ImageDraw, ImageFont

# ===============================
# Forest Pulse – NASA Space Apps 2025
# Tout-en-un : téléchargement, animation et MP4 avec année
# ===============================

# Paramètres
bbox = "8,2,17,7"  # Cameroun
years = range(2001, 2023)
frame_size = (512, 512)
duration = 0.8  # secondes par frame
base_url = "https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi"

# Créer dossiers
os.makedirs("frames_forest", exist_ok=True)
os.makedirs("frames_fire", exist_ok=True)
os.makedirs("frames_combined", exist_ok=True)

# Stockage frames
forest_frames, fire_frames, combined_frames = [], [], []

# Police pour texte
try:
    font = ImageFont.truetype("arial.ttf", 30)
except:
    font = ImageFont.load_default()

for year in years:
    print(f"Téléchargement et traitement {year} ...")

    # ---- 1. Image TrueColor (forêt) ----
    url_forest = f"{base_url}?service=WMS&version=1.3.0&request=GetMap" \
                 f"&layers=MODIS_Terra_CorrectedReflectance_TrueColor" \
                 f"&styles=&format=image/png&transparent=false&height={frame_size[1]}&width={frame_size[0]}" \
                 f"&bbox={bbox}&time={year}-01-01"
    img_forest = Image.open(requests.get(url_forest, stream=True).raw).convert("RGBA")
    
    # Ajouter l'année sur l'image
    draw = ImageDraw.Draw(img_forest)
    draw.text((10, 10), f"Year: {year}", fill="white", font=font)
    
    img_forest.save(f"frames_forest/forest_{year}.png")
    forest_frames.append(imageio.imread(f"frames_forest/forest_{year}.png"))

    # ---- 2. Image Fire ----
    url_fire = f"{base_url}?service=WMS&version=1.3.0&request=GetMap" \
               f"&layers=MODIS_Terra_Fire_TrueColor" \
               f"&styles=&format=image/png&transparent=true&height={frame_size[1]}&width={frame_size[0]}" \
               f"&bbox={bbox}&time={year}-01-01"
    img_fire = Image.open(requests.get(url_fire, stream=True).raw).convert("RGBA")
    
    # Ajouter l'année sur l'image
    draw = ImageDraw.Draw(img_fire)
    draw.text((10, 10), f"Year: {year}", fill="white", font=font)
    
    img_fire.save(f"frames_fire/fire_{year}.png")
    fire_frames.append(imageio.imread(f"frames_fire/fire_{year}.png"))

    # ---- 3. Combinaison forêt + feux ----
    combined = Image.alpha_composite(img_forest, img_fire)
    combined.save(f"frames_combined/combined_{year}.png")
    combined_frames.append(imageio.imread(f"frames_combined/combined_{year}.png"))

# ---- Créer GIFs ----
imageio.mimsave("forest_loss_cameroon.gif", forest_frames, duration=duration)
imageio.mimsave("fires_cameroon.gif", fire_frames, duration=duration)
imageio.mimsave("forest_fire_cameroon.gif", combined_frames, duration=duration)
print("✅ GIFs créés avec l'année affichée")

# ---- Conversion GIF → MP4 ----
def gif_to_mp4(gif_file):
    mp4_file = gif_file.replace(".gif", ".mp4")
    reader = imageio.get_reader(gif_file)
    fps = reader.get_meta_data().get('fps', 1)
    writer = imageio.get_writer(mp4_file, fps=fps)
    for frame in reader:
        writer.append_data(frame)
    writer.close()
    print(f"✅ Converti : {gif_file} → {mp4_file}")

for gif in ["forest_loss_cameroon.gif", "fires_cameroon.gif", "forest_fire_cameroon.gif"]:
    gif_to_mp4(gif)

print("🎬 Toutes les animations sont prêtes en GIF et MP4 avec l'année affichée !")
