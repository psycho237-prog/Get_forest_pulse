# Get_forest_pulse
Visualizing deforestation and fire dynamics in Cameroon using Terra satellite data (MODIS). Generates timelapse animations showing forest loss and fire hotspots from 2001–2022, highlighting environmental and human impacts.
Here’s a professional and complete README.md tailored for your repo “Forest Pulse – NASA Space Apps 2025” project:

# Forest Pulse – The Congo’s Breath in Danger

**Team:** GET  
**NASA Space Apps Challenge 2025**


## 🌍 Project Overview

*Forest Pulse* is an animated visualization project showcasing the dramatic deforestation and fire events in the Congo Basin, with a focus on Cameroon. Using Terra satellite data (MODIS True Color & MODIS Active Fire), we highlight the environmental and human impacts of forest loss and wildfires over the last two decades (2001–2022).

Our goal is to provide an intuitive, time-lapse view of the Congo’s second-largest rainforest, raising awareness about deforestation, climate change, and biodiversity loss.

---

## 🎯 Objectives

- Animate the yearly changes in forest cover using **MODIS Land Cover** data.
- Overlay fire hotspots with **MODIS Active Fire** data to show wildfire impacts.
- Create clear visualizations for educational outreach and scientific storytelling.
- Combine satellite data to deliver a compelling 30-second pitch video.

---

## 📦 Repository Structure

forest-pulse/ ├─ frames_forest/           # Raw True Color images per year ├─ frames_fire/             # Raw Fire images per year ├─ frames_combined/         # Combined forest + fire images ├─ forest_loss_cameroon.gif ├─ fires_cameroon.gif ├─ forest_fire_cameroon.gif ├─ forest_loss_cameroon.mp4 ├─ fires_cameroon.mp4 ├─ forest_fire_cameroon.mp4 ├─ forest_pulse_all_in_one.py   # Python script: download + GIF + MP4 └─ README.md

---

## ⚙️ Getting Started

### 1. Install Dependencies

```bash
pip install requests imageio pillow matplotlib

2. Run the All-in-One Python Script

python forest_pulse_all_in_one.py

This script will:

1. Download MODIS True Color and MODIS Active Fire images for Cameroon (2001–2022).


2. Generate three GIF animations:

Forest cover (forest_loss_cameroon.gif)

Fire hotspots (fires_cameroon.gif)

Combined forest + fires (forest_fire_cameroon.gif)



3. Convert the GIFs to MP4 videos for easier integration in your pitch.




---

📊 Data Sources

MODIS Terra Corrected Reflectance True Color (NASA GIBS / Worldview)

MODIS Terra Active Fire True Color (NASA GIBS / Worldview)


All data are publicly available via NASA’s Earthdata.


---

🎬 Usage

1. Use the MP4 animations to create a 30-second pitch video.


2. Add narration or subtitles for storytelling.


3. Combine GIFs/MP4s with presentation slides if needed.




---

🌱 Impact

Visualizes the environmental changes in Cameroon’s forests.

Highlights the link between deforestation and wildfires.

Educates communities and policymakers about the importance of protecting the Congo Basin.



---

📜 License

This project is open-source and shared under the MIT License. All NASA Earthdata imagery is publicly available.


---

🏆 Team

GET – Global Earth Team
NASA Space Apps Challenge 2025

  
