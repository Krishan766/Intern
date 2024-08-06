import torch
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the YOLOv5 model from PyTorch Hub
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Load an image using OpenCV
image_path = '/Users/krishansmacbook/Downloads/Pycharm/pythonProject/Traficc.jpg'  # Replace with your image path
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Perform inference
results = model(image_rgb)

# Parse the results
detections = results.pandas().xyxy[0]  # Bounding boxes in Pandas DataFrame

# Draw bounding boxes and labels on the image
for index, row in detections.iterrows():
    x1, y1, x2, y2 = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
    label = row['name']
    confidence = row['confidence']

    # Draw bounding box
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Put label and confidence
    text = f'{label} {confidence:.2f}'
    cv2.putText(image, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# Save the result
output_image_path = '/Users/krishansmacbook/Downloads/Pycharm/pythonProject/output_image.jpg'
cv2.imwrite(output_image_path, image)  # Save the result

# Display the result using matplotlib
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')  # Turn off axis
plt.show()
