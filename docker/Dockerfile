FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04

RUN apt-get update && apt-get install -y \
    git \
    wget \
    nano \ 
    libglib2.0-0 \
    python3 \
    python3-dev \
    python3-pip \
    freeglut3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install torch

RUN git clone https://github.com/tauzn-clock/MASt3R-SLAM.git --recursive

RUN pip install torchcodec

WORKDIR /MASt3R-SLAM
