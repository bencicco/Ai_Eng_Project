import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
from ultralytics import YOLO
import threading
import time

# Load YOLO model
model = YOLO('runs\\detect\\train27\\weights\\best.pt')

# Inference + annotation for image path
def annotate_image(image_path):
    results = model(image_path)
    return results[0].plot(), results[0]  # BGR image and detection result

# Inference + annotation for frame
def annotate_frame(frame):
    results = model(frame)
    return results[0].plot(), results[0]  # BGR image and detection result

class YOLO_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("YOLOv8 Annotator")
        self.root.geometry("1000x600")

        # Layout frames
        self.left_frame = tk.Frame(root)
        self.left_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.right_frame = tk.Frame(root)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

        # Canvas for image or webcam stream
        self.canvas = tk.Canvas(self.left_frame, width=700, height=500)
        self.canvas.pack()

        # Buttons
        self.upload_button = tk.Button(self.left_frame, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(side=tk.LEFT, padx=5, pady=10)

        self.cam_button = tk.Button(self.left_frame, text="Start Camera", command=self.start_camera)
        self.cam_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = tk.Button(self.left_frame, text="Stop Camera", command=self.stop_camera, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=5)

        # Detection result panel (scrollable)
        tk.Label(self.right_frame, text="Detections", font=("Arial", 12, "bold")).pack()
        self.text_area = tk.Text(self.right_frame, width=30, height=30, wrap=tk.WORD)
        self.text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(self.right_frame, command=self.text_area.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_area.config(yscrollcommand=scrollbar.set)

        # Camera
        self.cap = None
        self.running = False

        self.limit_fps = False
        self.target_fps = 30
        self.frame_duration = 1.0/self.target_fps

    def upload_image(self):
        self.stop_camera()
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
        if not file_path:
            return
        annotated_img, results = annotate_image(file_path)
        self.display_image(annotated_img)
        self.display_detections(results)

    def start_camera(self):
        if self.running:
            return
        self.running = True
        self.cap = cv2.VideoCapture(0)
        self.stop_button.config(state=tk.NORMAL)
        self.cam_button.config(state=tk.DISABLED)
        threading.Thread(target=self.camera_loop, daemon=True).start()

    def stop_camera(self):
        self.running = False
        if self.cap:
            self.cap.release()
            self.cap = None
        self.stop_button.config(state=tk.DISABLED)
        self.cam_button.config(state=tk.NORMAL)

    def camera_loop(self):
        while self.running and self.cap.isOpened():
            ret, frame = self.cap.read()
            frame_start = time.perf_counter()
            if not ret:
                break
            frame = cv2.flip(frame, 1)
            annotated_frame, results = annotate_frame(frame)
            self.display_image(annotated_frame)
            self.display_detections(results)
            delta_time = time.perf_counter() - frame_start
            sleep_time = self.frame_duration - delta_time
            if sleep_time > 0 and self.limit_fps:
                time.sleep(sleep_time)
        self.stop_camera()

    def display_image(self, bgr_img):
        rgb_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(rgb_img).resize((700, 500), Image.Resampling.LANCZOS)
        tk_img = ImageTk.PhotoImage(img_pil)

        if not hasattr(self, 'image_id'):
            self.image_id = self.canvas.create_image(0, 0, anchor="nw", image=tk_img)
        else:
            self.canvas.itemconfig(self.image_id, image=tk_img)
        
        self.canvas.image = tk_img  # prevent GC

    def display_detections(self, result):
        self.text_area.delete(1.0, tk.END)  # Clear previous
        if not result or not result.boxes:
            self.text_area.insert(tk.END, "No detections.")
            return

        for box in result.boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            label = model.names[cls_id]
            self.text_area.insert(tk.END, f"{label}: {conf:.2f}\n")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = YOLO_GUI(root)
    root.mainloop()
