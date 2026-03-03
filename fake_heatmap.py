import cv2
import numpy as np
import matplotlib.pyplot as plt
import uuid
import os

def generate_fake_density_map(image_path, detections, output_folder="static/outputs"):
    """
    detections = list of bounding boxes → [(x1, y1, x2, y2), ...]
    """

    img = cv2.imread(image_path)
    h, w, _ = img.shape

    # Create black heatmap
    heatmap = np.zeros((h, w), dtype=np.float32)

    # Each detection increases heat intensity
    for (x1, y1, x2, y2) in detections:
        cx = int((x1 + x2) / 2)   # center X
        cy = int((y1 + y2) / 2)   # center Y

        cv2.circle(heatmap, (cx, cy), 80, 1, -1)  # 80 pixel radius heat point

    heatmap = cv2.GaussianBlur(heatmap, (0, 0), sigmaX=50)

    heatmap_norm = cv2.normalize(heatmap, None, 0, 255, cv2.NORM_MINMAX)
    heatmap_norm = heatmap_norm.astype(np.uint8)

    heatmap_color = cv2.applyColorMap(heatmap_norm, cv2.COLORMAP_JET)

    # Blend heatmap + input image
    overlay = cv2.addWeighted(img, 0.5, heatmap_color, 0.7, 0)

    filename = f"heatmap_{uuid.uuid4().hex}.jpg"
    output_path = os.path.join(output_folder, filename)

    cv2.imwrite(output_path, overlay)

    return output_path
