# yolov5-archive
# Computer Vision Object Detection System

## 📖 Overview
This project implements a graphical user interface (GUI)-based object detection system using **PyQt5** and **YOLOv5**. Users can upload images or videos, perform real-time object detection, and view results through an intuitive interface. The system supports model switching, multi-threaded video processing, and result saving for later analysis.

---

## 🛠️ Environment Setup

### Prerequisites
- **Python**: 3.8 or higher
- **OS**: Windows (recommended)
- **GPU**: NVIDIA GPU (optional for CUDA acceleration)
### CUDA & PyTorch Configuration

Check CUDA Version:
Ensure your GPU supports CUDA. Run nvidia-smi in the command line to check compatibility.

Install CUDA Toolkit:
Download the CUDA Toolkit version compatible with your GPU from NVIDIA's website.

Install PyTorch with CUDA:

Visit PyTorch's official site to install the correct PyTorch version for your CUDA. Example:
```bash
pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 --extra-index-url https://download.pytorch.org/whl/cu113
### Dependencies
Install required libraries:
```bash
pip install PyQt5 numpy opencv-python torch torchvision

