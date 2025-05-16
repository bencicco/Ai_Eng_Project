import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
from ultralytics import YOLO
import numpy as np

# Load YOLO model
model = YOLO('runs\\detect\\train27\\weights\\best.pt')  # adjust path as needed

# Inference + plotting function
def annotate_image(image_path):
    results = model(image_path)

    # Get annotated result as an image (numpy array)
    result_img = results[0].plot()  # BGR image with annotations
    return result_img, results

# GUI app
class YOLO_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("YOLOv8 Image Annotator")
        self.root.geometry("800x600")

        self.label = tk.Label(root, text="Upload an image to annotate", font=("Arial", 14))
        self.label.pack(pady=10)

        self.canvas = tk.Canvas(root, width=700, height=500)
        self.canvas.pack()

        self.upload_button = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(pady=10)

        self.image_on_canvas = None

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
        if not file_path:
            return

        # Annotate image
        annotated_img, results = annotate_image(file_path)

        # Convert BGR to RGB for Tkinter
        annotated_img_rgb = cv2.cvtColor(annotated_img, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(annotated_img_rgb)
        pil_image = pil_image.resize((700, 500), Image.Resampling.LANCZOS)  # Resize for canvas
        tk_image = ImageTk.PhotoImage(pil_image)

        # Display on canvas
        self.canvas.delete("all")
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor="nw", image=tk_image)
        self.canvas.image = tk_image  # keep reference

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = YOLO_GUI(root)
    root.mainloop()
