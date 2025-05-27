"""
YOLOv8 video inference script (constants only)
============================================
Takes an input MP4, runs inference frame‑by‑frame with a trained Ultralytics
YOLO model, draws the predictions, and writes an annotated MP4.

All configuration is hard‑coded below so you can just `python yolo_video_inference.py`
without any arguments.
"""

from pathlib import Path
import cv2
from ultralytics import YOLO

# ───────────────────────── Constants ──────────────────────────
MODEL_WEIGHTS = Path("best.pt")  # path to .pt file
SOURCE_VIDEO  = Path("VIDEO_FOR_DEMO.MP4")              # input video
OUTPUT_VIDEO  = Path("test.mp4")    # output video
IMG_SIZE      = 640                                           # inference image size
CONF_THRESHOLD = 0.20                                        # confidence threshold

# ───────────────────────── Helpers ────────────────────────────

def draw_boxes(frame, results, names):
    """Draw bounding boxes and labels on a frame."""
    for box in results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0])
        cls = int(box.cls[0])
        if conf < CONF_THRESHOLD:
            continue
        label = f"{names[cls]} {conf:.2f}"
        color = (0, 255, 0)
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        (tw, th), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)
        cv2.rectangle(frame, (x1, y1 - th - 4), (x1 + tw, y1), color, -1)
        cv2.putText(frame, label, (x1, y1 - 2), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 1, cv2.LINE_AA)
    return frame


def annotate_video(model, input_path, output_path = OUTPUT_VIDEO):
    names = model.names

    cap = cv2.VideoCapture(str(SOURCE_VIDEO))
    if not cap.isOpened():
        return output_path, 0

    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps    = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(str(OUTPUT_VIDEO), fourcc, fps, (width, height))

    frame_idx = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        results = model.predict(frame, imgsz=IMG_SIZE, conf=CONF_THRESHOLD, verbose=False)
        if results:
            frame = draw_boxes(frame, results[0], names)
        out.write(frame)
        frame_idx += 1

    cap.release()
    out.release()
    return output_path, frame_idx

# ───────────────────────── Main ───────────────────────────────

def main():
    model = YOLO(str(MODEL_WEIGHTS))
    

    _,frame_idx = annotate_video(model, SOURCE_VIDEO)
    print(f"Finished! Saved annotated video to {OUTPUT_VIDEO} (processed {frame_idx} frames).")


if __name__ == "__main__":
    main()
