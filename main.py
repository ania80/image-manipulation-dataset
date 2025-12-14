import cv2
import numpy as np
import os

# Create output directories
os.makedirs("output/original", exist_ok=True)
os.makedirs("output/blur", exist_ok=True)
os.makedirs("output/noise", exist_ok=True)

# Load image
img = cv2.imread("eagle.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Save original
cv2.imwrite(
    "output/original/original.jpg",
    cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
)

# Blur image
blur = cv2.GaussianBlur(img, (15, 15), 0)
cv2.imwrite(
    "output/blur/blur.jpg",
    cv2.cvtColor(blur, cv2.COLOR_RGB2BGR)
)

# Add noise
noise = img + np.random.normal(0, 25, img.shape)
noise = np.clip(noise, 0, 255).astype(np.uint8)
cv2.imwrite(
    "output/noise/noise.jpg",
    cv2.cvtColor(noise, cv2.COLOR_RGB2BGR)
)

print("Done! Image variants created.")
