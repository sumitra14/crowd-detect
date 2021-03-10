import sys
sys.path.append('/content/drive/My Drive/CROWD-DETECT')
import h5py
import scipy.io as io
import PIL.Image as Image
import numpy as np
import os
import glob
from matplotlib import pyplot as plt
from scipy.ndimage.filters import gaussian_filter
import scipy
import scipy.spatial
import json
from matplotlib import cm as CM
from image import *
from model import CSRNet
import torch
from tqdm import tqdm
#%matplotlib inline
import matplotlib.pyplot
import io

def prediction(image_bytes):
    from torchvision import datasets, transforms
    transform=transforms.Compose([transforms.ToTensor(),transforms.Normalize(mean=[0.485, 0.456, 0.406],std=[0.229, 0.224, 0.225]),])
    model = CSRNet()
    model = model.cuda()
    checkpoint = torch.load('ShanghaiTech_Crowd_Counting_Dataset/part_A_final/0model_best.pth.tar')
    model.load_state_dict(checkpoint['state_dict'])
    img = transform(Image.open(image_bytes).convert('RGB')).cuda()
    output = model(img.unsqueeze(0))
    a=int(output.detach().cpu().sum().numpy())
    return a
