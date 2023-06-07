import torch
from skimage.io import imread
from torch.utils import data

class SegmentationDataSet(data.Dataset):
    def __init__(self,inputs : list,targets :list ,transform = None):
        self.inputs = inputs
        self.targets = targets
        self.transform = transform 



    def __len__(self):
        return len(self.inputs)
    

    def __getitem__(self,
                    index : int):
        
        #select the sample
        input_idx = self.inputs[index]
        target_idx = self.inputs[index]


        #load input and target
        x,y = imread(input_idx),imread(target_idx)


        #preprocessing
        if self.transform is not None:
            x,y = self.transform(x,y)


        #typecasting
        

