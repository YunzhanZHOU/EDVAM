# Practical subset usage
# PyTorch dataset

import numpy as np
import torch
from torch.utils.data import Dataset

train_set = np.load('./train.npy')
train_label = np.load('./train_label.npy')

class EyeTrackingDataset(Dataset):
    
    def __init__(self, train_set, train_label):
        self.train_set = train_set
        self.train_label = train_label

    def __len__(self):
        return len(self.train_set)

    def __getitem__(self,idx):
        sample = {'data': self.train_set[idx], 'labels': self.train_label[idx]}
        return sample

dataset = EyeTrackingDataset(train_set, train_label)
