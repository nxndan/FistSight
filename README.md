# FistSight
Real‑time hand‑gesture recognition using Mediapipe + OpenCV to trigger automated system actions.

FistSight is a real‑time computer‑vision system that detects hand gestures using Mediapipe’s Hand Landmarker and triggers automated desktop actions. The current implementation recognizes a closed‑fist gesture and captures a full‑screen screenshot using PyAutoGUI.

The system tracks 21 hand landmarks, evaluates finger‑fold states, and classifies a “FIST” gesture when all four fingers are folded. When detected, the program triggers a PyAutoGUI screenshot and saves it locally.


