---

# COS40007 Design Project

COS40007 students are expected to undertake a design project on a focused topic of AI for Engineering. Students will receive sample datasets, and may also collect similar data independently. More details on the projects will be discussed in Week 4 and 5 seminars.

---

## A. Grouping Rules

- Groups must contain 4–5 students.
- Groups must be formed within the same studio session unless special permission is granted.
- If you've changed studio sessions, inform your tutor.

**Group deliverables:**

- Project Brief  
- Data Labelling  
- Data Exploration & Pre-processing  
- Model Training and Validation  
- Model Evaluation  
- AI Demonstrator  
- Project Presentation  
- Final Report  

---

## B. Rubric, Report, and Project Progress

- Rubric available mid-semester.
- Final report outline released after mid-semester.
- Studio sessions post mid-semester will be used to review progress.

---

## C. Project Topics

- Apply AI knowledge to a selected engineering problem.
- Develop a project brief and plan.
- You may choose your own tech stack.

---

## D. Project Themes

Submit group members, student IDs, studio, and ranked preferences [via this form](https://forms.office.com/r/aBsdn1SNg9) by **noon, 7 April**. First preferences are not guaranteed.

---

### Theme 1: Smart City / Civil and Construction Engineering

**AI Areas:** Deep Learning, Object Classification, Anomaly Detection  
**Data:** Roadside images  

**Topic:** Detect roadside asset issues from vehicle-captured images (e.g., dumped rubbish, damaged signs).  

**Key Questions:**
1. What issue is detected?
2. What is the specific type of issue?

**Model:**
- **Input:** Image
- **Output:**
  - Identified issue + confidence score
  - Identified object + confidence score

**Data Source:**  
Contains images in folders: `rubbish`, `not_rubbish`, `damaged-sign3`.  
Annotate bounding boxes and label object types or damage types.

[Dataset Link](https://liveswinburneeduau-my.sharepoint.com/:f:/g/personal/fforkan_swin_edu_au/Es-xaGQBmtBCtW6I4G1wop0B0KACoFK3VMeRLVpLp1GyVg?e=HGMLRJ)

**Marking:**

| Task                                  | Weight |
|---------------------------------------|--------|
| Data labelling & image processing     | 40%    |
| Training & validation                 | 20%    |
| Detection on unseen data              | 15%    |
| Evaluation metrics                    | 15%    |
| User Interface                        | 10%    |

---

### Theme 2: Electronics / Biomedical Engineering

**AI Areas:** Activity Recognition, Predictive Analytics  
**Data:** Raw motion sensor data  

**Topic:** Detect worker activity & knife sharpness in a manufacturing setting.

**Key Questions:**
1. What activity is being performed?
2. What is the knife sharpness & when should it be sharpened?

**Model:**
- **Input:** 1-minute raw sensor data
- **Output:**
  - Activity
  - Knife sharpness & recommendation

**Data Source:**  
Folders `P1`, `P2` → boning/slicing → .xlsx with sensor data (Segment Velocity & Acceleration).  
Label knife sharpness as:
- Sharp: ≥ 85  
- Medium: 70–84  
- Blunt: < 70  

[Dataset Link](https://liveswinburneeduau-my.sharepoint.com/:f:/r/personal/fforkan_swin_edu_au/Documents/COS40007/Design%20Project/Theme2?csf=1&web=1&e=Ci09zn)

**Marking:**

| Task                                      | Weight |
|------------------------------------------|--------|
| Data preprocessing & feature extraction  | 40%    |
| ML model training & validation           | 20%    |
| Classification on unseen data            | 15%    |
| Evaluation & model comparison            | 15%    |
| User Interface                            | 10%    |

---

### Theme 3: Product Manufacturing / Mechanical Engineering

**AI Areas:** Machine Learning, Prescriptive Analytics  
**Data:** Machine settings & sensor data  

**Topic:** Recommend machine settings for desired product consistency & detect downtime anomalies.

**Key Questions:**
1. What settings yield desired product quality?
2. What anomalies may cause failures?

**Model:**
- **Input:** Sensor + settings
- **Output:**
  - Recommended settings
  - Detected anomalies

**Data Source:**  
`data_02_07_2019-26-06-2020` folder: 3 CSVs (`good`, `low_bad`, `high_bad`)  
`Downtime` folder for shutdown info (May–June 2020).

[Dataset Link](https://liveswinburneeduau-my.sharepoint.com/:f:/g/personal/fforkan_swin_edu_au/Ejt71qYd0mFIjE-MJLjyIIoBcCRqWfsEREfENZYoaamI5g?e=Z24s3u)

**Marking:**

| Task                                        | Weight |
|--------------------------------------------|--------|
| Data preprocessing & feature extraction    | 35%    |
| Model training & validation                | 20%    |
| SP recommendations & downtime prediction   | 25%    |
| Evaluation metrics                         | 10%    |
| User Interface                             | 10%    |

---

### Theme 4: Structural / Chemical Engineering

**AI Areas:** Deep Learning, Defect Detection  
**Data:** Structural defect images  

**Topic:** Detect and classify structural defects in images.

**Key Questions:**
1. Are there structural defects?
2. What type (e.g., corrosion, crack)?

**Model:**
- **Input:** Image
- **Output:**
  - Detection + confidence
  - Type + confidence

**Data Source:**  
"tower" folder: drone images of towers with corrosion.  
Use polygon and bounding box annotations.

[Dataset Link](https://liveswinburneeduau-my.sharepoint.com/:f:/g/personal/fforkan_swin_edu_au/EqXk88nqL4xBhAunAi0Ai8gBshRRkAhgIb8mUH3dRwL8mw?e=DfBbhS)

**Marking:**

| Task                                  | Weight |
|--------------------------------------|--------|
| Data labelling & image processing    | 40%    |
| Training & validation                | 20%    |
| Object & issue detection             | 15%    |
| Evaluation metrics                   | 15%    |
| User Interface                       | 10%    |

---

### Theme 5: Electrical / Telecom Engineering

**AI Areas:** Clustering, Predictive Analytics  
**Data:** 5G performance CSV data  

**Topic:** Cluster zones by performance & predict future performance.

**Key Questions:**
1. How many groups/zones exist based on performance?
2. What is the future performance of a zone?

**Model:**
- **Input:** 5G performance data
- **Output:**
  - Zone/group classification
  - Performance prediction

**Data Source:**  
`data` folder contains CSVs named by date and truck number.  
Includes GPS, speed, latency, and throughput measures.

[Dataset Link](https://liveswinburneeduau-my.sharepoint.com/:f:/g/personal/fforkan_swin_edu_au/EgwxQCu_xnlAmPkx63j9h2MBBmqza_pE_78ncbDuSWj-Ww?e=DrKcJa)

**Marking:**

| Task                                | Weight |
|------------------------------------|--------|
| Data preprocessing & feature extraction | 40% |
| Model training                     | 20%    |
| Clustering / forecasting           | 15%    |
| Evaluation metrics                 | 15%    |
| User Interface                     | 10%    |

---