import cv2
import numpy as np
import os
import sys

def remove_watermark(input_path, output_path, mask_size=25):
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print("[Error] Cannot open input video.")
        return

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"[UnionClean] Processing {frame_count} frames...")

    # Detect watermark region using brightness & static detection
    ret, first_frame = cap.read()
    if not ret:
        print('[Error] Cannot read frame.')
        return

    gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
    watermark_mask = cv2.threshold(gray, 245, 255, cv2.THRESH_BINARY)[1]
    watermark_mask = cv2.dilate(watermark_mask, np.ones((mask_size, mask_size), np.uint8), iterations=1)

    # Reset to start
    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    frame_idx = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cleaned = cv2.inpaint(frame, watermark_mask, 3, cv2.INPAINT_TELEA)
        out.write(cleaned)
        frame_idx += 1
        if frame_idx % 30 == 0:
            print(f"Processed {frame_idx}/{frame_count} frames...")

    cap.release()
    out.release()
    print('[UnionClean] ✔ Cleaning complete! Output saved to:', output_path)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python Union_Cleaner.py <input_video_path>')
    else:
        input_path = sys.argv[1]
        output_dir = os.path.join(os.path.dirname(input_path), 'clean_output')
        output_path = os.path.join(output_dir, os.path.basename(input_path))
        remove_watermark(input_path, output_path)
