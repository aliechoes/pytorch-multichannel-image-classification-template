import torch
import torchvision
import argparse
from datetime import datetime
import os
import json
import itertools
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from data_loaders.data_loaders import DataLoaderGenerator
from machine_learning.models import get_model
from machine_learning.optimizers import get_optimizer
from machine_learning.losses import get_loss
from tensorboard_writer.tensorboard_writer import TensorBoardSummaryWriter
from train import train
import warnings
warnings.filterwarnings("ignore")

# fix random seeds for reproducibility
#SEED = 123
#torch.manual_seed(SEED)
torch.backends.cudnn.deterministic = False
torch.backends.cudnn.benchmark = True
#np.random.seed(SEED)

def make_folders(desired_path):
    os.mkdir(desired_path)
    return None

def create_name(arch):
    run_name = str(datetime.now()) + "_" + arch
    print("Model Name: %s \n" % run_name)
    return run_name

def load_json(file_path):
    with open(file_path, 'r') as stream:    
        return json.load(stream)

def save_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def get_checkpoint(file_path):
    if file_path is not None:
        checkpoint = torch.load(file_path)
    else:
        checkpoint = None
    return checkpoint