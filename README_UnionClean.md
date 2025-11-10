# 🧼 Union_Cleaner v1.0

**Union_Cleaner** removes visible watermarks and overlay logos from video files using a pure‑Python approach (OpenCV + NumPy).  

### ⚙️ How to use:
1. Install Python 3.10+ and required packages:
   ```bash
   pip install -r requirements.txt
   ```
2. Place your input video in the same folder or specify its full path.
3. Run the cleaner:
   ```bash
   python Union_Cleaner.py input.mp4
   ```
4. Find cleaned output inside `/clean_output/`.

### 🧩 Options:
- Adjust `mask_size` (default 25) in code for thick / thin watermarks.
- Works with MP4, MOV, AVI formats.

### 📜 Algorithm:
1. Detect watermark region via brightness threshold.
2. Expand mask (dilate) to include halo/edges.
3. Apply OpenCV Telea Inpainting to reconstruct pixels underneath.

### 🔒 Philosophy:  
*No credits, no signatures — only clean, autonomous frames.*  
_“Clean act defines the hidden pulse.”_
