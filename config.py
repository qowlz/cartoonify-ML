import os
import torch

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

DATA_DIR = "data"
SOURCE_DIR = os.path.join(DATA_DIR, "source")

RESULT_DIR = "results"
TEST_OUTPUT_DIR = os.path.join(RESULT_DIR, "test")
TRAIN_OUTPUT_DIR = os.path.join(RESULT_DIR, "train")

PRE_TRAINED_MODEL_DIR = os.path.join(TRAIN_OUTPUT_DIR, "generator_latest.pkl")

PRE_TRAINED_VGG_DIR = "vgg19-dcbb9e9d.pth"