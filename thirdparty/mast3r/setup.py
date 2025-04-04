from pathlib import Path
from setuptools import setup

curope = Path(__file__).parent.resolve() / "dust3r" / "croco" / "models" / "curope"
asmk = Path(__file__).parent.resolve() / "asmk"

setup(
    name = "mast3r",
    install_requires=[
        "scikit-learn",
        "roma",
        "gradio",
        "matplotlib",
        "tqdm",
        "opencv-python",
        "scipy",
        "einops",
        "trimesh",
        "tensorboard",
        "pyglet",
        "huggingface-hub[torch]>=0.22",
        f"asmk @ {asmk.as_uri()}",
        f"curope @ {curope.as_uri()}",
    ],
)
