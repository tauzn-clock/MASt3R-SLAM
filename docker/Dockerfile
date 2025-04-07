FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04
ENV TORCH_CUDA_ARCH_LIST="7.5,8.0+PTX"

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

RUN pip install torchcodec
RUN pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1

RUN git clone https://github.com/tauzn-clock/MASt3R-SLAM.git --recursive

WORKDIR /MASt3R-SLAM
RUN pip install -e thirdparty/mast3r
RUN pip install -e thirdparty/in3d
RUN pip install --no-build-isolation -e .