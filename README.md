# YOLOv8 Tennis Match Tracking

## Introduction

Welcome to the YOLOv8 Tennis Player and Ball Tracker project! As the developer, my goal is to provide a comprehensive solution for detecting and tracking players, and ball in videos using the powerful YOLOv8 AI object detection model. Here's what you can expect from this project:

- **Object Detection with YOLOv8**:
  Utilizing YOLOv8, one of the best AI object detection models available, to accurately detect players, referees, and footballs in video footage.

- **Model Training for Performance Improvement**:
  Training the YOLOv5 model to enhance its performance and ensure accurate detection and tracking results.

- **Court Key Point Extracion**:
  Extract the court keypoint and plot the players and ball movement.

This project covers various advanced concepts and addresses real-world problems in tennis match analysis. Whether you're a beginner or an experienced machine learning engineer, you'll find this project both informative and practical. Let's dive in and explore the exciting world of football tracking with AI!

![Screenshot](test)

## Technology Used

The following modules are used in this project:

- YOLOv8: AI object detection model
- Fine Tuned YOLO for tennis ball detection
- Court Key point extraction

## Requirements

To run this project, you need to have the following requirements installed:

- Python 3.x
- ultralytics
- supervision
- OpenCV
- NumPy
- Matplotlib
- Pandas

## Getting started

To run this demo project, create an virtual environment and install the src package:

1. Download the model and copy in models/ folder:

[model](nolink)

2. Download the sample video for the project and copy in input_videos/ folder:

[video](nolink)

3. create .env files with the following secret keys:

```bash
ENV=dev
CONFIG_PATH=
ROBOFLOW_API_KEY=
```

4. Edit config/config.yaml accordingly

```bash
directory:
  input:
  output:
  model:
```

5. Setup the project

```bash
# install src package in development mode to install setup.py
pip install -e .

# install dependencies in requirements.txt file
pip install -r requirements.txt
```

6. Run the main program:

```bash
python src/main.py
```

## Challanges and Recommendation

- to be filled

## Future Improvement

- to be filled
