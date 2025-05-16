import os
import shutil
import random
from pathlib import Path

# === CONFIG ===
base_dir = Path("data")
image_exts = [".jpg", ".jpeg", ".png"]
val_ratio = 0.2

# Step 1: Flatten the folder
images_src = base_dir / "images/folder_2"
labels_src = base_dir / "labels/folder_2"

all_images = [f for f in images_src.iterdir() if f.suffix.lower() in image_exts]
random.shuffle(all_images)

# Step 2: Create YOLO-style structure
for split in ["train", "val"]:
    os.makedirs(base_dir / f"images/{split}", exist_ok=True)
    os.makedirs(base_dir / f"labels/{split}", exist_ok=True)

split_index = int(len(all_images) * (1 - val_ratio))
train_imgs = all_images[:split_index]
val_imgs = all_images[split_index:]

# Step 3: Move files
def move_files(images, split):
    for img_path in images:
        name = img_path.stem
        label_path = labels_src / f"{name}.txt"

        # Destination paths
        img_dst = base_dir / f"images/{split}" / img_path.name
        label_dst = base_dir / f"labels/{split}" / f"{name}.txt"

        shutil.copy(img_path, img_dst)
        if label_path.exists():
            shutil.copy(label_path, label_dst)

move_files(train_imgs, "train")
move_files(val_imgs, "val")

print("✅ Dataset split into train and val.")
