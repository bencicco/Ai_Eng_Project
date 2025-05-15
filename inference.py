from ultralytics import YOLO

# Load your trained model
model = YOLO('runs\\detect\\train7\\weights\\best.pt')  # replace with your model path

# Perform prediction on an image
results = model('data\\images\\val\\GMU.1-3-2022-1646079386795.jpg')  # replace with your image path

# Process results
for result in results:
    boxes = result.boxes  # Bounding boxes
    
    # Print detection results
    for box in boxes:
        # Get box coordinates
        x1, y1, x2, y2 = box.xyxy[0]  # get box coordinates in (x1, y1, x2, y2) format
        conf = box.conf[0]  # confidence score
        cls = int(box.cls[0])  # class id
        
        print(f"Detected {model.names[cls]} with confidence {conf:.2f} at location {x1:.2f}, {y1:.2f}, {x2:.2f}, {y2:.2f}")

# Optionally save results with bounding boxes
result_image = results[0].plot()  # plot a BGR numpy array of predictions
import cv2
cv2.imwrite('result.jpg', result_image)  # save the result image